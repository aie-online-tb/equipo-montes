# Guía de estilo de los apuntes de clase

Los apuntes son el **registro didáctico** de una Live Review: no son transcripción ni resumen plano. El lector típico es un alumno que quiere repasar sin volver al vídeo. El PDF debe caber en **~4 páginas interiores** (sin portada) y leerse de un vistazo.

Mirar siempre `plantillas/ejemplo_LR1_sprint13.md` como referencia de **longitud y densidad**.

## Tono

- Español, segunda persona o impersonal. Frases cortas y claras.
- Técnico sin jerga de más: define términos nuevos la primera vez que aparecen.
- Nombres de código, archivos y métodos en `` `inline code` ``.
- Negrita para los **conceptos clave**. Cursiva para *matices*.
- Citas literales de la clase: `>` + comillas.

## Callouts: una sola regla

Permitidos: `⚠️ 💡 📌 ✅ ❌`, al **inicio de línea**, con moderación (3–5 en todo el documento como máximo).

El PDF los pinta en rojo con una palabra delante:

| Emoji | Palabra que inserta el PDF |
|---|---|
| ⚠️ | Atención: |
| 💡 | Idea: |
| 📌 | Nota: |
| ✅ | Sí |
| ❌ | No |

**Redacta la frase de forma que lea bien con esa palabra delante.**

### Qué NO escribir (fuente de bugs reales)

```markdown
❌ MAL:  💡 **Idea:** el modelo propone, Python decide.
❌ MAL:  ⚠️ **Atención:** olvidar la vuelta rompe el bucle.
❌ MAL:  📌 **Nota:** el estado arranca con cadenas vacías.
```

En el PDF esto se verá como *"Idea: Idea: …"*, *"Atención: Atención: …"*, *"Nota: Nota: …"*. **Nunca repitas la palabra**: ya la inserta el script.

```markdown
✅ BIEN: 💡 el modelo propone, Python decide.
✅ BIEN: ⚠️ olvidar la vuelta rompe el bucle.
✅ BIEN: 📌 el estado arranca con cadenas vacías.
```

Si quieres introducir un matiz adicional, usa otras palabras: `⚠️ **Error típico:** olvidar la vuelta` sí es válido (porque "Error típico" ≠ "Atención"). Pero en general: menos es más.

## Qué va en cada sección fija

- **Ideas claves** → **3 bullets de 1 línea**. La tesis de la clase.
- **Índice** → numeración 1..N consistente con los `## N. …` del cuerpo.
- **Secciones de desarrollo** (3–5) → cada una con `⏱ HH:MM–HH:MM` en el título, cuerpo de **2–5 líneas** + lista corta opcional. Puede cerrarse con un callout (`⚠️`, `💡`) cuando aplique.
- **Glosario** → **opcional**. Solo si hay 3–6 términos **que no estén ya explicados en el cuerpo**.
- **Dudas resueltas** → **opcional**. Máx. **3 dudas** con respuesta de **1–2 líneas**. Solo preguntas de alumnos realmente respondidas en clase.
- **Pendiente** → solo si el profesor anunció próximos pasos concretos.

## Longitud dura

| | Objetivo |
|---|---|
| Líneas totales del `.md` | **70–130** |
| Secciones de desarrollo | **3–5** |
| Tablas en todo el documento | **≤ 3** |
| Bloques de código | **≤ 2**, cada uno **≤ 12 líneas** |

Si te pasas, estás transcribiendo. Si te quedas corto, agrupa secciones o quita glosario.

## Reglas duras

- **Cero alucinación**: todo debe estar en el VTT. Si una idea no está, no inventar.
- **Timestamps**: `HH:MM` con dos dígitos; rango `HH:MM–HH:MM` con **guion largo `–`** (no `-`).
- **No copiar la transcripción**: reescribir. Un párrafo nuestro vale más que diez líneas pegadas.
- **No incluir ruido**: saludos, "¿me oís?", esperas, chistes privados.
- **Código del profesor**: cuando dicta/muestra un bloque, reconstrúyelo limpio. Si no se ve en pantalla, descríbelo en prosa — no inventes la sintaxis.
- **Nombres propios de alumnos**: solo si son imprescindibles; mejor "una pregunta del alumnado".
- **No duplicar entre cuerpo y glosario**.

## Qué NO debe aparecer

- Firmas, correos, enlaces de Zoom.
- Especulaciones ("quizás el profe quiso decir…").
- Referencias cruzadas inventadas a otros sprints.
- Las palabras "Idea:", "Nota:", "Atención:", "Sí", "No" **inmediatamente después** de su emoji.
