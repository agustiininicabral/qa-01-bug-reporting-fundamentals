# Bug Report — ejemplo pendiente de validación

**Título:** El mensaje de validación podría no explicar cómo corregir el error  
**ID:** BR-003-ui-error-message  
**Estado:** Pendiente de reproducción; no es un defecto confirmado.  
**Severidad propuesta:** Baja  
**Prioridad propuesta:** P3

## Ambiente
- Sistema operativo: Windows 11 (ambiente propuesto)
- Navegador: Chrome (registrar versión durante la ejecución)
- URL: https://www.demoblaze.com/
- Build / versión: sitio público de demostración; versión no identificada

## Precondiciones
Tener disponible un formulario que permita provocar una validación de datos.

## Pasos para reproducir
1. Abrir el formulario de compra.
2. Introducir datos inválidos o dejar un campo requerido vacío.
3. Enviar el formulario y leer el mensaje de respuesta.

## Resultado actual
Hipótesis a verificar: el mensaje podría ser genérico y no identificar el campo o la acción correctiva.

## Resultado esperado
El mensaje debe describir el problema de forma comprensible y orientar al usuario para corregirlo sin revelar información sensible.

## Frecuencia
Pendiente de medir mediante ejecuciones repetidas.

## Evidencia
- Ruta prevista: `04-evidence/screenshots/BR-003-ui-error-message.png`
- No se adjunta captura porque el caso aún no fue ejecutado y verificado.

## Criterio de cierre
Reproducir el caso en el sitio indicado, adjuntar evidencia, registrar fecha y versión del navegador, y actualizar el estado con el resultado observado. Si no se reproduce, cerrar como no reproducible o descartar la hipótesis.
