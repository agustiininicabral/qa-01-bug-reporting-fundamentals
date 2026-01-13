# Bug Report

**Título:** Carrito se vacía al refrescar página en ciertos escenarios  
**ID:** BR-002-cart-persistence

## Ambiente
- OS: Windows 11
- Navegador/App: Chrome (última)
- URL / Build / Versión: Sitio demo

## Precondiciones
- Usuario con carrito con al menos 1 ítem (si aplica)

## Pasos para reproducir
1. Ir a checkout / formulario de compra
2. Borrar campos obligatorios (Nombre, Dirección, etc.)
3. Enviar formulario

## Resultado actual
- El sistema permite continuar / no muestra validación consistente.

## Resultado esperado
- Bloquear envío y mostrar validaciones por campo con mensajes claros.

## Severidad
- Media

## Prioridad
- P1

## Frecuencia
- Siempre

## Evidencia
- Captura sugerida: `04-evidence/screenshots/BR-002-cart-persistence.png`

## Notas
- Recomendar validaciones client-side + server-side.
