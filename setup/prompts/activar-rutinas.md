# Activar las rutinas

Cada persona activa su **diaria**. La **maestra** solo la activa Hugo, porque es la única que escribe en Trello y necesita el secreto de Trello de su entorno. El detalle de cada rutina está en [rutinas/](../../rutinas/README.md).

## 1. Crear la tarea programada

En tu cuenta de Claude, crea una tarea programada (rutina) con:

| Campo | Diaria | Maestra |
| --- | --- | --- |
| Nombre | `Equipo Montes · Diaria · {tu nombre}` | `Equipo Montes · Maestra` |
| Horario | De lunes a viernes, 9:00, Europe/Madrid | De lunes a viernes, 8:00, Europe/Madrid |
| Repo | `aie-online-tb/equipo-montes`, lectura | `aie-online-tb/equipo-montes` y `aie-online-tb/bootcamp_AI_Engineering_10_26`, lectura |
| Conectores | GitHub, Google Calendar, Trello, Google Sheets | GitHub, Google Calendar, Trello |
| Entorno | El tuyo | El que tiene el secreto de Trello |
| Modelo | Uno ligero | Uno ligero |

## 2. Texto de la rutina

Cambia `{…}`. Mientras `main` esté vacío, usa `develop` como rama.

```
Eres la rutina «{Diaria | Maestra}» del equipo docente de AI Engineering de The Bridge.
Persona: {Hugo | Soraya}.
Lee el fichero rutinas/{diaria | maestra}.md de la rama {main | develop} del repo aie-online-tb/equipo-montes y síguelo al pie de la letra.
Nunca publiques nada en Slack ni cambies el campus. En Trello, sigue exactamente lo que diga ese fichero.
```

## 3. Probarla

Lánzala una vez a mano y comprueba que:

- el aviso dice bien el sprint de esta semana y tu rol (LI o TA);
- cabe en una pantalla de móvil;
- la maestra no ha creado tarjetas duplicadas.

Si algo falla, no cambies el texto de la rutina: corrige el fichero de `rutinas/` por PR.
