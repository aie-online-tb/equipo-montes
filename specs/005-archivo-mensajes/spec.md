# 005 · Archivo de mensajes de Slack

Estado: borrador del 17/11/2026, pendiente de aprobar.

## Qué

Un archivo con una plantilla por tipo de mensaje que mandamos a los alumnos, con ejemplos reales de cada una:

- Aviso de clase: teórica, dudas, práctica, taller, Microcredencial UAM y masterclass externa.
- Apertura de sprint.
- Cierre de semana.
- Enunciado, recordatorio de entrega y presentación de TC y PB.

## Por qué

Los mensajes son del TA y el TA cambia con el módulo. Sin un archivo común, cada relevo cambia el tono y el formato, y se pierden cosas que ya funcionaban, como el orden por prioridad del mensaje de cierre.

## Alcance

Dentro:
- Plantillas en `plantillas/mensajes/`, una por tipo, con los huecos marcados y un ejemplo real.
- Punto de partida: los mensajes de MAY26 que ya existen (aperturas, cierres y avisos de S14 a S16).
- Qué datos necesita cada plantilla y de dónde salen (calendario, campus o repo).

Fuera:
- Enviar mensajes. Los publica siempre una persona.
- Mensajes al claustro.

## Criterios de aceptación

- Cada tipo de mensaje de la lista tiene plantilla y ejemplo.
- El TA de una semana real ha escrito todos los avisos de esa semana con las plantillas.
- Las plantillas siguen la skill `normas-aie`.
