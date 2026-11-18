# Modelos de Gemini para el Sprint 05 (capa gratuita)

*Texto pensado para pegarlo tal cual en el README del sprint (antes del «### Workout» del Bloque 2, como en el S05). Comprobado el 17/11/2026 con una clave gratuita y `google-genai` 3.4.0. Las tablas de los sprints siguientes mantienen este mismo formato.*

*Nota para quien prepara el sprint: un modelo `*-preview` da `404` con `google-genai` 3.x aunque responda por `curl` (el SDK usa la API `v1`). Prueba siempre con el SDK.*

---

### 🤖 Qué modelo de Gemini usar

Usa uno de estos modelos en la variable `MODEL`. Son de la **capa gratuita** de la API de Gemini.

| Modelo (`MODEL = …`) | ¿Cuándo usarlo? | Estado comprobado (17/11/2026) |
|---|---|---|
| `gemini-3.6-flash` | **Recomendado** para todo el sprint | ✅ Responde |
| `gemini-3.5-flash-lite` | Alternativa más ligera, si el anterior da 429 o 503 | ✅ Responde |
| `gemini-3.8-flash` | El más nuevo. Google lo recomienda para proyectos nuevos | ⚠️ Daba `503 UNAVAILABLE` (saturado). Puede fallar en horas punta |

**No uses:**
- `gemini-3-flash-preview`: con la librería `google-genai` 3.x da `404 NOT_FOUND` (la librería usa una versión de la API que no incluye los modelos «preview»).
- `gemini-2.5-flash`: Google solo lo deja usar a cuentas que ya lo usaban. A una cuenta nueva le da `404`.

**Si te sale un error:**
- `503 UNAVAILABLE` → el modelo está saturado. Espera unos segundos y reintenta, o cambia a otro modelo de la tabla.
- `429 RESOURCE_EXHAUSTED` → has gastado tu cuota gratuita (por minuto o por día). Espera y no repitas celdas sin necesidad.
- `404 NOT_FOUND … is not found` → el nombre del modelo no existe. Revisa que esté bien escrito.
- `400 … API key not valid` → la clave del `.env` no es correcta.

**Para ver la lista actualizada:**
- Modelos gratuitos y precios: <https://ai.google.dev/gemini-api/docs/pricing> (columna «Free tier»).
- Los modelos que tu clave puede usar, desde Python:
  ```python
  from google import genai
  client = genai.Client()
  print([m.name for m in client.models.list() if "flash" in m.name])
  ```

> Los modelos cambian cada pocos meses. Si un nombre deja de funcionar, consulta la página de precios.
