# 002 · Mapa de recursos y conectores

Estado: borrador del 17/11/2026, pendiente de aprobar.

## Qué

Que cualquiera de los dos, desde su Claude y con su propia cuenta, pueda leer Trello, Slack, Notion, Google Calendar y las hojas del curso. Y que el repo diga dónde está cada recurso, para que Claude no tenga que preguntarlo.

## Por qué

Las skills y los recordatorios necesitan datos: quién es LI esta semana, qué tarjetas hay, qué se dijo en Slack o qué alumnos van tarde. Hoy esos datos solo los ve el Claude de Hugo y los identificadores están repartidos por memorias de un proyecto personal.

## Alcance

Dentro:
- Completar `docs/mapa-recursos.md`: hoja de seguimiento de OCT26, canales de Slack (alumnos, equipo y el de los tres con Álex Cárabe), carpeta de actas en Drive, Deck y curso de OCT26 en el campus.
- Una tabla por herramienta con qué hay que conectar, dónde se conecta (app de chat o Claude Code) y si está comprobado.
- Declarar en el plugin los conectores que se puedan declarar, sin claves. El resto se documenta como paso manual.
- Una regla común: leer libremente; escribir en Trello, Notion, Slack o el calendario solo con el OK de una persona.

Fuera:
- Automatizar nada con esos datos (specs 003 y 004).
- Cambiar permisos o administradores en Trello, Slack o Notion.

## Criterios de aceptación

- Los dos, desde su Claude, responden a «¿qué tarjetas tengo esta semana en Trello?» y «¿qué clases hay el jueves?».
- `mapa-recursos.md` no tiene ningún «por completar».
- En el repo no hay ninguna clave ni token.

## Preguntas abiertas

- ¿Qué conectores se pueden declarar en un plugin de Claude Code y cuáles solo se activan desde la app? Sin comprobar.
- Trello: Alejandro Reyes es el único administrador del tablero. ¿Quién le releva?
