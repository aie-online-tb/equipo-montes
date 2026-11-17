# Live Review 1 – Sprint 13: LangGraph, Human-in-the-Loop y Multi-agente

> Clase impartida por Jorge López Blasco. Último sprint del módulo de Agentes.
> Formato: apuntes breves con timestamps.

---

## 🎯 Ideas claves
- Un grafo de **LangGraph** no es exótico: es el mismo bucle `modelo → tools → modelo`, pero con estado y bifurcaciones aparte.
- Sin **Checkpointer** no hay pausa; sin pausa no hay **Human-in-the-Loop**.
- El modelo propone el siguiente paso, pero **Python siempre decide** (regla determinista por debajo).

---

## 📑 Índice
1. Patrón ReAct y Reducer
2. Persistencia: Checkpointer, MemorySaver, `thread_id`
3. Human-in-the-Loop (HITL)
4. Supervisor + especialistas (práctica AirReview)
5. Cierre: anécdota multimodal

---

## 1. Patrón ReAct y Reducer  ⏱ 00:12–00:23

**ReAct** = loop `agent → ¿pide tool? → tools → agent`. El router condicional mira la última respuesta: si hay `tool_calls` → `tools`; si no → `END`.

El **Reducer** es una anotación sobre un campo del estado (p. ej. `messages`, `log`) que **acumula** en vez de pisar. Hoy lo usamos en `log` y en la traza de herramientas.

⚠️ olvidar la arista de vuelta `tools → agent` deja al modelo sin ver el resultado de la herramienta y respondiendo como si no hubiera pasado nada.

---

## 2. Persistencia: Checkpointer, MemorySaver, `thread_id`  ⏱ 00:29–00:38

Hasta ahora el estado lo guardaba quien llamara al agente. LangGraph propone que **el propio grafo guarde una foto de su estado en cada paso** (*checkpoint*).

| Pieza | Qué hace |
|---|---|
| **Checkpoint** | Foto del estado tras cada paso |
| **`thread_id`** | Id de la conversación (dos ids = memorias separadas) |
| **Checkpointer** | Guarda las fotos. `MemorySaver` en RAM (clase/demo); SQLite/Postgres en producción |

`get_state(cfg)` devuelve `values` (estado actual) y `next` (nodos pendientes: vacío si terminó, con nombre si está pausado).

📌 **Reducer** ≠ **Checkpointer**: el primero acumula **dentro** de una ejecución; el segundo guarda **entre** ejecuciones.

---

## 3. Human-in-the-Loop (HITL)  ⏱ 00:39–00:53

Hay acciones que un agente no debe hacer solo (mandar correo, cerrar incidencia, aplicar un plan). Con HITL dejamos que trabaje libre hasta un paso sensible y, justo antes, **se para y pregunta**. LangGraph lo trae de serie.

En código son 3 líneas:

```python
app = grafo.compile(
    checkpointer=MemorySaver(),
    interrupt_before=["aplicar"],
)
app.update_state(cfg, {"decision": "aprobado"})   # inyectar decisión
app.invoke(None, cfg)                              # reanudar
```

💡 la pausa **no es un `input()` bloqueante**: el proceso termina y el estado queda guardado. Por eso HITL **necesita Checkpointer**.

**Time-travel**: como `thread_id` identifica el hilo, se puede inspeccionar un checkpoint antiguo, bifurcar o reanudar desde el pasado (similar a `git checkout` / `git revert`).

---

## 4. Supervisor + especialistas (práctica AirReview)  ⏱ 00:53–01:42

El grafo de la práctica **no es ReAct puro**: es un **supervisor** que reparte trabajo entre 3 especialistas. El bucle de herramientas vive dentro de cada especialista en `ejecutar_tools()` (el bucle del Sprint 12 con otro nombre).

Las 4 piezas: estado compartido, supervisor (decide quién sigue, **no redacta**), especialistas, y arista de vuelta fija al supervisor. Freno: `MAX_ITER` aplicado por Python en el nodo supervisor — no por el modelo.

Reglas del router sobre `finish`:

- Si supervisor dice `finish` → el router manda a **`aplicar`** (donde está la pausa). Nadie cierra sin aprobación.
- Si dice `finish` pero no hay plan ni respuesta → redirige a `sintetizar`. No se cierra con las manos vacías.

⚠️ compilar el grafo en cada turno crea un `MemorySaver` nuevo y el agente no recuerda nada. **Compilar una sola vez.**

---

## 5. Cierre: anécdota multimodal  ⏱ 01:45–01:49

Google sacó una demo multimodal que parecía real-time; resultó no serlo del todo → caída en bolsa, limpieza de equipo. Meses después OpenAI publica **GPT-4o** y confirma que la multimodalidad real es posible. Hoy Google va recuperando el ritmo.

Mañana: pasar imágenes a una tool con Gemini (`describir_imagen`).

---

## 📌 Glosario rápido

| Término | Significado |
|---|---|
| **ReAct** | Patrón *Reason + Act*: modelo → tool → modelo |
| **Reducer** | Función que acumula en el estado en vez de pisar |
| **Checkpointer** | Componente que guarda los checkpoints (MemorySaver, SQLite, Postgres) |
| **`thread_id`** | Identificador del hilo de conversación |
| **HITL** | Human-in-the-Loop — pausa para aprobación humana |
| **`invoke(None, cfg)`** | Reanudar un grafo pausado sin añadir input nuevo |

---

## ❓ Dudas resueltas en clase

- **¿Se puede volver a un checkpoint pasado?** — Sí: *time-travel*. Listar, inspeccionar, bifurcar o reanudar desde uno antiguo (análogo a `git checkout`).
- **¿Qué es `cfg`?** — Abreviatura de *config*: `{"configurable": {"thread_id": "..."}}`. Identifica el hilo que se retoma.
- **¿Hay que tirar el código del Sprint 12?** — No. `Max Steps`, la whitelist y la función que ejecuta tools se reutilizan tal cual; solo cambian de sitio dentro del grafo.

---

## 📅 Pendiente para mañana

- Tercer TODO: `procesar_turno` (uso real del HITL).
- Interacción desde Streamlit con 3 memorias (chat, estado grafo, traza).
- Multimodalidad: pasar imágenes a una tool con Gemini.
