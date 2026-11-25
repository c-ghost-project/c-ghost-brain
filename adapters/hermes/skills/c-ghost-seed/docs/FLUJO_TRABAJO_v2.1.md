# DIAGRAMA DE FLUJO — C://GHOST v2.1

## Flujo completo de trabajo (4 Fases + 5 Niveles)

```mermaid
flowchart TD
    A["👤 Comandante envía pedido"] --> B["🔍 Pre-P1: intent_classify.py<br/>Clasifica intención → JSON<br/>{tipo, nivel, skill, confianza}"]
    B --> C{"¿confianza ≥ 0.75?"}
    C -->|"No"| D["❓ Hermes pregunta<br/>al Comandante"]
    D --> B
    C -->|"Sí"| E["⚙️ FASE 0: preflight_check.sh<br/>git diff + linters + typecheck<br/>+ test discovery + STATUS.md ≤100 líneas"]
    E --> F{"¿exit code 0?"}
    F -->|"No ❌"| G["🛑 Reportar errores<br/>y DETENER"]
    F -->|"Sí ✅"| H["📋 FASE 1: Inicio<br/>Leer STATUS.md + .hermes.md<br/>Detectar skill del pilar"]
    H --> I{"¿Nivel recomendado?"}
    I -->|"Nivel 0"| J["🔧 Ejecutar preflight<br/>ya hecho — continuar"]
    I -->|"Nivel 1"| K["🧠 Motor Nativo Hermes<br/>nemotron-3.5-super-vl /<br/>mistral-large-4 / qwen2.5 local<br/>~60% del trabajo ($0)"]
    I -->|"Nivel 2"| L["📦 opencode-cli (2.º plano)<br/>opencode/deepseek-v4.1-flash-free<br/>≥3 archivos o >80 líneas<br/>notify_on_complete=true"]
    I -->|"Nivel 3"| M{"¿cuota_antigravity<br/>_usada > 80%?"}
    M -->|"Sí ⚠️"| N["✋ Alerta + pedir<br/>confirmación al Comandante"]
    N --> O["🎯 antigravity-cli (2.º plano)<br/>gemini-4-carbon-high /<br/>claude-opus-5-5 / etc.<br/>Arquitectura crítica, UI/UX, WhitePaper"]
    M -->|"No ✅"| O
    I -->|"Nivel 4"| P["🎨 visual_gen.py<br/>Mermaid → PNG (1920px, scale 2)<br/>+ PDF (A4) en .agents/artifacts/"]
    J --> Q["🚀 FASE 2: Ejecución<br/>P2: Handoff 5 campos<br/>P3: umbral delegación<br/>P5: adaptar entorno<br/>P11: preflight ya validado"]
    K --> Q
    L --> R["📥 Auditar resultado<br/>git diff --stat +<br/>comando de verificación"]
    O --> R
    P --> Q
    R --> Q
    Q --> S{"¿Falta contexto?"}
    S -->|"Sí"| T["📦 P8: La Caja Negra<br/>STATUS → CHANGELOG →<br/>git log → package.json/pyproject"]
    T --> Q
    S -->|"No"| U["✅ FASE 3: Cierre<br/>P7: Gate de Verificación<br/>typecheck + lint + tests en verde"]
    U --> V{"¿Todo en verde?"}
    V -->|"No ❌"| W["🔄 No cerrar<br/>Corregir o revertir"]
    W --> Q
    V -->|"Sí ✅"| X["📝 P4: Actualizar STATUS.md<br/>+ cuota_antigravity_usada<br/>Archivar últimas 5 tareas → CHANGELOG.md"]
    X --> Y["💡 P6: Registrar ideas en IDEAS.md<br/>Sincronizar hitos → docs/whitepaper/"]
    Y --> Z["🎨 P9+/N4: Si aplica, autogenerar<br/>artefacto visual (Mermaid → PNG/PDF)"]
    Z --> AA["📤 Entregar handoff de 5 campos<br/>[SKILL REQUERIDA]<br/>[OBJETIVO ATÓMICO]<br/>[RUTAS PERMITIDAS]<br/>[CONTRATO Y RESTRICCIONES]<br/>[COMANDO DE VERIFICACIÓN]"]
    AA --> AB["🏁 Tarea cerrada"]

    style A fill:#e1f5fe
    style AB fill:#c8e6c9
    style G fill:#ffcdd2
    style W fill:#ffcdd2
    style N fill:#fff9c4
    style E fill:#fff3e0
    style K fill:#e8f5e9
    style L fill:#e3f2fd
    style O fill:#f3e5f5
    style P fill:#fce4ec
```

## Pirámide de 5 Niveles (vista lateral)

```mermaid
flowchart BT
    N0["🔧 NIVEL 0 — Pre-flight<br/>preflight_check.sh<br/>0 tokens · SIEMPRE PRIMERO"] --> N1["🧠 NIVEL 1 — Motor Nativo<br/>nemotron / mistral / qwen local<br/>$0 · ~60% del trabajo"]
    N1 --> N2["📦 NIVEL 2 — OpenCode CLI<br/>deepseek-v4.1-flash-free<br/>$0 · ≥3 archivos / >80 líneas"]
    N2 --> N3["🎯 NIVEL 3 — Antigravity CLI<br/>gemini-4-carbon-high / claude-opus<br/>Cuota · verificar >80% antes"]
    N3 --> N4["🎨 NIVEL 4 — Artefactos Visuales<br/>visual_gen.py: Mermaid → PNG/PDF<br/>$0 · automático si aplica"]

    style N0 fill:#fff3e0,stroke:#e65100
    style N1 fill:#e8f5e9,stroke:#2e7d32
    style N2 fill:#e3f2fd,stroke:#1565c0
    style N3 fill:#f3e5f5,stroke:#6a1b9a
    style N4 fill:#fce4ec,stroke:#c2185b
```

## Flujo de delegación con Handoff de 5 campos (P2 + P11)

```mermaid
sequenceDiagram
    participant C as Comandante
    participant H as Hermes (Nivel 1)
    participant PF as preflight_check.sh
    participant OC as opencode-cli (Nivel 2)
    participant AG as antigravity-cli (Nivel 3)

    C->>H: Pedido en lenguaje natural
    H->>H: intent_classify.py → nivel/skill
    H->>PF: Ejecuta preflight (P11)
    PF-->>H: exit 0 ✅ [PREFLIGHT_REPORT]
    alt Nivel 2 (macro-tarea mecánica)
        H->>OC: [SKILL REQUERIDA] opencode-cli<br/>[OBJETIVO ATÓMICO] ...<br/>[RUTAS PERMITIDAS] ...<br/>[CONTRATO Y RESTRICCIONES] ...<br/>[COMANDO DE VERIFICACIÓN] ...<br/>[PREFLIGHT_REPORT] adjunto
        OC-->>H: Resultado en 2.º plano (notify_on_complete)
        H->>H: Audita con git diff --stat + comando verificación
    else Nivel 3 (fuerza especial)
        H->>H: quota_tracker.py check (>80%?)
        H->>AG: Handoff 5 campos + preflight report
        AG-->>H: Resultado en 2.º plano
        H->>H: quota_tracker.py add modelo tokens
        H->>H: Audita resultado
    end
    H->>H: P7 gate: typecheck/lint/tests en verde
    H->>C: Handoff de cierre + STATUS.md actualizado
```

## Migración segura v2.0 → v2.1 (P12)

```mermaid
flowchart LR
    A["Proyecto existente<br/>con STATUS.md / AGENTS.md"] --> B{"c-ghost-seed detecta<br/>archivos preexistentes?"}
    B -->|"Sí"| C["🚫 NO usar --force"]
    C --> D["✅ Usar --migrate"]
    D --> E["Diff 3-vías:<br/>plantilla v2.1 vs actual vs proyecto"]
    E --> F["Scripts nuevos → .agents/scripts/"]
    E --> G["Memoria viva preservada:<br/>STATUS, IDEAS, CHANGELOG,<br/>.hermes.md, AGENTS.md"]
    F --> H["Comandante revisa diffs<br/>y decide merge manual"]
    G --> H

    style C fill:#ffcdd2
    style D fill:#c8e6c9
    style G fill:#c8e6c9
```