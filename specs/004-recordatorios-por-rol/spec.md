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

- **Una rutina maestra que escribe y una diaria por persona que lee** (decisión de Hugo, 17/11/2026). La maestra, a las 8:00 en la cuenta de Hugo, hace todo lo que se puede hacer sin publicar y lo deja en Trello. La diaria de cada uno, a las 9:00, solo lo resume.
- **Solo la maestra escribe en Trello.** Si escribieran las dos cuentas, saldrían tarjetas duplicadas. Además, asignar personas solo funciona con la API de Trello desde el entorno de Hugo. La cuenta de Soraya puede escribir en Trello con el conector; lo que lo impide en sus rutinas es esta regla, no un permiso.
- **La maestra crea tarjetas y comenta sin pedir OK** (decisión de Hugo, 17/11/2026). Mover, archivar, borrar o marcar como hecha sigue necesitando el OK de una persona.
- **La diaria calcula el rol cada mañana.** En un relevo no hay que tocar nada.
- **Aviso de PRs a `main` pendientes de revisar** (Hugo, 17/11/2026): en la diaria y en una rutina a las 12:00 y a las 17:00, aunque llegue el correo de GitHub. Cuenta toda PR a `main` que no haya abierto la persona. Ver `rutinas/revision-prs.md`.
- **Los datos de alumnos no van a Trello.** La diaria los lee directamente de la hoja de seguimiento.
- **Ninguna rutina publica nada.** Avisan y dejan borradores; publicar es cosa de una persona.
- **Instrucciones en el repo, no en la rutina.** La rutina solo dice qué fichero de `rutinas/` seguir. Así se cambian por PR y no se pagan miles de caracteres en cada ejecución.

## Alcance

Dentro:
- `rutinas/maestra.md`: solo en la cuenta de Hugo, de lunes a viernes a las 8:00.
- `rutinas/diaria.md`: una por persona, de lunes a viernes a las 9:00.
- Guardas de `equipo-montes` y del plugin (hechas) y del repo de alumnos de OCT26 (pendientes del OK de Hugo).

Fuera:
- La automatización de grabaciones, que sigue en el Mac de Hugo.
- Publicar mensajes, mover o archivar tarjetas o cambiar el campus.

## Criterios de aceptación

- Durante dos semanas seguidas, una de ellas con relevo, ningún aviso ni ninguna tarjeta va a la persona equivocada.
- La maestra no crea duplicados aunque se ejecute varias veces la misma semana.
- Los borradores de apertura y de cierre están en su tarjeta antes de las 9:00 del día que tocan.
- Cada aviso diario cabe en una pantalla de móvil.
- Desactivar la rutina de uno no afecta a la del otro.

## Preguntas abiertas

- Dónde llegan los avisos. Se recomienda la notificación de la app de Claude.
- Si la cuenta Pro de Soraya admite tareas programadas.
- La Diaria antigua sigue activa y hay que desactivarla antes.
