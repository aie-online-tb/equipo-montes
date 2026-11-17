# Guía de inicio

Para Soraya y Hugo. Se lee en 10 minutos. Explica qué es este repo, cómo nos organizamos y qué hay que hacer el primer día.

Estado: propuesta del 16/11/2026, aprobada por Hugo y pendiente de revisar con Soraya en la reunión del 17/11.

## 1. La idea en cinco líneas

- Desde el S05 de OCT26 llevamos los dos un único intake. MAY26 queda fuera de este sistema.
- Las funciones no son de Hugo o de Soraya: son del **LI** (quien imparte esa semana) o del **TA** (el otro). Los roles cambian con el módulo.
- Cada uno sigue con su Claude Pro personal. Lo que compartimos no es un chat, es **este repo**.
- Todo lo que deba durar se escribe aquí: quién hace qué, cuándo, con qué reglas y con qué herramientas.
- Lo que construyamos (skills, plantillas, rutinas) se diseña primero en una spec corta y entra por PR.

## 2. Cómo nos organizamos

### Roles

| Rol | Qué hace |
| --- | --- |
| LI | Imparte la LR teórica del jueves, la sesión de dudas del lunes y la LR práctica del martes |
| TA | Acompaña todas las clases y lleva la operación: liberar el sprint, campus, Deck, mensajes, grabaciones y actas |

Hay un matiz importante. Unas funciones **siguen a la semana** y otras **siguen al sprint**. Revisar y preparar un sprint es de quien lo va a impartir, aunque esa semana todavía sea TA. Y la sesión de dudas del lunes es del sprint anterior, así que tras un relevo la da quien impartió ese sprint.

El detalle de las 29 funciones está en [roles-y-funciones.md](roles-y-funciones.md).

### La semana, de miércoles a martes

| Día | Qué pasa |
| --- | --- |
| Miércoles | El TA libera el sprint hacia las 13:00 y publica el mensaje de apertura. A las 19:00 acompaña a Álex Cárabe |
| Jueves | LR teórica (LI). El TA acompaña |
| Viernes | El TA comprueba grabaciones y publica el mensaje de cierre de semana |
| Lunes | Weekly a las 16:00. Sesión de dudas del sprint anterior a las 19:00 |
| Martes | LR práctica (LI). Durante la clase, el TA abre la PR de release del sprint siguiente |

Los plazos de preparación están en [semana-tipo.md](semana-tipo.md).

### Quién es LI ahora

| Módulo | Sprints | LI |
| --- | --- | --- |
| M02 y M03 | S05, S06 y S07 | Hugo, desde el miércoles 18/11 |
| M04 RAG | S08, S09 y S10 | Soraya, desde el miércoles 09/12 |
| M05 Agents | S11, S12 y S13 | Hugo, desde el 03/02/2027 |
| M06 MLOps | S14, S15 y S16 | Sin asignar |

La fuente es el calendario OCT26 de Google. El detalle y los relevos están en [li-por-modulo.md](li-por-modulo.md).

### Tres capas

Personal (lo de cada uno), Equipo Montes (nosotros dos, este repo) y Claustro (con Sergio, Marisa, Álex Cárabe y el resto). Cada cosa vive en la capa más baja que la resuelve y sube cuando el otro la necesita.

## 3. Primer día: puesta en marcha

Necesitas tener acceso al repo en GitHub y Claude Code instalado.

1. Clona el repo junto a los demás repos del bootcamp:

```bash
git clone https://github.com/aie-online-tb/equipo-montes.git
```

2. Instala las skills comunes. Se hace una sola vez:

```bash
claude plugin marketplace add aie-online-tb/equipo-montes
claude plugin install aie-equipo@equipo-montes
```

3. Abre la carpeta con Claude Code y pregúntale algo para comprobar que lee el repo. Por ejemplo: «¿quién libera el sprint esta semana y cuándo?».

4. Lee la [constitución](../specs/000-constitucion/spec.md) y apunta lo que cambiarías.

Para actualizar las skills cuando haya una versión nueva en `main`:

```bash
claude plugin marketplace update equipo-montes
claude plugin update aie-equipo@equipo-montes
```

Aviso: el plugin se instala en Claude Code. Si se puede usar tal cual desde la app de chat con el plan Pro está sin comprobar.

## 4. Cómo se trabaja en el repo

1. Parte de `develop` y crea una rama corta con tu prefijo: `soraya/003-skill-preparar-sprint`.
2. Haz commits pequeños y abre PR a `develop`. Esa PR puedes mergearla tú.
3. Cuando `develop` tenga algo que los dos debamos usar, se abre PR de `develop` a `main` y se pide revisión en GitHub a la otra persona.
4. Si falta menos de una hora para que el cambio haga falta, se puede mergear a `main` sin esperar, dejando un comentario con el motivo.

Claude puede hacer commit, push y abrir PR en tu rama. Nunca mergea a `main`.

Las reglas completas están en [reglas-git.md](reglas-git.md).

## 5. Cómo se propone algo nuevo

1. **Empieza en personal.** Pruébalo en tu Claude.
2. **Súbelo a la incubadora.** Déjalo en `incubadora/tu-nombre/` tal cual, con dos líneas que expliquen para qué sirve.
3. **Escribe la spec** si es una pieza grande: qué queremos, por qué y cómo sabremos que funciona. El formato está en [specs/README.md](../specs/README.md).
4. **Pasa al plugin** por PR cuando la otra persona lo haya revisado. Desde ese momento lo tenemos instalado los dos.

El material de Soraya para preparar sprints ya está en `incubadora/soraya/preparar-sprint/`, sin tocar. Será la base de la primera skill común.

## 6. Qué herramienta para qué

| Necesito | Voy a |
| --- | --- |
| Saber qué tareas hay y de quién son | Trello |
| Saber fechas, clases y quién es LI | Calendario OCT26 de Google |
| Actas, alumnos y fechas de entrega | Notion |
| Avisar a alumnos o al equipo | Slack |
| Saber cómo se hace algo o qué regla aplica | Este repo |

Los identificadores y enlaces están en [mapa-recursos.md](mapa-recursos.md). En el repo nunca van claves: cada uno conecta sus herramientas con su propia cuenta.

## 7. Qué está hecho y qué falta

Hecho: roles, funciones, semana tipo, LI por módulo, reglas de git, mapa de recursos, estructura del repo y un plugin con la primera skill (`normas-aie`).

Por hacer, en este orden propuesto:

| Spec | Qué resuelve |
| --- | --- |
| 001 | Cerrar la estructura del repo y del plugin |
| 002 | Completar el mapa de recursos y declarar los conectores |
| 003 | Primeras skills comunes: preparar sprint, actas y liberar sprint |
| 004 | Recordatorios de la semana tipo por rol |
| 005 | Archivo de mensajes de Slack |
| 006 | Estandarización de estilo y formato |

## 8. Para la reunión del 17/11

- Revisar la constitución y la asignación de funciones.
- Tutorías: propuesta de horarios.
- LI de M06 y puente del 7 y 8 de diciembre.
- Hoja de seguimiento de OCT26.
- Quién mantiene este repo.
- Trello: quitar la cuenta duplicada de Soraya y relevar a Alejandro Reyes como administrador del tablero.
