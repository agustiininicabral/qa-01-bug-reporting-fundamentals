# Bug Reporting Fundamentals

Portfolio de QA Manual centrado en diseñar casos de prueba claros, documentar defectos reproducibles y mantener resultados verificables.

## Objetivo y alcance

- 15 casos funcionales para un flujo de compra de demostración.
- 3 ejemplos de bug reports con severidad, prioridad, pasos, resultado esperado y criterio de cierre.
- Plantillas reutilizables de casos y defectos.
- Validación automática de la estructura de los artefactos mediante Python y GitHub Actions.

**Transparencia de resultados:** los casos de prueba todavía no fueron ejecutados. Los tres bug reports son hipótesis de práctica pendientes de reproducción, no defectos confirmados del sitio público. El reporte de resultados no afirma PASS/FAIL ni Go/No-Go sin evidencia.

## Sistema bajo prueba propuesto

- Sitio de demostración: https://www.demoblaze.com/
- Navegador sugerido: Chrome estable.
- Antes de ejecutar, registrar fecha, versión del navegador, pasos realizados, resultado observado y evidencia. El sitio público puede cambiar sin aviso.

Los casos describen el comportamiento esperado que se desea verificar; no presuponen que el sistema tenga un defecto.

## Estructura

- `01-requirements/`: alcance e historias de usuario.
- `03-work/test-cases.csv`: 15 casos con prioridad, precondiciones, pasos y resultado esperado.
- `03-work/bug-reports/`: ejemplos de informes pendientes de reproducción.
- `templates/`: plantillas para nuevos casos y bug reports.
- `05-results/report.md`: estado de ejecución y limitaciones actuales.
- `scripts/validate_artifacts.py`: controles de integridad de los artefactos.
- `tests/`: pruebas automáticas del validador.
- `04-evidence/`: carpeta prevista para capturas, logs y otros respaldos reales.

## Cómo trabajar con el proyecto

1. Leer `01-requirements/scope.md` y `01-requirements/user-stories.md`.
2. Ejecutar los casos en el sitio propuesto y actualizar la columna `status` en el CSV.
3. Registrar solamente defectos que se hayan reproducido. Adjuntar evidencia y registrar el ambiente.
4. Actualizar `05-results/report.md` con conteos reales y una recomendación respaldada.
5. Ejecutar la validación estática antes de enviar cambios.

## Validación automática

Requiere Python 3.12 o posterior; no necesita dependencias externas:

```powershell
python scripts/validate_artifacts.py
python -m unittest discover -s tests -v
```

GitHub Actions ejecuta ambos comandos en pushes y pull requests. Estos controles verifican la integridad de la documentación y los CSV; no ejecutan el sitio web ni reemplazan las pruebas manuales.

## Fuera de alcance

- No se ejecutan compras reales ni se usan datos personales.
- No se afirma que el sitio público tenga los defectos descritos hasta que haya evidencia.
- Performance testing, pentesting y automatización de UI pertenecen a proyectos separados.

## Licencia

MIT. Consultá [LICENSE](LICENSE).
