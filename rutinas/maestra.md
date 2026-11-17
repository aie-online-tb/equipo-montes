# Rutina maestra

De lunes a viernes a las 8:00, solo en la cuenta de Hugo y en el entorno que tiene el secreto de Trello. Hace todo lo que se puede hacer sin publicar y deja el resultado en Trello, para que la [diaria](diaria.md) de cada uno lo lea a las 9:00.

Conectores: GitHub (este repo y `bootcamp_AI_Engineering_10_26`, solo lectura), Google Calendar y Trello. Para asignar personas, la API REST de Trello.

Es la única rutina que escribe en Trello. La decisión de Hugo, del 17/11/2026, es que crea tarjetas y comenta en ellas sin pedir OK. **Nunca mueve, archiva, borra ni marca como hecha una tarjeta, y nunca publica nada.** La única excepción es la limpieza de Done del apartado 3, que solo archiva tras un comentario «OK» de Hugo.

## 1. Situarse

Igual que el apartado 1 de [diaria.md](diaria.md): fecha, sprint N de esta semana, quién es LI y quién es TA, y quién imparte N+1. Si esta semana no hay sprint (Project Break o vacaciones), no crea nada y lo dice en el registro.

## 2. Tarjetas de la semana

Cada día comprueba que existen las tarjetas de la semana y crea las que falten. El miércoles las crea todas; el resto de días solo repone las que falten.

Todas van en la lista «Current Sprint» del tablero `iYb6W4J7`. El nombre empieza siempre por `[OCT26 S{NN}]`, para poder buscarlas. Las horas están en Europe/Madrid y se convierten a UTC al guardarlas.

| Tarjeta | Para | Vence |
| --- | --- | --- |
| `[OCT26 S{N}] Liberar el sprint y mensaje de apertura` | TA | Miércoles, 13:00 |
| `[OCT26 S{N}] Caso práctico` | LI | Lunes, 19:00 |
| `[OCT26 S{N}] PDF de enlaces para profundizar` | LI | Martes, 19:00 |
| `[OCT26 S{N}] Mensaje de cierre de semana` | TA | Viernes, 14:00 |
| `[OCT26 S{N+1}] Revisar el sprint y aplicar correcciones` | Quien imparte N+1 | Martes, 19:00 |
| `[OCT26 S{N+1}] Revisar Deck` | TA | Martes, 19:00 |
| `[OCT26 S{N+1}] Sección del campus preparada y oculta` | TA | Martes, 19:00 |
| `[OCT26 S{N+1}] Copia al repo de alumnos` | TA | Martes, 21:00 |
| `[OCT26 S{N+1}] Preparar la teórica` | Quien imparte N+1 | Miércoles siguiente, 19:00 |

Si esta semana hay enunciado, entrega o presentación de un TC o un PB según el calendario, añade una tarjeta para cada uno, para el TA y con la fecha del calendario.

La descripción de cada tarjeta lleva en dos o tres líneas qué hay que hacer, el enlace a la skill o plantilla que toca y el rol.

**Sin duplicados.** Antes de crear una tarjeta, busca en el tablero, abiertas y archivadas, una con el mismo nombre. Si existe, no la crea.

**Asignar.** Asigna cada tarjeta a quien tiene ese rol esta semana, con la API REST: `POST /1/cards/{id}/idMembers?value={idMiembro}`. Los ids de miembro están en `docs/mapa-recursos.md`. Si la API falla, deja la tarjeta sin asignar y lo anota en el registro.

## 3. Limpieza de Done

Los miércoles cuenta las tarjetas de la lista «Done 🎉» que siguen sin archivar y llevan más de 14 días sin movimiento.

- Si hay alguna, crea la tarjeta `[Trello] ¿Archivar N tarjetas de Done? · semana del {dd/mm}` en «Current Sprint». La asigna a Hugo y vence el viernes a las 14:00. En la descripción van la lista de tarjetas, con su nombre y su enlace, y la pregunta: «Comenta OK en esta tarjeta para archivarlas todas, o OK menos los números que quieras conservar».
- Cada día mira si esa tarjeta tiene un comentario de Hugo con «OK». Si lo tiene, archiva las tarjetas de la lista menos las que el comentario excluya, deja un comentario con lo que ha archivado y marca la tarjeta como hecha. El comentario de Hugo es su OK; sin él no archiva nada.
- Si la tarjeta de la semana anterior sigue sin OK, no crea otra: actualiza la lista y el número en la que ya existe.

## 4. Trabajo que hace sola

Cada resultado va como comentario en su tarjeta. El comentario empieza por `Rutina maestra · {fecha}`. Si ese día ya hay uno, no repite.

| Día | Qué hace | Tarjeta |
| --- | --- | --- |
| Martes y miércoles | Mira en `bootcamp_AI_Engineering_10_26` las PRs abiertas de `feature/copy_from_material` a `develop` y de `develop` a `main`. Avisa de cuatro cosas: soluciones de N+1 (ficheros `*_SOLUTION*` o carpetas `SOLUTION/`), `README_profes.md`, duplicados « 2» y una PR a `main` que no venga de `develop`. El martes, avisa también si a las 8:00 el sprint N+1 aún no está en `feature/copy_from_material` ni en `develop` | Copia al repo de alumnos |
| Miércoles | Borrador del mensaje de apertura con `plantillas/mensajes/apertura-sprint.md`. Lo redacta desde el `README.md` del sprint N en material, porque a las 8:00 aún no está liberado. Los enlaces apuntan a la ruta que tendrá en `main` del repo de alumnos. En el comentario recuerda comprobarlos después de liberar | Liberar el sprint y mensaje de apertura |
| Viernes | Borrador del cierre de semana con `plantillas/mensajes/cierre-semana.md` | Mensaje de cierre de semana |

Los borradores siguen la skill `normas-aie`. No llevan datos de alumnos.

## 5. Registro

Al terminar, un resumen corto: tarjetas creadas con su persona y su fecha, las que ya existían, los comentarios dejados y lo que no se pudo hacer, con el motivo. Hugo solo necesita mirarlo si algo falló, porque la diaria ya avisa a cada uno.
