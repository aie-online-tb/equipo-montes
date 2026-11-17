# Rutina de Trello

Miércoles a las 8:30, solo en la cuenta de Hugo. Crea en Trello las tarjetas de la semana tipo que empieza ese día.

Conectores: GitHub (este repo), Google Calendar y Trello. Para asignar personas, la API REST de Trello con el secreto del entorno de Hugo.

Decisión de Hugo (17/11/2026): esta rutina crea tarjetas sin pedir OK. **Nunca mueve, archiva ni borra.**

## 1. Situarse

Igual que el apartado 1 de [diaria.md](diaria.md): sprint N que se libera hoy, quién es LI y TA esta semana y quién imparte N+1. Si esta semana no hay sprint (Project Break o vacaciones), no crea nada y lo dice.

## 2. Tarjetas que crea

Todas en la lista «Current Sprint» del tablero `iYb6W4J7`. El nombre empieza siempre por `[OCT26 S{NN}]`, para poder buscarlas. Horas en Europe/Madrid, convertidas a UTC al guardarlas.

| Tarjeta | Para | Vence |
| --- | --- | --- |
| `[OCT26 S{N}] Liberar el sprint y mensaje de apertura` | TA | Miércoles de hoy, 13:00 |
| `[OCT26 S{N}] Caso práctico` | LI | Lunes, 19:00 |
| `[OCT26 S{N}] PDF de enlaces para profundizar` | LI | Martes, 19:00 |
| `[OCT26 S{N}] Mensaje de cierre de semana` | TA | Viernes, 14:00 |
| `[OCT26 S{N+1}] Revisar el sprint y aplicar correcciones` | Quien imparte N+1 | Martes, 19:00 |
| `[OCT26 S{N+1}] Revisar Deck` | TA | Martes, 19:00 |
| `[OCT26 S{N+1}] Sección del campus preparada y oculta` | TA | Martes, 19:00 |
| `[OCT26 S{N+1}] PR de release` | TA | Martes, 21:00 |
| `[OCT26 S{N+1}] Preparar la teórica` | Quien imparte N+1 | Miércoles siguiente, 19:00 |

Si esta semana hay enunciado, entrega o presentación de un TC o un PB según el calendario, añade una tarjeta para cada uno, para el TA y con la fecha del calendario.

La descripción de cada tarjeta lleva en dos o tres líneas qué hay que hacer, el enlace a la skill o plantilla que toca y el rol.

## 3. Sin duplicados

Antes de crear una tarjeta, busca en el tablero (abiertas y archivadas) una con el mismo nombre. Si existe, no la crea.

## 4. Asignar

Asigna cada tarjeta a la persona que tiene ese rol esta semana, con la API REST: `POST /1/cards/{id}/idMembers?value={idMiembro}`. Los ids de miembro están en `docs/mapa-recursos.md`. Si la API no responde, deja la tarjeta sin asignar y dilo en el aviso.

## 5. Aviso

Lista de tarjetas creadas, con su persona y su fecha, y de las que ya existían. Si algo no se pudo hacer, el motivo.
