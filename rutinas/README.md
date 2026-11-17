# Rutinas

Tareas programadas de Claude. Las instrucciones están aquí; la tarea programada solo dice qué fichero seguir.

| Rutina | Fichero | Cuándo | En qué cuenta | Qué hace |
| --- | --- | --- | --- | --- |
| Maestra | [maestra.md](maestra.md) | De lunes a viernes, 8:00 | Solo la de Hugo | Crea tarjetas, comprueba la copia al repo de alumnos y deja borradores en Trello |
| Diaria | [diaria.md](diaria.md) | De lunes a viernes, 9:00 | La de cada uno | Solo lee: un único aviso al día, siempre en tu hilo «Avisos», con lo tuyo y una tarjeta de skills recomendadas |
| PRs | [revision-prs.md](revision-prs.md) | De lunes a viernes, 12:00 y 17:00 | La de cada uno | Avisa de las PRs a `main` que esperan tu revisión; si no hay, no avisa |

Una sola rutina escribe y las demás solo leen. Así no hay tarjetas duplicadas y cada uno puede apagar su diaria sin afectar al otro.

## Cómo se activa

Los pasos completos, con el texto que se pega, están en [setup/prompts/activar-rutinas.md](../setup/prompts/activar-rutinas.md). En resumen:

1. Crea tu hilo «Avisos» (solo la diaria): la diaria escribe siempre ahí.
2. Crea una tarea programada en tu cuenta de Claude, con el horario de la tabla y la zona horaria Europe/Madrid.
3. Dale acceso a los conectores que pide el fichero y al repo `aie-online-tb/equipo-montes`. La maestra necesita además el entorno con el secreto de Trello.
4. Pega este texto, cambiando el nombre:

```
Eres la rutina «{Maestra | Diaria}» del equipo de AI Engineering de The Bridge.
Persona: {Hugo | Soraya}.
Lee el fichero rutinas/{maestra | diaria}.md de la rama main del repo aie-online-tb/equipo-montes y síguelo al pie de la letra.
```

## Reglas para todas las rutinas

- Usa un modelo ligero. Lo que cuesta es el razonamiento largo, no la rutina.
- Nunca publican en Slack, nunca cambian el campus y nunca mueven, archivan ni borran tarjetas. Solo la maestra crea tarjetas y comenta en ellas, y solo archiva las de Done tras un «OK» de Hugo en su tarjeta.
- Si falta un dato o un conector, lo dicen en el aviso y siguen con lo demás.
