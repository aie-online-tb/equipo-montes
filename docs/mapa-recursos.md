# Mapa de recursos

Dónde está cada cosa. Aquí van identificadores y enlaces, nunca claves ni tokens. Cada uno se conecta con su propia cuenta.

## Tareas y base compartida

| Recurso | Identificador | Notas |
| --- | --- | --- |
| Trello, tablero «AI Engineering» | https://trello.com/b/iYb6W4J7/ai-engineering | Fuente de verdad de las tareas. Listas: Info, Brainstorming, Backlog, Sprint Planning, Current Sprint, In progress, Done, blocked |
| Notion, espacio «The Bridge AIE» | https://app.notion.com/p/3e948b5deb6b81fe9e6ed4bd58c62195 | Base compartida: actas, alumnos, calendario, fechas de entrega |

Cuentas de Trello: Hugo es `hugomm_thebridge` (id de miembro `6a564e823f39b80b55665d98`). La cuenta que usa Soraya es `sorayamalpicamontes1` (id de miembro `6a9588ebd27c3031097fa9d1`); existe otra duplicada, `sorayamalpicamontes`, sin uso desde julio de 2026 y pendiente de quitar.

## Calendario

| Recurso | Identificador |
| --- | --- |
| Google Calendar OCT26 | `c_6ba5d10bc3fc1860ca7ea24e058066601c1efa069ec6d17e7b7d79a092c65a3c@group.calendar.google.com` |
| Hoja «Calendario_AIE_OCT26_v2» | Google Sheets, id `171PvaxuEHjkCYW2lRkVZEZaLccQU9av_yj_HZi-WkYw` |

Los banners de sprint del calendario llevan el nombre del LI.

## Seguimiento de alumnos

| Recurso | Identificador | Notas |
| --- | --- | --- |
| Hoja «Informe de seguimientos IAE-ON-Octubre26» | Google Sheets, id `1DlOrdNId5yf-t-HgOMdimcjv_nBGM_NfuqnZeM7ECLk` | Pestañas clave: «Seguimientos» (columna «Seguimiento docente»), «Calificaciones AIE-26», «TC - GRUPOS», «PB1», «PB2», «Git de estudiantes» y «Evolución Alumnos» |

Tiene datos personales de alumnos: se consulta, pero nunca se copia al repo.

## Slack

| Espacio | Canal | Notas |
| --- | --- | --- |
| The Bridge (equipo) | `#equipo-octubre-2026` | Público, equipo del intake |
| The Bridge (equipo) | `#equipo_docente_octubre-2026` | Privado, equipo docente |
| The Bridge Online (alumnos) | `ia_engineering_online_oct_26` | Privado, canal de alumnos de OCT26 |
| The Bridge Online (alumnos) | `oct26-claustro-aie` | Privado, claustro de OCT26. Es también el canal de coordinación con Álex Cárabe |
| The Bridge Online (alumnos) | `claustro_bootcamp_aie_septiembre_26` | Privado, claustro |
| The Bridge Online (alumnos) | `bootcamp_ia-engineering-may26` | Privado, alumnos de MAY26, fuera del alcance de este repo |

Cada uno conecta un solo espacio de Slack a su Claude. El de alumnos no es visible para Claude: los canales de arriba los pasó Hugo el 17/11/2026.

## Repos (organización `aie-online-tb`)

| Repo | Para qué |
| --- | --- |
| `equipo-montes` | Este repo: organización y herramientas |
| `material_bootcamp_AI_Engineering` | Material fuente, privado |
| `bootcamp_AI_Engineering_10_26` | Repo de alumnos de OCT26 |
| `workouts_AIE_permanente` | Workouts enlazados desde el campus |

Usuarios de GitHub: Hugo es `hug4470` y Soraya es `somm14`. Las PRs que abre Claude desde la cuenta de alguien salen con su usuario.

## Clases y grabaciones

| Recurso | Notas |
| --- | --- |
| Zoom, YouTube y campus | Cuenta compartida TA IA ONLINE, que es la de MAY26. La cuenta de Google de OCT26 está pendiente de conectar |
| YouTube | Lista «Grabaciones AI Engineering 10-26», vídeos en Oculto |
| Automatización de grabaciones | Corre en el equipo de Hugo; el TA de la semana comprueba el resultado |

## Conectores

Cada uno activa los conectores en su cuenta de claude.ai (Ajustes → Conectores), con su propio usuario. Así funcionan en la app de chat y en Claude Code a la vez: Claude Code usa los conectores de la cuenta con la que se ha iniciado sesión. El plugin no declara ningún conector por ahora, para no duplicarlos ni meter direcciones sin comprobar.

| Herramienta | Conector | Para qué lo usa Claude | Hugo | Soraya |
| --- | --- | --- | --- | --- |
| Trello | Trello | Leer el tablero y las tarjetas de cada uno | Conectado | Por comprobar |
| Notion | Notion | Actas, alumnos, calendario y fechas de entrega | Conectado | Por comprobar |
| Slack | Slack | Leer canales y preparar borradores de mensajes | Conectado al espacio de equipo | Por comprobar |
| Google Calendar | Google Calendar | Clases, banners de sprint y quién es LI | Conectado | Por comprobar |
| Google Sheets y Drive | Google Drive y Google Sheets | Hoja de seguimiento y calendario del curso | Conectado | Por comprobar |
| GitHub | GitHub | Repos del bootcamp y este repo | Conectado | Por comprobar |
| Zoom | Zoom | Grabaciones y transcripciones | Conectado | Opcional |

Reglas:
- Leer, libre. Escribir en Trello, Notion, Slack o el calendario, solo con el OK de una persona.
- Slack solo admite un espacio por cuenta. Cada uno decide cuál conecta: el de equipo (The Bridge) o el de alumnos (The Bridge Online), donde están el canal de alumnos y `oct26-claustro-aie`.
- Los conectores dependen de la cuenta, no del repo: si uno cambia, se apunta aquí.

## Por completar

- Cuenta de Google de OCT26 (Zoom, YouTube y campus), que necesita la automatización de grabaciones.
- Carpeta de Drive de actas.
- Deck, la plataforma de ejercicios online.
- Curso de OCT26 en el campus.
