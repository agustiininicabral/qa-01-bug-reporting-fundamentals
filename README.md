# Bug Reporting Fundamentals

## Objetivo
Redactar reportes de bugs claros, reproducibles y accionables (estándar industria).

## Contexto
Proyecto de portfolio QA: se trabaja con un sitio demo (p. ej. Demoblaze, SauceDemo o The Internet) para producir artefactos estándar y evidencia.

## Alcance
- Pruebas funcionales (UI/API según repo)
- Documentación de evidencia
- Reporte final con hallazgos y recomendación

## Fuera de alcance
- Performance testing profundo
- Security pentesting
- Automatización (fuera de este paquete)

## Herramientas
- Jira (conceptual)
- Google Sheets/Excel (artefactos)
- Postman (conceptual)
- SQL (conceptual)
- Navegador Chrome/Firefox

## Entregables
- Casos de prueba (CSV)
- 3 a 8 Bug Reports (Markdown)
- Evidencias (carpeta)
- Reporte final (Markdown)

## Cómo reproducir
1) Leer `01-requirements/scope.md`.
2) Ejecutar los casos de prueba listados en `03-work/test-cases.csv`.
3) Registrar fallos en `03-work/bug-reports/` usando la plantilla.
4) Completar `05-results/report.md`.

## Evidencia
- Ver carpeta `04-evidence/` (capturas, exports, logs).

## Resultados
- Ver `05-results/report.md`.

## Próximos pasos
- Extender cobertura por riesgos
- Agregar automatización (Playwright/Cypress) en un repo dedicado
- Integrar CI (GitHub Actions) para smoke básico
