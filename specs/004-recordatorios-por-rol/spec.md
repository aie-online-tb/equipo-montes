# 004 · Rutinas y automatizaciones

Estado: aprobada por Hugo el 17/11/2026. Ampliada el 17/11/2026: antes solo cubría recordatorios por rol.

## Qué

Todo lo que pasa solo, sin que nadie lo lance: recordatorios según el rol de cada semana, tarjetas de Trello de la semana tipo, comprobaciones de la release y borradores de mensajes. Más las guardas que impiden errores en los repos.

## Por qué

La semana tipo está escrita, pero los roles cambian con el módulo y las funciones que siguen al sprint se adelantan una semana. Es fácil equivocarse en los relevos. Sustituye a la tarea programada Diaria, que se abandonó.

## Mecanismos

| Mecanismo | Dónde corre | Para qué |
| --- | --- | --- |
| Rutinas (tareas programadas de Claude) | En la cuenta de cada uno | Recordatorios, comprobaciones, tarjetas de Trello y borradores |
| Skills | Cuando una persona las lanza | Trabajo con criterio: preparar, liberar y actas |
| Guardas | GitHub Actions y hooks del plugin | Que no se cuelen errores en los repos |
| Mac de Hugo | launchd, cada noche | Grabaciones y actas |

## Decisiones

- **Una rutina diaria igual para los dos.** Cada mañana averigua quién es LI esa semana y da a cada uno solo lo suyo. En un relevo no hay que tocar nada.
- **Una sola rutina de Trello, en la cuenta de Hugo.** Si la tuvieran los dos, saldrían tarjetas duplicadas. Además, asignar personas solo funciona con la API de Trello desde el entorno de Hugo.
- **La rutina de Trello crea tarjetas sola** (decisión de Hugo, 17/11/2026). Mover, archivar o borrar sigue necesitando el OK de una persona.
- **Ninguna rutina publica nada.** Avisan y dejan borradores; publicar es cosa de una persona.
- **Instrucciones en el repo, no en la rutina.** La rutina solo dice qué fichero de `rutinas/` seguir. Así se cambian por PR y no se pagan miles de caracteres en cada ejecución.

## Alcance

Dentro:
- `rutinas/diaria.md`: una por persona, de lunes a viernes a las 9:00.
- `rutinas/trello.md`: solo en la cuenta de Hugo, los miércoles a las 8:30.
- Guardas de `equipo-montes` y del plugin (hechas) y del repo de alumnos de OCT26 (pendientes del OK de Hugo).

Fuera:
- La automatización de grabaciones, que sigue en el Mac de Hugo.
- Publicar mensajes, mover o archivar tarjetas o cambiar el campus.

## Criterios de aceptación

- Durante dos semanas seguidas, una de ellas con relevo, ningún aviso ni ninguna tarjeta va a la persona equivocada.
- La rutina de Trello no crea duplicados aunque se ejecute dos veces la misma semana.
- Cada aviso diario cabe en una pantalla de móvil.
- Desactivar la rutina de uno no afecta a la del otro.

## Preguntas abiertas

- Dónde llegan los avisos. Se recomienda la notificación de la app de Claude.
- Si la cuenta Pro de Soraya admite tareas programadas.
- La Diaria antigua sigue activa y hay que desactivarla antes.
