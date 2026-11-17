# Modelos de Gemini para el Sprint 04 (capa gratuita)

*Texto pensado para pegarlo tal cual en el README del sprint (ver abajo dónde). Comprobado el 10/11/2026 con una clave gratuita y `google-genai` 3.0.0.*

---

### 🤖 Qué modelo de Gemini usar

Usa uno de estos modelos en la variable `MODEL`. Son de la **capa gratuita** de la API de Gemini.

| Modelo (`MODEL = …`) | ¿Cuándo usarlo? | Estado comprobado (10/11/2026) |
|---|---|---|
| `gemini-3.6-flash` | **Recomendado** para todo el sprint | ✅ Responde: texto, JSON, `system_instruction`, streaming y chat |
| `gemini-3.5-flash-lite` | Alternativa más ligera, si el anterior da 429 o 503 | ✅ Responde |
| `gemini-3.8-flash` | El más nuevo. Google lo recomienda para proyectos nuevos | ⚠️ Daba `503 UNAVAILABLE` (saturado). Puede fallar en horas punta |

**No uses:**
- `gemini-3-flash-preview` (el que sale en la teoría): **ya no existe** → `404 NOT_FOUND`.
- `gemini-2.5-flash` (el que sale en los ejercicios): Google solo lo deja usar a cuentas que ya lo usaban. A una cuenta nueva le puede fallar. Además, con `google-genai` 3.x **no admite** el modo JSON ni `system_instruction`.

**Si te sale un error:**
- `503 UNAVAILABLE` → el modelo está saturado. Espera unos segundos y reintenta, o cambia a otro modelo de la tabla.
- `429 RESOURCE_EXHAUSTED` → has gastado tu cuota gratuita (por minuto o por día). Espera y no repitas celdas sin necesidad.
- `404 NOT_FOUND … is not found` → el nombre del modelo no existe. Revisa que esté bien escrito.
- `400 … API key not valid` → la clave del `.env` no es correcta.

**Para ver la lista actualizada:**
- Modelos gratuitos y precios: <https://ai.google.dev/pricing> (columna «Free tier»).
- Los modelos que tu clave puede usar, desde Python:
  ```python
  from google import genai
  client = genai.Client()
  print([m.name for m in client.models.list() if "flash" in m.name])
  ```

> Los modelos cambian cada pocos meses. Si un nombre deja de funcionar, consulta la página de precios.

---

## Dónde ponerlo (para el TA)

Sí, merece la pena ponerlo en el README: es lo primero que leen y así el modelo está en un único sitio.

1. **`Sprint_04/README.md`**: pegar la sección anterior justo **después de la lista «¿Qué aprenderás?» del Bloque 02** (después de la línea 53, antes del `---`).
2. **`01_Teoria/02_IA_generativa_python/readme.md`**: añadir una línea al principio: «Modelo a usar en este bloque: ver la sección *Qué modelo de Gemini usar* del README del sprint».
3. Cambiar `MODEL = "gemini-3-flash-preview"` y `MODEL = "gemini-2.5-flash"` por `MODEL = "gemini-3.6-flash"` en los ficheros que lista `cambios_README_teoria_v2.md` (G2).
