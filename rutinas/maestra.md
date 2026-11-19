# Rutina maestra

De lunes a viernes a las 8:00, solo en la cuenta de Hugo y en el entorno que tiene el secreto de Trello. Hace todo lo que se puede hacer sin publicar y deja el resultado en Trello, para que la [diaria](diaria.md) de cada uno lo lea a las 9:00.

Conectores: GitHub (este repo y `bootcamp_AI_Engineering_10_26`, solo lectura), Google Calendar y Trello. En Trello lee con el conector o con la API REST, pero **todo lo que escribe lo hace con la API REST** (apartado «Cómo escribe en Trello»).

Es la única rutina que escribe en Trello. La decisión de Hugo, del 17/11/2026, es que crea tarjetas y comenta en ellas sin pedir OK. **Nunca mueve, archiva, borra ni marca como hecha una tarjeta, y nunca publica nada.** La única excepción es la limpieza de Done del apartado 3, que solo archiva tras un comentario «OK» de Hugo.

## Cómo escribe en Trello

Esta rutina corre sin nadie delante. Las herramientas de escritura del conector de Trello piden permiso y se quedan esperando, así que no se usan. Se escribe con `curl` a `https://api.trello.com/1/`: el entorno añade las credenciales, así que no se pone ninguna clave ni token en la URL. Si una llamada falla, no se reintenta con el conector: se anota en el registro y se sigue.

Tablero `iYb6W4J7`. Lista «Current Sprint»: `6ac788da4495c71e9e810cda`.

| Qué | Llamada |
| --- | --- |
| Buscar tarjetas, también archivadas | `GET /1/boards/iYb6W4J7/cards/all?fields=name,closed,idList,due` |
| Crear una tarjeta | `POST /1/cards` con `idList`, `name`, `desc`, `due` (UTC, ISO 8601) e `idMembers` (la persona asignada) |
| Comentar | `POST /1/cards/{id}/actions/comments` con `text` |
| Archivar (solo limpieza de Done con OK) | `PUT /1/cards/{id}` con `closed=true` |
| Marcar como hecha (solo limpieza de Done con OK) | `PUT /1/cards/{id}` con `dueComplete=true` |

Los parámetros van con `--data-urlencode`, para que los acentos y los saltos de línea de `name`, `desc` y `text` lleguen bien.

## 1. Situarse

Igual que el apartado 1 de [diaria.md](diaria.md): fecha, sprint N de esta semana, quién es LI y quién es TA, y quién imparte N+1. Si esta semana no hay sprint (Project Break o vacaciones), no crea nada y lo dice en el registro.

## 2. Tarjetas de la semana

Cada día comprueba que existen las tarjetas de la semana y crea las que falten. El jueves, primer día de la semana, las crea todas; el resto de días solo repone las que falten.

Todas van en la lista «Current Sprint» del tablero `iYb6W4J7`. El nombre empieza siempre por `[OCT26 S{NN}]`, para poder buscarlas. Las horas están en Europe/Madrid y se convierten a UTC al guardarlas.

| Tarjeta | Para | Vence |
| --- | --- | --- |
| `[OCT26 S{N}] Liberar el sprint y mensaje de apertura` | TA | Jueves, 9:00 |
| `[OCT26 S{N}] Caso práctico` | LI | Lunes, 19:00 |
| `[OCT26 S{N}] PDF de enlaces para profundizar` | LI | Martes, 19:00 |
| `[OCT26 S{N}] Mensaje de cierre de semana` | TA | Viernes, 14:00 |
| `[OCT26 S{N+1}] Revisar el sprint y aplicar correcciones` | Quien imparte N+1 | Martes, 19:00 |
| `[OCT26 S{N+1}] Revisar Deck` | TA | Viernes, 12:00 |
| `[OCT26 S{N+1}] Sección del campus preparada y oculta` | TA | Miércoles, 19:00 |
| `[OCT26 S{N+1}] Copia al repo de alumnos` | TA | Miércoles, 21:00 |
| `[OCT26 S{N+1}] Preparar la teórica` | Quien imparte N+1 | Miércoles, 19:00 |

Si esta semana hay enunciado, entrega o presentación de un TC o un PB según el calendario, añade una tarjeta para cada uno, para el TA y con la fecha del calendario.

La descripción de cada tarjeta lleva en dos o tres líneas qué hay que hacer, el enlace a la skill o plantilla que toca y el rol.

**Sin duplicados.** Antes de crear una tarjeta, busca en el tablero, abiertas y archivadas, una con el mismo nombre. Si existe, no la crea.

**Asignar.** Asigna cada tarjeta a quien tiene ese rol esta semana al crearla, con `idMembers`. Los ids de miembro están en `docs/mapa-recursos.md`. Si la API falla, deja la tarjeta sin asignar y lo anota en el registro.

## 3. Limpieza de Done

Los jueves cuenta las tarjetas de la lista «Done 🎉» que siguen sin archivar y llevan más de 14 días sin movimiento.

- Si hay alguna, crea la tarjeta `[Trello] ¿Archivar N tarjetas de Done? · semana del {dd/mm}` en «Current Sprint». La asigna a Hugo y vence el viernes a las 14:00. En la descripción van la lista de tarjetas, con su nombre y su enlace, y la pregunta: «Comenta OK en esta tarjeta para archivarlas todas, o OK menos los números que quieras conservar».
- Cada día mira si esa tarjeta tiene un comentario de Hugo con «OK». Si lo tiene, archiva las tarjetas de la lista menos las que el comentario excluya, deja un comentario con lo que ha archivado y marca la tarjeta como hecha. El comentario de Hugo es su OK; sin él no archiva nada.
- Si la tarjeta de la semana anterior sigue sin OK, no crea otra: actualiza la lista y el número en la que ya existe.

## 4. Trabajo que hace sola

Cada resultado va como comentario en su tarjeta. El comentario empieza por `Rutina maestra · {fecha}`. Si ese día ya hay uno, no repite.

| Día | Qué hace | Tarjeta |
| --- | --- | --- |
| Miércoles y jueves | Mira en `bootcamp_AI_Engineering_10_26` las PRs abiertas de `feature/copy_from_material` a `develop` y de `develop` a `main`. Avisa de cuatro cosas: soluciones de N+1 (ficheros `*_SOLUTION*` o carpetas `SOLUTION/`), `README_profes.md`, duplicados « 2» y una PR a `main` que no venga de `develop`. El jueves, avisa también si a las 8:00 el sprint N no está en `develop` ni en una PR abierta a `main`, porque no podrá liberarse a primera hora | Copia al repo de alumnos |
| Jueves | Borrador del mensaje de apertura con `plantillas/mensajes/apertura-sprint.md`. Lo redacta desde el `README.md` del sprint N en material, porque a las 8:00 aún no está liberado. Los enlaces apuntan a la ruta que tendrá en `main` del repo de alumnos. En el comentario recuerda comprobarlos después de liberar | Liberar el sprint y mensaje de apertura |
| Viernes | Borrador del cierre de semana con `plantillas/mensajes/cierre-semana.md` | Mensaje de cierre de semana |

Los borradores siguen la skill `normas-aie`. No llevan datos de alumnos.

## 5. Registro

Al terminar, un resumen corto: tarjetas creadas con su persona y su fecha, las que ya existían, los comentarios dejados y lo que no se pudo hacer, con el motivo. Hugo solo necesita mirarlo si algo falló, porque la diaria ya avisa a cada uno.
