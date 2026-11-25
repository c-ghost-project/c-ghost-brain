# TUTORIAL PASO A PASO — Implementar C://GHOST v2.1

**Tiempo estimado:** 15-30 minutos para proyecto nuevo · 10 minutos para migrar uno existente
**Requisitos:** Python 3.8+, git, (opcional) Chrome/Chromium para visual_gen.py

---

## PARTE A — Proyecto NUEVO desde cero

### Paso 1: Verificar entorno

```bash
python3 --version   # debe ser ≥ 3.8
git --version
which google-chrome || which chromium   # opcional, para visual_gen.py
```

### Paso 2: Ejecutar la semilla

```bash
cd ~/.hermes/skills/software-development/c-ghost-seed

python3 scripts/init_c_ghost.py \
  --dir /ruta/a/tu-proyecto \
  --name "Mi Proyecto" \
  --org "Mi Organización" \
  --stack "Python 3.12 + FastAPI + PostgreSQL"
```

Salida esperada:

```
C://GHOST v2.1.0 — semilla aplicada
Proyecto     : Mi Proyecto
...
  creado       .hermes.md
  creado       AGENTS.md
  creado       STATUS.md
  creado       IDEAS.md
  creado       CHANGELOG.md
  creado       .agents/skills/01-core-domain/SKILL.md
  creado       docs/whitepaper/README.md
  creado       .agents/scripts/preflight_check.sh
  creado       .agents/scripts/intent_classify.py
  creado       .agents/scripts/quota_tracker.py
  creado       .agents/scripts/visual_gen.py

Total: 11 · creados: 11 · sobrescritos: 0 · omitidos: 0
Siguiente paso: abre STATUS.md y define la Tarea Activa.
```

### Paso 3: Verificar que todo se creó correctamente

```bash
cd /ruta/a/tu-proyecto
find . -type f | sort
echo "---"
wc -l STATUS.md   # debe ser ≤ 100
echo "---"
grep "cuota_antigravity_usada" STATUS.md   # debe existir
```

### Paso 4: Ejecutar el preflight por primera vez

```bash
chmod +x .agents/scripts/preflight_check.sh
./.agents/scripts/preflight_check.sh
```

Salida esperada (exit 0):

```
=== C://GHOST v2.1 Pre-flight Check ===
[1/6] Git diff --stat
[2/6] Linters
  ruff no instalado (opcional)
...
[5/6] STATUS.md validation
  ✓ STATUS.md: 67/100 líneas
  ✓ cuota_antigravity_usada presente
[6/6] Brain version
  .hermes.md version: v2.1.0

✅ Pre-flight PASSED — Listo para delegar
```

### Paso 5: Probar el clasificador de intención

```bash
echo "necesito crear los tests unitarios del módulo de usuarios, son como 5 archivos" | ./.agents/scripts/intent_classify.py
```

Salida esperada:

```json
{"tipo": "Macro-Construcción", "nivel_recomendado": 2, "skill": "opencode-cli", "confianza": 0.67, "requiere_preflight": true}
```

### Paso 6: Definir la Tarea Activa en STATUS.md

Edita `STATUS.md` y reemplaza la tabla de Tarea Activa:

```markdown
## Tarea Activa

| Campo | Valor |
|-------|-------|
| Objetivo | Implementar modelo de Usuario con validaciones |
| Pilar | Core Domain |
| Responsable | Guardián |
| Inicio | 2026-11-23 |
| Verificación | `pytest tests/test_user.py -v` |
| Rollback | `git checkout HEAD -- src/core/user.py` |
```

### Paso 7: Probar el generador visual

```bash
echo 'flowchart LR; A[Inicio] --> B[Fin]' | ./.agents/scripts/visual_gen.py mi-primer-diagrama
ls -la .agents/artifacts/
```

### Paso 8: Inicializar git y hacer el primer commit

```bash
git init
git add .
git commit -m "feat: inicializar proyecto con C://GHOST v2.1"
```

---

## PARTE B — MIGRAR un proyecto existente (v2.0 → v2.1)

### Paso 1: Respaldar primero (obligatorio)

```bash
cd /ruta/a/tu-proyecto-existente
cp STATUS.md STATUS.md.backup-v2.0
cp AGENTS.md AGENTS.md.backup-v2.0
cp .hermes.md .hermes.md.backup-v2.0
git add -A && git commit -m "chore: backup pre-migración a C://GHOST v2.1"
```

### Paso 2: Ejecutar en modo migración (NUNCA --force)

```bash
cd ~/.hermes/skills/software-development/c-ghost-seed

python3 scripts/init_c_ghost.py \
  --dir /ruta/a/tu-proyecto-existente \
  --name "Proyecto Existente" \
  --migrate
```

Salida esperada:

```
=== MIGRACIÓN C://GHOST v2.1 ===
Analizando archivos existentes...

  📄 STATUS.md existe — se preservará (usa --force para sobrescribir)
  📄 AGENTS.md existe — se preservará
  📄 .hermes.md existe — se preservará
  📄 IDEAS.md existe — se preservará
  📄 CHANGELOG.md existe — se preservará

--- Diff .hermes.md (plantilla v2.1 vs actual) ---
...

C://GHOST v2.1.0 — semilla aplicada
  creado       .agents/scripts/preflight_check.sh
  creado       .agents/scripts/intent_classify.py
  creado       .agents/scripts/quota_tracker.py
  creado       .agents/scripts/visual_gen.py
  omitido      .hermes.md
  omitido      AGENTS.md
  omitido      STATUS.md
  ...

Modo migración: archivos de memoria preservados.
```

### Paso 3: Revisar los diffs y migrar manualmente lo que quieras

```bash
cd /ruta/a/tu-proyecto-existente
# Ver qué cambió en la plantilla nueva
diff .hermes.md.backup-v2.0 <(python3 -c "
import sys; sys.path.insert(0, '~/.hermes/skills/software-development/c-ghost-seed/scripts')
from init_c_ghost import render, TEMPLATES_DIR
print(render((TEMPLATES_DIR / '.hermes.template.md').read_text(), {'PROJECT_NAME':'X','ORG':'Y','STACK':'Z','DATE':'2026-11-23','YEAR':'2026','BRAIN_VERSION':'v2.1.0'}))
")
```

### Paso 4: Añadir campos nuevos a STATUS.md

Edita manualmente `STATUS.md` y añade:

```markdown
- **cuota_antigravity_usada: 0**
```

En la sección "Estado Global".

### Paso 5: Actualizar .hermes.md con la versión

Añade al principio de `.hermes.md`:

```markdown
version: v2.1.0
```

### Paso 6: Verificar que el preflight funciona en el proyecto migrado

```bash
chmod +x .agents/scripts/preflight_check.sh
./.agents/scripts/preflight_check.sh
```

### Paso 7: Commit de la migración

```bash
git add -A
git commit -m "feat: migrar cerebro a C://GHOST v2.1 (P12 --migrate)"
```

---

## PARTE C — Uso diario del cerebro v2.1

### Cada vez que empieces una sesión:

```bash
# 1. Pre-flight SIEMPRE primero
./.agents/scripts/preflight_check.sh

# 2. Leer estado actual
cat STATUS.md | head -30
```

### Cada vez que recibas un pedido complejo:

```bash
# Clasificar antes de actuar
echo "el pedido del usuario" | ./.agents/scripts/intent_classify.py
```

### Antes de usar Antigravity (Nivel 3):

```bash
# Verificar cuota
./.agents/scripts/quota_tracker.py check

# Después de usarlo, registrar consumo
./.agents/scripts/quota_tracker.py add gemini-4-carbon-high
```

### Cuando una tarea genere arquitectura o flujo:

```bash
# Generar diagrama automático
echo 'flowchart TD; A-->B-->C' | ./.agents/scripts/visual_gen.py arquitectura-modulo-auth
# → genera .agents/artifacts/arquitectura-modulo-auth.png y .pdf
```

### Al cerrar una tarea:

1. Verificar que typecheck + lint + tests pasan (P7)
2. Actualizar `STATUS.md` (nueva Tarea Activa o archivar a CHANGELOG)
3. Actualizar `cuota_antigravity_usada` si se usó Nivel 3
4. Registrar ideas nuevas en `IDEAS.md`
5. Entregar handoff de 5 campos

---

## PARTE D — Solución de problemas comunes

| Problema | Solución |
|----------|----------|
| `preflight_check.sh` falla | Lee el output, corrige los errores reportados, vuelve a ejecutar |
| `intent_classify.py` da confianza < 0.75 | Normal — Hermes preguntará en lugar de asumir |
| `visual_gen.py` dice "Chrome no encontrado" | `sudo dnf install chromium` (Fedora) o instala google-chrome |
| `quota_tracker.py` no encuentra STATUS.md | Ejecútalo desde la raíz del proyecto, no desde otra carpeta |
| Migración sobrescribió algo sin querer | `git checkout HEAD~1 -- archivo` o restaura desde el backup `.backup-v2.0` |
| STATUS.md supera 100 líneas | Archiva las últimas 5 tareas completadas a CHANGELOG.md (P4) |

---

## Checklist final de verificación

```bash
# Ejecuta esto y todo debe dar ✅
cd /ruta/a/tu-proyecto

./.agents/scripts/preflight_check.sh && echo "✅ Preflight OK"
echo '"consulta simple"' | ./.agents/scripts/intent_classify.py | grep -q '"tipo"' && echo "✅ Clasificador OK"
./.agents/scripts/quota_tracker.py read && echo "✅ Quota tracker OK"
grep -q "version: v2.1.0" .hermes.md && echo "✅ Versión OK"
grep -q "cuota_antigravity_usada" STATUS.md && echo "✅ Cuota en STATUS OK"
ls .agents/scripts/*.sh .agents/scripts/*.py | wc -l | grep -q "4" && echo "✅ 4 scripts OK"
wc -l STATUS.md | awk '{if ($1 <= 100) print "✅ STATUS.md ≤ 100 líneas"; else print "❌ STATUS.md muy largo"}'