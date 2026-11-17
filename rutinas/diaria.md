# Rutina diaria

De lunes a viernes a las 9:00, en la cuenta de cada uno. Da a la persona solo lo que le toca hoy según su rol.

Es el **único aviso diario**: la persona no recibe nada más por la mañana. Llega siempre al mismo hilo, «Avisos». Por eso no repite ni resume los avisos de días anteriores: cada día es independiente y empieza leyendo de nuevo los ficheros de `main`.

Solo lee. Lo que se puede hacer sin publicar ya lo ha hecho la [rutina maestra](maestra.md) a las 8:00 y está en Trello: la diaria lo resume. La maestra no avisa por su cuenta: si falla, lo dice esta rutina.

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

## 5. Skills y recursos que ya existen

Mira las tareas de «Hoy» y «Vence pronto» y busca cada una en esta tabla. Los recursos que salgan, sin repetir, van todos juntos en la **última línea** del mensaje (apartado 6), no al lado de cada tarea.

| Tarea (n.º en `roles-y-funciones.md`) | Recurso | Para quién |
| --- | --- | --- |
| Revisar el sprint, preparar la teórica, el caso práctico o el PDF de enlaces (7, 8, 10, 11) | `preparar-sprint` | Quien imparte el sprint |
| Liberar el sprint, copia al repo de alumnos, campus (14, 15) | `liberar-sprint` | TA |
| Mensaje de apertura del sprint (16) | plantilla `apertura-sprint` (`plantillas/mensajes/`) | TA |
| Mensaje de cierre de semana (17) | plantilla `cierre-semana` (`plantillas/mensajes/`) | TA |
| Mensajes de aviso de clases, MC y talleres (18) | plantillas de `plantillas/mensajes/` | TA |
| Acta de una sesión (20) | `acta-sesion` | TA |
| Cualquier texto de cara al alumno | `normas-aie` | Los dos |
| Kahoot de una LR (9) | `kahoot` (skill personal) | Solo Hugo |
| Subir y comprobar una grabación (19) | `subir-video` (skill personal) | Solo Hugo |

- Solo ofrece lo que está en la tabla. Si una tarea no tiene recurso, no digas nada: no inventes skills.
- Las skills personales se ofrecen solo a su dueño. A la otra persona no se le nombran.
- Si un recurso no existe en el repo o en la cuenta de la persona, no lo ofrezcas.

## 6. Formato del aviso

Un solo mensaje que se lea de un vistazo en el móvil: **12 líneas como máximo**, sin contar el título ni la última línea. Lo demás, como «y N más», con el enlace al tablero.

- Título: `Diaria · {día} {fecha} · {LI | TA} · Sprint {N}`.
- Tres bloques, en este orden:
  1. **Hoy**: las clases y tareas del día con su hora. Aquí va también lo del lunes.
  2. **Vence pronto**: tarjetas vencidas o que vencen en los próximos dos días, con fecha y enlace. Si hay tarjetas sin fecha, una sola línea con el número.
  3. **Decide tú**: lo que espera una decisión de la persona. Las PRs por revisar, la tarjeta de archivar Done sin OK, las propuestas de archivar tarjetas caducadas y los avisos de la maestra (un fallo o un comentario de aviso). Si no hay nada, el bloque no sale.
- Viñetas de una línea, con hora y enlace.
- Si la maestra no ha dejado su comentario un día de trabajo, es la primera línea de «Decide tú».
- **Última línea, sola:** `Skills recomendadas: preparar-sprint, kahoot`, con los recursos del apartado 5 que correspondan a lo de hoy, máximo cuatro. Si no hay ninguno, la línea no sale.
- Nunca nombres ni datos personales de alumnos más allá del nombre y los días sin actividad.
