# Rutina diaria

De lunes a viernes a las 9:00, en la cuenta de cada uno. Da a la persona solo lo que le toca hoy según su rol.

Solo lee. Lo que se puede hacer sin publicar ya lo ha hecho la [rutina maestra](maestra.md) a las 8:00 y está en Trello: la diaria lo resume.

Conectores: GitHub (este repo y los del bootcamp, lectura), Google Calendar, Trello y Google Sheets. Trello y Sheets, solo para leer.

## 1. Situarse

1. Fecha de hoy en Europe/Madrid.
2. Lee `docs/li-por-modulo.md`, `docs/semana-tipo.md` y `docs/roles-y-funciones.md` de este repo, en `main`.
3. Saca N del calendario OCT26. Los banners de sprint van de jueves a miércoles, pero nuestra semana va de miércoles a martes. Por eso N no es el banner de hoy, sino el banner que contiene el jueves de esta semana: mañana si hoy es miércoles, o el jueves pasado en los demás días. Ejemplo: el miércoles 18/11/2026 el banner de hoy es S04, pero N es S05.
4. Averigua el rol de la persona esta semana (LI o TA) y si va a impartir N+1, porque las funciones que siguen al sprint se preparan una semana antes.
5. Si hoy no hay clases (festivo, vacaciones o Project Break), dilo en una línea y da solo lo de los apartados 3, 4 y 5.

## 2. Qué toca hoy

Saca de `semana-tipo.md` lo de hoy para el rol de la persona, con la hora. Añade lo que vence en los próximos dos días con su fecha, sobre todo lo que sigue al sprint.

Según el día, añade:

| Día | Qué añadir |
| --- | --- |
| Lunes | Alumnos sin actividad en 7 días o más, de la pestaña «Seguimientos» de la hoja de seguimiento, sin los que estén en «Seg. PAUSADO». Solo nombre y días. Y la lista de tarjetas abiertas para la weekly de las 16:00 |
| Martes | Al TA: la copia de N+1 al repo de alumnos durante la clase de las 19:00, con la skill `liberar-sprint`. A quien imparte N+1: la revisión vence hoy a las 19:00 |
| Miércoles | Al TA: liberar hacia las 13:00. Si la maestra ha dejado el borrador de apertura, el enlace a la tarjeta |
| Viernes | Al TA: el enlace a la tarjeta con el borrador del cierre de semana, para revisar y publicar |

## 3. PRs por revisar

Sigue [revision-prs.md](revision-prs.md) para la persona: las PRs a `main` que no ha abierto ella y esperan su revisión.

## 4. Tarjetas de Trello

Del tablero `iYb6W4J7`, las tarjetas pendientes asignadas a la persona. Pendiente quiere decir no archivada y fuera de las listas «Done 🎉» e «Info»:
- vencidas;
- que vencen hoy o en los próximos dos días;
- con un comentario de hoy de la rutina maestra (un borrador o un aviso), en una línea;
- sin fecha, solo el número y las tres más antiguas.

Si hoy es día de trabajo de la maestra y no hay ningún comentario suyo, dilo: puede haber fallado.

Propón archivar, sin archivar nada:
- si la persona es Hugo y la tarjeta `[Trello] ¿Archivar N tarjetas de Done?` de la maestra sigue sin su OK, una línea con el número y el enlace;
- las pendientes que parezcan caducadas: de MAY26, de sprints ya liberados o sin movimiento en 30 días. Para estas, el nombre y el motivo.

## 5. Recursos que ya existen

Para cada tarea de «Hoy», «Próximos dos días» y «Trello» que figure en esta tabla, añade al final de su línea el recurso, así: `→ skill preparar-sprint`.

| Tarea (n.º en `roles-y-funciones.md`) | Recurso | Para quién |
| --- | --- | --- |
| Revisar el sprint, preparar la teórica, el caso práctico o el PDF de enlaces (7, 8, 10, 11) | skill `preparar-sprint` | Quien imparte el sprint |
| Liberar el sprint, copia al repo de alumnos, campus (14, 15) | skill `liberar-sprint` | TA |
| Mensaje de apertura del sprint (16) | plantilla `plantillas/mensajes/apertura-sprint.md` | TA |
| Mensaje de cierre de semana (17) | plantilla `plantillas/mensajes/cierre-semana.md` | TA |
| Mensajes de aviso de clases, MC y talleres (18) | plantillas de `plantillas/mensajes/` | TA |
| Acta de una sesión (20) | skill `acta-sesion` | TA |
| Cualquier texto de cara al alumno | skill `normas-aie` | Los dos |
| Kahoot de una LR (9) | skill personal `kahoot` | Solo Hugo |
| Subir y comprobar una grabación (19) | skill personal `subir-video` | Solo Hugo |

- Solo ofrece lo que está en la tabla. Si una tarea no tiene recurso, no digas nada: no inventes skills.
- Las skills personales se ofrecen solo a su dueño. A la otra persona no se le nombran.
- Si un recurso no existe en el repo o en la cuenta de la persona, no lo ofrezcas y dilo en una línea al final.

## 6. Formato del aviso

- Título: `Diaria · {día} {fecha} · {LI | TA} · Sprint {N}`.
- Bloques, en este orden: «PRs por revisar» (solo si hay alguna), «Hoy», «Próximos dos días» y «Trello». Viñetas cortas, con hora y enlace, y el recurso del apartado 5 al final de la línea cuando lo haya.
- Que quepa en una pantalla de móvil. Si hay más, lo más urgente primero y el resto como «y N más».
- Nunca nombres ni datos personales de alumnos más allá del nombre y los días sin actividad.
