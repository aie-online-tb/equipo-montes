# Activar las rutinas

Cada persona activa su **diaria** y su rutina de **PRs**. La **maestra** solo la activa Hugo, porque es la única que escribe en Trello y necesita el secreto de Trello de su entorno. El detalle de cada rutina está en [rutinas/](../../rutinas/README.md).

## 0. Tu hilo «Avisos» (solo la diaria)

La diaria es el único aviso de la mañana y llega siempre al **mismo hilo**, no a uno nuevo por ejecución.

1. Crea en tu cuenta un hilo que se llame `Avisos diarios de equipo-montes`, con los repos de `equipo-montes` y del bootcamp.
2. En ese hilo, pide a Claude que cree la rutina de la diaria **atada a ese mismo hilo** (así cada ejecución escribe ahí).

La maestra y la rutina de PRs no avisan por su cuenta: la diaria recoge lo suyo.

## 1. Crear la tarea programada

En tu cuenta de Claude, crea una tarea programada (rutina) con:

| Campo | Diaria | PRs | Maestra |
| --- | --- | --- | --- |
| Nombre | `Equipo Montes · Diaria · {tu nombre}` | `Equipo Montes · PRs · {tu nombre}` | `Equipo Montes · Maestra` |
| Horario | De lunes a viernes, 9:00 | De lunes a viernes, 12:00 y 17:00 | De lunes a viernes, 8:00 |
| Hilo | El de Avisos (apartado 0) | Uno por ejecución | Uno por ejecución |
| Repos, lectura | `equipo-montes` y los del bootcamp | `equipo-montes` y los del bootcamp | `equipo-montes` y `bootcamp_AI_Engineering_10_26` |
| Conectores | GitHub, Google Calendar, Trello, Google Sheets | GitHub | GitHub, Google Calendar, Trello |
| Entorno | El tuyo | El tuyo | El que tiene el secreto de Trello |
| Modelo | Uno ligero | Uno ligero | Uno ligero |

Todos los horarios en Europe/Madrid. Los repos del bootcamp son `bootcamp_AI_Engineering_10_26` y `material_bootcamp_AI_Engineering`.

## 2. Texto de la rutina

Cambia `{…}`.

```
Eres la rutina «{Diaria | PRs | Maestra}» del equipo docente de AI Engineering de The Bridge.
Persona: {Hugo | Soraya}.
Lee el fichero rutinas/{diaria | revision-prs | maestra}.md de la rama main del repo aie-online-tb/equipo-montes y síguelo al pie de la letra.
Nunca publiques nada en Slack ni cambies el campus. En Trello, sigue exactamente lo que diga ese fichero.
```

Para la diaria, añade una línea: `Publica el aviso en este hilo, con el formato del apartado 6 de ese fichero, y después la tarjeta de skills recomendadas.`

## 3. Probarla

Lánzala una vez a mano y comprueba que:

- el aviso dice bien el sprint de esta semana y tu rol (LI o TA);
- cabe en una pantalla de móvil;
- debajo del aviso sale la tarjeta de skills recomendadas, y solo con skills que te tocan a ti (`kahoot` y `subir-video` son solo de Hugo);
- la maestra no ha creado tarjetas duplicadas.

Pulsa una opción de la tarjeta que solo deje un borrador, como `apertura-sprint`, y comprueba que el hilo lo prepara. Si tu cuenta no tiene las tarjetas de opciones o el plugin `aie-equipo`, el aviso acaba en una línea de texto con las skills y las lanzas a mano.

Si algo falla, no cambies el texto de la rutina: corrige el fichero de `rutinas/` por PR.
