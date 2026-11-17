# Entorno en la nube: red y secretos

Lo que no queda en el código y cada persona tiene que replicar en su propio entorno de Claude (el de las sesiones y rutinas en la nube). Se hace una vez. **Nunca se escribe una clave en el repo ni se pega en el chat**: la introduce cada persona en los ajustes.

Dónde: en el proyecto de Claude, *Project settings* → entorno en la nube → engranaje junto al entorno. Hay dos sitios: *Allowed domains* (red) y *Network secrets* (claves).

## Hosts permitidos (red limitada)

Para revisar un sprint (`preparar-sprint`, fases 0 y 0b) el entorno necesita llegar a la documentación oficial de Gemini y a su API:

| Host | Para qué |
| --- | --- |
| `ai.google.dev` | Páginas de precios y de modelos deprecados |
| `aistudio.google.com` | Destino al que redirige `ai.google.dev` |
| `generativelanguage.googleapis.com` | La API de Gemini, para comprobar que el modelo responde |

Los cambios de red se aplican en segundos a las sesiones abiertas.

## Secreto de Gemini

Cada persona usa **su propia clave** de [Google AI Studio](https://aistudio.google.com/) (capa gratuita). Es la misma que va en su `.env`.

| Campo | Valor |
| --- | --- |
| Tipo de secreto | Bearer (no te pide ningún token aparte; solo se envía la cabecera personalizada) |
| Sitios web permitidos | `generativelanguage.googleapis.com` |
| Prefijos de ruta | Vacío (permite el host completo) |
| Encabezado personalizado, nombre | `x-goog-api-key` |
| Prefijo | Vacío |
| Valor | Tu clave de Gemini |

Solo lo ven las **sesiones creadas después** de guardarlo. Las abiertas antes pueden no verlo.

### Comprobarlo

En una sesión nueva, sin escribir la clave en ningún sitio:

```bash
curl -s -o /dev/null -w '%{http_code}\n' "https://generativelanguage.googleapis.com/v1beta/models"
```

Debe dar `200`. Con el SDK de Python, `GEMINI_API_KEY=dummy` basta: el proxy sustituye la cabecera.

### Cuidado con la cuota

La capa gratuita da `429 RESOURCE_EXHAUSTED` si se lanzan muchas llamadas seguidas. Ejecuta de uno en uno, nunca notebooks en paralelo.

## Quién y cuándo

Cada uno en su entorno, antes de preparar su primer sprint. Si algo cambia (un host nuevo, otro secreto), se actualiza esta página por PR.
