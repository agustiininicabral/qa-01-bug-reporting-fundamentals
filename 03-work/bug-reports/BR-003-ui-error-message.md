# Bug Report

**Título:** Mensaje de error no describe causa ni cómo corregir  
**ID:** BR-003-ui-error-message

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
- Baja

## Prioridad
- P3

## Frecuencia
- Siempre

## Evidencia
- Captura sugerida: `04-evidence/screenshots/BR-003-ui-error-message.png`

## Notas
- Recomendar validaciones client-side + server-side.
