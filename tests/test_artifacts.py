from __future__ import annotations

import csv
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import validate_artifacts  # noqa: E402


class ArtifactValidatorTests(unittest.TestCase):
    def test_repository_artifacts_are_consistent(self) -> None:
        case_errors, rows = validate_artifacts.validate_test_cases()
        self.assertEqual(case_errors, [])
        self.assertEqual(validate_artifacts.validate_bug_reports(), [])
        self.assertEqual(validate_artifacts.validate_results(rows), [])
        self.assertEqual(len(rows), 15)

    def test_rejects_duplicate_test_case_ids(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "test-cases.csv"
            fields = [
                "id",
                "feature",
                "title",
                "priority",
                "precondition",
                "steps",
                "expected",
                "status",
            ]
            row = {
                "id": "TC-001",
                "feature": "Cart",
                "title": "Add a product",
                "priority": "P1",
                "precondition": "Product page is open",
                "steps": "Select Add to cart",
                "expected": "Product appears in cart",
                "status": "Not executed",
            }
            with path.open("w", newline="", encoding="utf-8") as stream:
                writer = csv.DictWriter(stream, fieldnames=fields)
                writer.writeheader()
                writer.writerow(row)
                writer.writerow(row)

            with patch.object(validate_artifacts, "CASES_PATH", path):
                errors, rows = validate_artifacts.validate_test_cases()

        self.assertEqual(len(rows), 2)
        self.assertTrue(any("duplicate test case ID" in error for error in errors))

    def test_results_must_match_case_execution_status(self) -> None:
        rows = [{"status": "Not executed"}, {"status": "Pass"}]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "report.md"
            path.write_text(
                "- Casos diseñados: 2\n"
                "- Casos ejecutados: 0\n"
                "- Pass: N/A\n"
                "- Fail: N/A\n"
                "- Blocked: N/A\n"
                "Estado global: **No evaluado**\n",
                encoding="utf-8",
            )
            with patch.object(validate_artifacts, "RESULTS_PATH", path):
                errors = validate_artifacts.validate_results(rows)

        self.assertTrue(any("1 executed test cases" in error for error in errors))


    def test_results_report_must_match_pass_fail_and_blocked_counts(self) -> None:
        rows = [
            {"status": "Pass"},
            {"status": "Fail"},
            {"status": "Blocked"},
            {"status": "Not executed"},
        ]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "report.md"
            path.write_text(
                "- Casos diseñados: 4\\n"
                "- Casos ejecutados: 3\\n"
                "- Pass: 2\\n"
                "- Fail: 0\\n"
                "- Blocked: 1\\n"
                "Estado global: **No-Go**\\n",
                encoding="utf-8",
            )
            with patch.object(validate_artifacts, "RESULTS_PATH", path):
                errors = validate_artifacts.validate_results(rows)

        self.assertTrue(any("1 cases with status Pass" in error for error in errors))
        self.assertTrue(any("1 cases with status Fail" in error for error in errors))

    def test_bug_reports_require_core_sections(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)
            (folder / "BR-999-sample.md").write_text(
                "**ID:** BR-999-sample\n**Estado:** Pending\n",
                encoding="utf-8",
            )
            with patch.object(validate_artifacts, "BUG_REPORTS_DIR", folder):
                errors = validate_artifacts.validate_bug_reports()

        self.assertTrue(any("missing section" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
