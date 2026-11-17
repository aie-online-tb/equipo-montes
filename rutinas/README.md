# Rutinas

Tareas programadas de Claude. Las instrucciones están aquí; la tarea programada solo dice qué fichero seguir.

| Rutina | Fichero | Cuándo | En qué cuenta | Qué hace |
| --- | --- | --- | --- | --- |
| Maestra | [maestra.md](maestra.md) | De lunes a viernes, 8:00 | Solo la de Hugo | Crea tarjetas, comprueba la copia al repo de alumnos y deja borradores en Trello |
| Diaria | [diaria.md](diaria.md) | De lunes a viernes, 9:00 | La de cada uno | Solo lee: resume a cada uno lo suyo |

Una sola rutina escribe y dos leen. Así no hay tarjetas duplicadas y cada uno puede apagar su diaria sin afectar al otro.

## Cómo se activa

1. Crea una tarea programada en tu cuenta de Claude, con el horario de la tabla y la zona horaria Europe/Madrid.
2. Dale acceso a los conectores que pide el fichero y al repo `aie-online-tb/equipo-montes`. La maestra necesita además el entorno con el secreto de Trello.
3. Pega este texto, cambiando el nombre:

```
Eres la rutina «{Maestra | Diaria}» del equipo de AI Engineering de The Bridge.
Persona: {Hugo | Soraya}.
Lee el fichero rutinas/{maestra | diaria}.md de la rama main del repo aie-online-tb/equipo-montes y síguelo al pie de la letra.
```

## Reglas para todas las rutinas

- Usa un modelo ligero. Lo que cuesta es el razonamiento largo, no la rutina.
- Nunca publican en Slack, nunca cambian el campus y nunca mueven, archivan ni borran tarjetas. Solo la maestra crea tarjetas y comenta en ellas.
- Si falta un dato o un conector, lo dicen en el aviso y siguen con lo demás.
