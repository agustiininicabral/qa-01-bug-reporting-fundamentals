# Bug Report — ejemplo pendiente de validación

**Título:** El carrito podría perder productos tras actualizar la página  
**ID:** BR-002-cart-persistence  
**Estado:** Pendiente de reproducción; no es un defecto confirmado.  
**Severidad propuesta:** Media  
**Prioridad propuesta:** P2

## Ambiente
- Sistema operativo: Windows 11 (ambiente propuesto)
- Navegador: Chrome (registrar versión durante la ejecución)
- URL: https://www.demoblaze.com/
- Build / versión: sitio público de demostración; versión no identificada

## Precondiciones
Agregar al menos un producto al carrito y anotar su nombre y precio.

## Pasos para reproducir
1. Abrir el carrito y registrar los productos presentes.
2. Actualizar la página del navegador.
3. Volver a abrir el carrito y comparar los productos.

## Resultado actual
Hipótesis a verificar: uno o más productos podrían desaparecer tras actualizar la página.

## Resultado esperado
El carrito debe conservar el estado definido por el comportamiento esperado del sitio; cualquier pérdida debe estar documentada y ser consistente.

## Frecuencia
Pendiente de medir mediante ejecuciones repetidas.

## Evidencia
- Ruta prevista: `04-evidence/screenshots/BR-002-cart-persistence.png`
- No se adjunta captura porque el caso aún no fue ejecutado y verificado.

## Criterio de cierre
Reproducir el caso en el sitio indicado, adjuntar evidencia, registrar fecha y versión del navegador, y actualizar el estado con el resultado observado. Si no se reproduce, cerrar como no reproducible o descartar la hipótesis.
