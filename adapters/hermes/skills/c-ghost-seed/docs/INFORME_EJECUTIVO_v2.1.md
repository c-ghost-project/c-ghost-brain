# INFORME EJECUTIVO — C://GHOST v2.1 (Optimizado)

**Fecha:** 2026-11-23
**Autor:** Hermes Agent (estratega del Comandante Dugui)
**Versión del cerebro:** v2.1.0
**Cambio principal:** de 10 a 12 protocolos, de 3 a 4 fases cognitivas, de 4 a 5 niveles de automatización, con 4 scripts determinísticos de soporte.

---

## 1. RESUMEN EJECUTIVO

C://GHOST v2.1 transforma el cerebro de un "manual de operación" a un **sistema operativo automatizado**. La diferencia clave: antes dependías de recordar ejecutar pasos manuales; ahora el propio sistema ejecuta validaciones, clasifica intenciones, rastrea cuotas y genera artefactos visuales sin que nadie tenga que pedírselo.

**Antes (v2.0):** Tú le decías a Hermes qué protocolo aplicar.
**Ahora (v2.1):** Hermes ejecuta el Nivel 0 (preflight) automáticamente antes de cualquier acción, clasifica tu intención con un clasificador embebido y elige el nivel óptimo sin comandos manuales.

---

## 2. ¿QUÉ CAMBIÓ? (v2.0 → v2.1)

| Aspecto | v2.0 | v2.1 |
|---------|------|------|
| **Protocolos** | 10 (P0–P10) | 12 (P0–P12) — añade P11 (preflight obligatorio) y P12 (migración segura) |
| **Fases cognitivas** | 3 (Comprender, Decidir, Ejecutar) | 4 (Pre-flight, Inicio, Ejecución, Cierre) |
| **Niveles de automatización** | 4 (Gobierno, Estrategia, Ejecución, Evidencia) | 5 (añade Nivel 0 determinístico + Nivel 4 visual) |
| **Handoff** | 5 campos en texto libre | 5 campos estructurados con nombres fijos `[SKILL REQUERIDA]`, `[OBJETIVO ATÓMICO]`, etc. |
| **Clasificación de tareas** | Manual (tú decidías) | Automática vía `intent_classify.py` (Pre-P1) |
| **Cuota Antigravity** | No rastreada | Rastreada en `STATUS.md` como `cuota_antigravity_usada` vía `quota_tracker.py` |
| **Artefactos visuales** | Manual | Autogenerados vía `visual_gen.py` (Mermaid → PNG/PDF) |
| **Migración de proyectos** | `--force` peligroso | `--migrate` con diff de tres vías, nunca sobrescribe memoria viva |
| **Scripts de soporte** | Ninguno | 4 scripts en `.agents/scripts/` |

---

## 3. EL NUEVO CEREBRO PASO A PASO

### 3.1 Estructura de archivos (ahora con 11 archivos base + 4 scripts)

```
<proyecto>/
├── .hermes.md              # Delta del proyecto + version: v2.1.0
├── AGENTS.md               # Constitución operativa (12 protocolos)
├── STATUS.md               # Memoria viva ≤100 líneas + cuota_antigravity_usada
├── IDEAS.md                # Fuga cero de ideas
├── CHANGELOG.md            # Histórico append-only
├── .agents/
│   ├── skills/
│   │   └── 01-core-domain/SKILL.md
│   ├── scripts/            # ← NUEVO en v2.1
│   │   ├── preflight_check.sh      # Nivel 0: validación pre-delegación
│   │   ├── intent_classify.py      # Pre-P1: clasificador de intención
│   │   ├── quota_tracker.py        # P3: rastreador cuota Antigravity
│   │   └── visual_gen.py           # Nivel 4: generador PNG/PDF
│   └── artifacts/          # ← NUEVO: diagramas generados
└── docs/whitepaper/
    └── README.md
```

### 3.2 Los 5 Niveles de la Pirámide (reemplazan a la pirámide de 4 niveles)

```
        ┌─────────────────────────────┐
        │  NIVEL 4 — Artefactos       │  $0 · visual_gen.py (Mermaid→PNG/PDF)
        │  Visuales autogenerados     │  Se activa si la tarea produce arquitectura
        ├─────────────────────────────┤
        │  NIVEL 3 — Antigravity CLI  │  Cuota · agy -p (fuerzas especiales)
        │  gemini-4-carbon-high,      │  Arquitectura crítica, UI/UX, WhitePapers,
        │  claude-opus-5-5, etc.      │  SQL complejo. Verificar cuota antes (>80% = alerta)
        ├─────────────────────────────┤
        │  NIVEL 2 — OpenCode CLI     │  $0 · opencode run -m deepseek-v4.1-flash-free
        │  Scaffolding, refactors,    │  ≥3 archivos o >80 líneas. En 2.º plano
        │  tests, migraciones         │  con notify_on_complete=true
        ├─────────────────────────────┤
        │  NIVEL 1 — Motor Nativo     │  $0 · ~60% del trabajo diario
        │  nemotron-3.5-super-vl,     │  Chat, análisis, redacción, razonamiento
        │  mistral-large-4, qwen2.5   │  Contingencia offline: Ollama local
        ├─────────────────────────────┤
        │  NIVEL 0 — Pre-flight       │  0 tokens · OBLIGATORIO siempre primero
        │  preflight_check.sh         │  Linters + typecheck + tests + git diff +
        │  (determinístico)           │  STATUS.md ≤100 líneas. Exit 0 = verde
        └─────────────────────────────┘
```

### 3.3 El Bucle Cognitivo de 4 Fases

```
┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐
│ FASE 0  │───→│ FASE 1  │───→│ FASE 2  │───→│ FASE 3  │
│Pre-flight│   │ Inicio  │    │Ejecución│    │ Cierre  │
│         │    │         │    │         │    │         │
│preflight│    │P0, P1   │    │P2, P3,  │    │P7 gate, │
│_check.sh│    │intent_  │    │P5, P11  │    │P0, P4,  │
│exit 0?  │    │classify │    │handoff  │    │P12, P6, │
│         │    │         │    │5 campos │    │P9+/N4   │
└────┬────┘    └─────────┘    └────┬────┘    └─────────┘
     │                              │
     ▼                              ▼
   SI FALLA →              Si cuota >80% → pedir
   reportar y DETENER      confirmación antes Nivel 3
```

### 3.4 Los 12 Protocolos (qué hace cada uno)

| # | Nombre | Función en v2.1 |
|---|--------|-----------------|
| P0 | Conciencia y Exclusividad | Lee STATUS.md primero; solo el Guardián escribe en STATUS/IDEAS/CHANGELOG |
| P1 | Zero-Command Routing | Clasificador embebido elige nivel/skill automático |
| P2 | Handoff Estructurado Zero-Trust | 5 campos fijos obligatorios; prohibido pasar credenciales |
| P3 | Economía de Fuerzas + Cuota | Micro-tareas directas (≤2 archivos); macro-tareas delegadas; verifica cuota antes Nivel 3 |
| P4 | Cierre y Ventana Deslizante | Actualiza STATUS.md + cuota; archiva últimas 5 tareas a CHANGELOG |
| P5 | Bifurcación de Entornos | Adapta criterio: Cloud / VPS / Directivo / Móvil |
| P6 | Fuga Cero de Ideas + WhitePaper | IDEAS.md para ideas; docs/whitepaper/ para hitos |
| P7 | Gate de Verificación | Zero-broken-commits: sin typecheck/lint/tests en verde, no se cierra |
| P8 | La Caja Negra | Si falta contexto: STATUS → CHANGELOG → git log → manifiestos |
| P9 | Activos Visuales | .webp + lazy loading + estética limpia |
| P10 | Semilla del Edén | Proyectos nuevos nacen con c-ghost-seed completo |
| **P11** | **Hook Pre-Delegación** | **NUEVO: preflight_check.sh obligatorio antes de Nivel 2/3** |
| **P12** | **Migración y Versionado** | **NUEVO: --migrate con diff 3-vías; version en .hermes.md** |

### 3.5 Clasificador de Intención Embebido (Pre-P1)

Antes de cualquier Protocolo 1, Hermes ejecuta:

```bash
echo "necesito refactorizar los tests del módulo de auth" | ./.agents/scripts/intent_classify.py
```

Salida:

```json
{
  "tipo": "Macro-Construcción",
  "nivel_recomendado": 2,
  "skill": "opencode-cli",
  "confianza": 0.85,
  "requiere_preflight": true
}
```

Si `confianza < 0.75` → Hermes pregunta al Comandante en lugar de asumir.

---

## 4. LOS 4 SCRIPTS DE SOPORTE (Nivel 0)

| Script | ¿Cuándo se ejecuta? | ¿Qué valida/produce? |
|--------|---------------------|----------------------|
| `preflight_check.sh` | **Siempre primero**, antes de cualquier delegación (P11) | git diff, ruff/eslint, tsc/mypy, pytest/vitest collect, STATUS.md ≤100 líneas, .hermes.md version. Exit 0 = verde |
| `intent_classify.py` | Antes de P1 (Pre-P1), en cada pedido | JSON con tipo, nivel, skill, confianza, requiere_preflight |
| `quota_tracker.py` | Antes de Nivel 3 (P3) y al cerrar tarea (P4) | Lee/actualiza `cuota_antigravity_usada` en STATUS.md; estima tokens por modelo |
| `visual_gen.py` | Nivel 4, cuando la tarea produce arquitectura/flujo/diseño | Mermaid en stdin → PNG (1920px, scale 2) + PDF (A4) en `.agents/artifacts/` |

---

## 5. MIGRACIÓN SEGURA (P12)

Si un proyecto ya tiene cerebro v2.0:

```bash
# NUNCA uses --force en proyectos existentes
python3 scripts/init_c_ghost.py --dir ./mi-proyecto --name "Mi Proyecto" --migrate
```

Esto:
1. Detecta STATUS.md/AGENTS.md preexistentes
2. **No los sobrescribe**
3. Genera diff de tres vías (plantilla v2.1 vs actual vs proyecto)
4. Crea solo los scripts nuevos en `.agents/scripts/`
5. Tú decides qué migrar manualmente viendo los diffs

---

## 6. MÉTRICAS DE MEJORA ESPERADAS

| Métrica | v2.0 | v2.1 | Mejora |
|---------|------|------|--------|
| Pasos manuales antes de delegar | 3-4 (leer STATUS, clasificar, decidir nivel) | 1 (preflight automático) | -70% fricción |
| Riesgo de olvidar preflight | Alto | Cero (P11 bloquea) | -100% |
| Visibilidad de cuota Antigravity | Ninguna | Campo en STATUS.md + script | Control proactivo |
| Tiempo para generar diagrama de arquitectura | Manual (~10 min) | Automático (~30 seg) | -95% |
| Seguridad en migración de proyectos | --force destructivo | --migrate con diff 3-vías | Cero pérdida de datos |
| Tokens gastados en tareas mecánicas | ~40% en Nivel 1 | ~60% en Nivel 1, resto en Nivel 0/2/4 ($0) | +20% eficiencia |

---

## 7. PRÓXIMOS PASOS RECOMENDADOS

1. **Migrar este repositorio** (el de la skill c-ghost-seed) a v2.1 con `--migrate`.
2. **Probar preflight** en cualquier proyecto existente: `./.agents/scripts/preflight_check.sh`.
3. **Usar intent_classify** en tus próximos 5 pedidos para calibrar el clasificador.
4. **Generar el primer artefacto visual**: pipe cualquier diagrama Mermaid a `visual_gen.py`.
5. **Registrar cuota Antigravity** después de cada uso de Nivel 3 con `quota_tracker.py add`.

---

*Informe generado por Hermes Agent bajo C://GHOST v2.1 — Protocolo 6 (WhitePaper sincronizado).*