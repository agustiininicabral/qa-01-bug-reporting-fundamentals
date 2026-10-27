"""Validate the structure and internal consistency of QA portfolio artifacts."""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES_PATH = ROOT / "03-work" / "test-cases.csv"
BUG_REPORTS_DIR = ROOT / "03-work" / "bug-reports"
RESULTS_PATH = ROOT / "05-results" / "report.md"
REQUIRED_CASE_COLUMNS = {
    "id",
    "feature",
    "title",
    "priority",
    "precondition",
    "steps",
    "expected",
    "status",
}
VALID_PRIORITIES = {"P0", "P1", "P2", "P3"}
VALID_STATUSES = {"Not executed", "Pass", "Fail", "Blocked", "Not applicable"}
REQUIRED_BUG_REPORT_SECTIONS = (
    "## Ambiente",
    "## Precondiciones",
    "## Pasos para reproducir",
    "## Resultado actual",
    "## Resultado esperado",
    "## Evidencia",
    "## Criterio de cierre",
)


def validate_test_cases() -> tuple[list[str], list[dict[str, str]]]:
    errors: list[str] = []
    try:
        with CASES_PATH.open(newline="", encoding="utf-8-sig") as stream:
            reader = csv.DictReader(stream)
            columns = set(reader.fieldnames or [])
            if not REQUIRED_CASE_COLUMNS.issubset(columns):
                missing = sorted(REQUIRED_CASE_COLUMNS - columns)
                return [f"Test case CSV is missing columns: {', '.join(missing)}"], []
            rows = list(reader)
    except OSError as error:
        return [f"Unable to read test case CSV: {error}"], []

    if not rows:
        errors.append("Test case CSV contains no test cases.")

    seen_ids: set[str] = set()
    for row_number, row in enumerate(rows, start=2):
        case_id = (row.get("id") or "").strip()
        if not case_id:
            errors.append(f"CSV row {row_number}: test case ID is empty.")
        elif case_id in seen_ids:
            errors.append(f"CSV row {row_number}: duplicate test case ID {case_id}.")
        seen_ids.add(case_id)

        for field in ("feature", "title", "precondition", "steps", "expected", "status"):
            if not (row.get(field) or "").strip():
                errors.append(f"CSV row {row_number}: {field} is empty.")

        if (row.get("priority") or "").strip() not in VALID_PRIORITIES:
            errors.append(f"CSV row {row_number}: invalid priority.")

        status = (row.get("status") or "").strip()
        if status not in VALID_STATUSES:
            errors.append(f"CSV row {row_number}: invalid status {status!r}.")

        title = (row.get("title") or "").strip().lower()
        if title.startswith("validar escenario"):
            errors.append(f"CSV row {row_number}: generic placeholder title remains.")

    return errors, rows


def validate_bug_reports() -> list[str]:
    errors: list[str] = []
    reports = sorted(BUG_REPORTS_DIR.glob("BR-*.md"))
    if not reports:
        return ["No bug reports found under 03-work/bug-reports."]

    for path in reports:
        content = path.read_text(encoding="utf-8")
        expected_id = path.stem
        if expected_id not in content:
            errors.append(f"{path.name}: report ID does not match its filename.")
        for section in REQUIRED_BUG_REPORT_SECTIONS:
            if section not in content:
                errors.append(f"{path.name}: missing section {section}.")
        if not re.search(r"\*\*Estado:\*\*\s*\S", content):
            errors.append(f"{path.name}: status is missing.")
        if "Pendiente de reproducción" not in content and "No reproducible" not in content:
            if "Confirmado" in content and "No se adjunta captura" in content:
                errors.append(f"{path.name}: confirmed defect has no evidence.")

    return errors


def validate_results(rows: list[dict[str, str]]) -> list[str]:
    if not RESULTS_PATH.is_file():
        return ["Results report is missing."]

    report = RESULTS_PATH.read_text(encoding="utf-8")
    designed = len(rows)
    executed = sum(
        (row.get("status") or "").strip() not in {"Not executed", "Not applicable"}
        for row in rows
    )
    errors: list[str] = []

    if f"- Casos diseñados: {designed}" not in report:
        errors.append(f"Results report must state {designed} designed test cases.")
    if f"- Casos ejecutados: {executed}" not in report:
        errors.append(f"Results report must state {executed} executed test cases.")
    if "Estado global:" not in report:
        errors.append("Results report must state the overall execution status.")

    if executed == 0:
        for label in ("Pass", "Fail", "Blocked"):
            if f"- {label}: N/A" not in report:
                errors.append(f"Results report must mark {label} as N/A when no cases ran.")
        if "Estado global: **No evaluado**" not in report:
            errors.append("Results report must not claim an execution result before testing.")

    return errors


def main() -> int:
    errors, rows = validate_test_cases()
    errors.extend(validate_bug_reports())
    errors.extend(validate_results(rows))

    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors), file=sys.stderr)
        return 1

    print(
        f"Validated {len(rows)} test cases, "
        f"{len(list(BUG_REPORTS_DIR.glob('BR-*.md')))} bug reports, and the results report."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
