# Activar las rutinas

Cada persona activa su **diaria** y su rutina de **PRs**. La **maestra** solo la activa Hugo, porque es la única que escribe en Trello y necesita el secreto de Trello de su entorno. El detalle de cada rutina está en [rutinas/](../../rutinas/README.md).

## 1. Crear la tarea programada

En tu cuenta de Claude, crea una tarea programada (rutina) con:

| Campo | Diaria | PRs | Maestra |
| --- | --- | --- | --- |
| Nombre | `Equipo Montes · Diaria · {tu nombre}` | `Equipo Montes · PRs · {tu nombre}` | `Equipo Montes · Maestra` |
| Horario | De lunes a viernes, 9:00 | De lunes a viernes, 12:00 y 17:00 | De lunes a viernes, 8:00 |
| Repos, lectura | `equipo-montes` y los del bootcamp | `equipo-montes` y los del bootcamp | `equipo-montes` y `bootcamp_AI_Engineering_10_26` |
| Conectores | GitHub, Google Calendar, Trello, Google Sheets | GitHub | GitHub, Google Calendar, Trello |
| Entorno | El tuyo | El tuyo | El que tiene el secreto de Trello |
| Modelo | Uno ligero | Uno ligero | Uno ligero |

Todos los horarios en Europe/Madrid. Los repos del bootcamp son `bootcamp_AI_Engineering_10_26`, `material_bootcamp_AI_Engineering` y `workouts_AIE_permanente`.

## 2. Texto de la rutina

Cambia `{…}`. Mientras `main` esté vacío, usa `develop` como rama.

```
Eres la rutina «{Diaria | PRs | Maestra}» del equipo docente de AI Engineering de The Bridge.
Persona: {Hugo | Soraya}.
Lee el fichero rutinas/{diaria | revision-prs | maestra}.md de la rama {main | develop} del repo aie-online-tb/equipo-montes y síguelo al pie de la letra.
Nunca publiques nada en Slack ni cambies el campus. En Trello, sigue exactamente lo que diga ese fichero.
```

## 3. Probarla

Lánzala una vez a mano y comprueba que:

- el aviso dice bien el sprint de esta semana y tu rol (LI o TA);
- cabe en una pantalla de móvil;
- la maestra no ha creado tarjetas duplicadas.

Si algo falla, no cambies el texto de la rutina: corrige el fichero de `rutinas/` por PR.
