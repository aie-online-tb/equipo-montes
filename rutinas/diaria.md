# Rutina diaria

De lunes a viernes a las 9:00, en la cuenta de cada uno. Da a la persona solo lo que le toca hoy según su rol.

Conectores: GitHub (este repo), Google Calendar, Trello y Google Sheets.

## 1. Situarse

1. Fecha de hoy en Europe/Madrid.
2. Lee `docs/li-por-modulo.md`, `docs/semana-tipo.md` y `docs/roles-y-funciones.md` de este repo, en `main`.
3. Mira en el calendario OCT26 el banner de sprint de hoy. La semana va de miércoles a martes: N es el sprint que se liberó el miércoles de esta semana.
4. Averigua el rol de la persona esta semana (LI o TA) y si va a impartir N+1, porque las funciones que siguen al sprint se preparan una semana antes.
5. Si hoy no hay clases (festivo, vacaciones o Project Break), dilo en una línea y da solo lo de los apartados 3 y 4.

## 2. Qué toca hoy

Saca de `semana-tipo.md` lo de hoy para el rol de la persona, con la hora. Añade lo que vence en los próximos dos días con su fecha, sobre todo lo que sigue al sprint.

Según el día, añade:

| Día | Qué añadir |
| --- | --- |
| Lunes | Alumnos sin actividad en 7 días o más, de la pestaña «Seguimientos» de la hoja de seguimiento, sin los que estén en «Seg. PAUSADO». Solo nombre y días. Y la lista de tarjetas abiertas para la weekly de las 16:00 |
| Martes | Al TA: abrir la PR de release de N+1 durante la clase de las 19:00, con la skill `liberar-sprint`. A quien imparte N+1: la revisión vence hoy a las 19:00 |
| Miércoles | Al TA: comprobar la PR de release, mergearla y liberar hacia las 13:00. Después, el mensaje de apertura con `plantillas/mensajes/apertura-sprint.md` |
| Viernes | Al TA: borrador del cierre de semana con `plantillas/mensajes/cierre-semana.md`, para revisar y publicar |

## 3. Tarjetas de Trello

Del tablero `iYb6W4J7`, las tarjetas abiertas asignadas a la persona:
- vencidas;
- que vencen hoy o en los próximos dos días;
- sin fecha, solo el número y las tres más antiguas.

Propón archivar las que parezcan terminadas o caducadas (de MAY26, de sprints ya liberados o sin movimiento en 30 días), con el motivo. Solo proponer: no se archiva nada.

## 4. Formato del aviso

- Título: `Diaria · {día} {fecha} · {LI | TA} · Sprint {N}`.
- Tres bloques como mucho: «Hoy», «Próximos dos días» y «Trello». Viñetas cortas, con hora y enlace.
- Que quepa en una pantalla de móvil. Si hay más, lo más urgente primero y el resto como «y N más».
- Nunca nombres ni datos personales de alumnos más allá del nombre y los días sin actividad.
