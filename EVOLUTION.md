# 🧬 Evolución Histórica — Metodología y Cerebro Operativo `C://GHOST` (`v1.0 → v3.0`)

Este documento resume la progresión real de las cuatro generaciones publicadas como *Git Releases* en este repositorio para que desarrolladores, estudiantes e investigadores comprendan **por qué nació cada mecanismo**.

| Generación | Release / Tag | Problema que Resolvió | Innovaciones Introducidas | Manual Paso a Paso |
| :--- | :---: | :--- | :--- | :--- |
| **1.ª — Génesis** | `v1.0.0` | **Amnesia del Chat** en sesiones largas y sobrecarga cognitiva al pedir estrategia y código al mismo LLM. | Patrón **LLM-Wiki** (`STATUS.md` inmutable), separación **Estratega ("Jobs") vs. Ejecutor ("Wozniak")** y guía accesible para principiantes sin código. | [MANUAL_V1_GENESIS.md](docs/manuals/MANUAL_V1_GENESIS.md) |
| **2.ª — Semilla del Edén** | `v2.0.0` | Crecimiento infinito de `STATUS.md` y saturación de contexto al inyectar todas las reglas de golpe. | **10 Protocolos Maestros**, tríada de memoria con **ventana deslizante (`STATUS.md ≤ 100` líneas + `IDEAS.md` + `CHANGELOG.md`)**, **Skills Progresivas** (`.agents/skills/`), Handoff de 5 campos y Gate Pre-Commit. | [MANUAL_V2_SEMILLA_DEL_EDEN.md](docs/manuals/MANUAL_V2_SEMILLA_DEL_EDEN.md) |
| **3.ª — Hermes × C://GHOST** | `v2.1.0` | Quema innecesaria de cuotas premium en tareas repetitivas y riesgo de sobrescribir cerebros existentes. | **12 Protocolos** (`P11` Pre-flight Nivel 0 + `P12` `--migrate` de 3 vías), **Pirámide de 5 Niveles a costo \$0**, `init_c_ghost.py` en Python stdlib, `intent_classify.py`, `quota_tracker.py` (alerta 80%) y `visual_gen.py` (Mermaid → PNG/PDF). | [MANUAL_V2.1_HERMES.md](docs/manuals/MANUAL_V2.1_HERMES.md) |
| **4.ª — Edición Universal** | `v3.0.0` *(Latest)* | Plantillas acopladas a una sola nube, stack o gestor de tareas; falta de cumplimiento mecánico de reglas al cerrar turno. | **100% agnóstico**, flujo en **2 Prompts** (*Marcar la Semilla* → *Morfogénesis Camaleónica* en 3 modos), **Lifecycle Hooks** (`SessionStart`, `PreToolUse` Zero-Trust y `Stop` anti-bucle con `continuationActive`), `Workspace: "share"`, `run_workflow` y adaptador oficial Hermes incluido. | [MANUAL_V3_UNIVERSAL.md](docs/manuals/MANUAL_V3_UNIVERSAL.md) |

---

## Cómo inspeccionar cualquier generación exacta en Git

```bash
git tag -l -n1              # Listar las 4 generaciones etiquetadas
git checkout v1.0.0         # Explorar el estado exacto de v1.0 (Génesis)
git checkout v2.0.0         # Explorar el estado exacto de v2.0 (Semilla del Edén)
git checkout v2.1.0         # Explorar el estado exacto de v2.1 (Hermes × C://GHOST)
git checkout main           # Volver a v3.0.0 (Universal + Adaptador Hermes + 4 Manuales)
```
