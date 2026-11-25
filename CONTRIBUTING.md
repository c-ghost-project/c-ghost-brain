# 🤝 Guía para Contribuyentes — `C://GHOST Brain`

Gracias por tu interés en mejorar y expandir la **Metodología C-GHOST**. Este proyecto se mantiene **abierto para uso personal, académico y comercial** bajo un marco claro de gobernanza que garantiza calidad, neutralidad técnica y atribución transparente.

---

## 1. Qué contribuciones son bienvenidas (Alcance)

### ✅ Muy bienvenidas
* **Nuevos adaptadores en `adapters/<ecosistema>/`:** Integraciones limpias para otros entornos de agentes (Cursor, Claude Code, Codex, Windsurf, Aider, Cline, Continue, etc.), acompañadas de su propio manual paso a paso en `docs/manuals/`.
* **Mejoras de seguridad *Zero-Trust*:** Nuevos patrones de protección de secretos y casos de prueba para `templates/hooks/pre-tool-guard.sh` y `stop-gate.sh`.
* **Portabilidad multiplataforma:** Mejoras para Windows (PowerShell nativo / WSL) y macOS sin agregar dependencias externas.
* **Traducciones y casos de estudio:** Traducción de manuales (`docs/manuals/en/`, `pt/`, etc.) y ejemplos reales anonimizados.

### ❌ Fuera de alcance (se rechazarán por diseño)
* Acoplar el núcleo raíz (`01_PROMPT_*`, `02_PROMPT_*`, `plant-seed.sh`, `templates/`) a una nube, lenguaje o gestor de tareas comercial específico.
* Introducir dependencias externas (`pip`, `npm`, binarios no estándar) en los scripts sembradores o hooks base.
* Eliminar o debilitar los protocolos fundamentales (ventana deslizante `≤ 100` líneas, jerarquía de escritura o bloqueo *Zero-Trust*).

---

## 2. Flujo de Trabajo y Firma Legal DCO (`Signed-off-by`)

1. Haz un **Fork** del repositorio y crea una rama descriptiva desde `main`:
   ```bash
   git checkout -b feat/adapter-cursor
   ```
2. Realiza commits atómicos siguiendo **Conventional Commits** (`feat(...)`, `fix(...)`, `docs(...)`, `test(...)`) y **firma cada commit con DCO (`-s`)**:
   ```bash
   git commit -s -m "feat(adapters): add Cursor adapter and step-by-step manual"
   ```
   > Al usar `-s` (`Signed-off-by: Tu Nombre <tu@email>`), certificas bajo el *Developer Certificate of Origin (DCO 1.1)* que tienes derecho legal sobre tu aporte y aceptas distribuirlo bajo **Apache 2.0** (código/scripts) y **CC BY-SA 4.0** (documentación/manuales).

---

## 3. Verificación Obligatoria Antes de Abrir un Pull Request

Tu PR debe pasar localmente (y pasará automáticamente en **GitHub Actions**):

```bash
# 1. Sintaxis de shell scripts y validez JSON
bash -n plant-seed.sh templates/hooks/*.sh
python3 -m json.tool templates/hooks.universal.json >/dev/null

# 2. Compilación AST del sembrador de Hermes (sin generar __pycache__)
PYTHONDONTWRITEBYTECODE=1 python3 -c "import ast; ast.parse(open('adapters/hermes/skills/c-ghost-seed/scripts/init_c_ghost.py').read())"

# 3. Cero rutas personales ni secretos hardcodeados
! grep -rniE "/home/|/Users/|C:\\\\Users|BEGIN PRIVATE KEY|sk-[a-zA-Z0-9]{20,}" . --exclude-dir=.git --exclude='*.png' --exclude='*.pdf'
```

---

## 4. Atribución y Política de Marca

* **Cómo citar en derivados o proyectos:** Conserva el archivo [`NOTICE`](./NOTICE) e incluye la atribución visible:  
  **`José Dugarte | Dugui - Metodología C-GHOST`** (o usa el botón **«Cite this repository»** generado por [`CITATION.cff`](./CITATION.cff)).
* **Forks y Marca:** Los forks son bienvenidos; si modificas sustancialmente la metodología o distribuyes un producto propio derivado, elige un nombre propio que no sugiera ser una distribución oficial de `C://GHOST` (Apache 2.0, Sección 6).
