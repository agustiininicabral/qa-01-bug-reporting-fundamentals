# Bug Report — ejemplo pendiente de validación

**Título:** Checkout no comunica claramente los campos obligatorios  
**ID:** BR-001-checkout-validation  
**Estado:** Pendiente de reproducción; no es un defecto confirmado.  
**Severidad propuesta:** Alta  
**Prioridad propuesta:** P1

## Ambiente
- Sistema operativo: Windows 11 (ambiente propuesto)
- Navegador: Chrome (registrar versión durante la ejecución)
- URL: https://www.demoblaze.com/
- Build / versión: sitio público de demostración; versión no identificada

## Precondiciones
- El sitio de demostración está disponible y hay al menos un producto en el carrito.

## Pasos para reproducir
1. Abrir el carrito y seleccionar Place Order.
2. Dejar vacíos los campos del formulario de compra.
3. Intentar confirmar la compra.

## Resultado actual
Hipótesis a verificar: el formulario podría no identificar de forma clara todos los campos obligatorios.

## Resultado esperado
La compra no debe completarse con datos obligatorios ausentes; el formulario debe indicar qué falta y conservar los datos válidos ya ingresados.

## Frecuencia
Pendiente de medir mediante ejecuciones repetidas.

## Evidencia
- Ruta prevista: `04-evidence/screenshots/BR-001-checkout-validation.png`
- No se adjunta captura porque el caso aún no fue ejecutado y verificado.

## Criterio de cierre
Reproducir el caso en el sitio indicado, adjuntar evidencia, registrar fecha y versión del navegador, y actualizar el estado con el resultado observado. Si no se reproduce, cerrar como no reproducible o descartar la hipótesis.
