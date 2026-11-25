#!/usr/bin/env python3
"""Inicializa el cerebro C://GHOST v2.1 en un proyecto nuevo o migra uno existente.

Solo usa la biblioteca estándar. Crea los archivos de gobernanza y memoria
a partir de las plantillas de esta skill, sin tocar nada fuera de --dir.
"""

import argparse
import sys
from datetime import date
from pathlib import Path
import difflib

TEMPLATES_DIR = Path(__file__).resolve().parent.parent / "templates"
PILLARS = ("Core Domain", "Experience", "Platform")
BRAIN_VERSION = "v2.1.0"


def render(text, values):
    """Sustituye los marcadores {{CLAVE}} por su valor."""
    for key, value in values.items():
        text = text.replace("{{" + key + "}}", str(value))
    return text


def clamp_description(text, limit=60):
    """Normaliza una descripción de skill a una frase de máximo 60 caracteres."""
    clean = " ".join(text.split())
    if len(clean) <= limit:
        return clean if clean.endswith(".") else clean + "."
    cut = clean[: limit - 1]
    if " " in cut:
        cut = cut[: cut.rfind(" ")]
    return cut.rstrip(" ,;:-.") + "."


def whitepaper(project, org, stack, today):
    """Documento fundacional generado sin plantilla externa."""
    return (
        f"# {project} — Whitepaper\n\n"
        f"Organización: {org}\n"
        f"Stack: {stack}\n"
        f"Fecha: {today}\n\n"
        "## Propósito\n\n"
        f"Explicar el problema, la solución y el fundamento técnico de {project} "
        "en un documento que sobreviva a las sesiones de trabajo.\n\n"
        "## Estructura sugerida\n\n"
        "1. Problema: qué duele y a quién.\n"
        "2. Propuesta: qué hace el producto y qué no hace.\n"
        "3. Arquitectura: pilares, límites y decisiones irreversibles.\n"
        "4. Evidencia: métricas, pruebas y resultados observados.\n"
        "5. Riesgos: qué puede fallar y cómo se mitiga.\n"
        "6. Roadmap: hitos en `CHANGELOG.md` y deuda visible en `IDEAS.md`.\n\n"
        "## Estado\n\n"
        "Borrador inicial creado por la semilla C://GHOST v2.1. "
        "Completar antes del primer hito de producto.\n"
    )


def preflight_check_script():
    """Genera preflight_check.sh"""
    return '''#!/usr/bin/env bash
# preflight_check.sh — Validación obligatoria antes de cualquier delegación (Protocolo 11)
# Exit 0 = verde, Exit 1 = errores bloqueantes

set -euo pipefail

PROJECT_ROOT="${1:-$(git rev-parse --show-toplevel 2>/dev/null || pwd)}"
cd "$PROJECT_ROOT"

echo "=== C://GHOST v2.1 Pre-flight Check ==="
echo "Directorio: $PROJECT_ROOT"
echo ""

ERRORS=0

# 1. Git status
echo "[1/6] Git diff --stat"
git diff --stat 2>/dev/null || echo "  (no git repo o sin cambios)"

# 2. Linters
echo "[2/6] Linters"
if command -v ruff >/dev/null 2>&1; then
    ruff check . --quiet 2>&1 | head -20 || ((ERRORS++))
else
    echo "  ruff no instalado (opcional)"
fi
if command -v eslint >/dev/null 2>&1; then
    eslint . --quiet 2>&1 | head -20 || ((ERRORS++))
else
    echo "  eslint no instalado (opcional)"
fi

# 3. Typecheck
echo "[3/6] Typecheck"
if command -v tsc >/dev/null 2>&1 && [ -f tsconfig.json ]; then
    tsc --noEmit 2>&1 | head -20 || ((ERRORS++))
else
    echo "  tsc no disponible o sin tsconfig.json"
fi
if command -v mypy >/dev/null 2>&1 && [ -f pyproject.toml ]; then
    mypy . --quiet 2>&1 | head -20 || ((ERRORS++))
else
    echo "  mypy no disponible o sin pyproject.toml"
fi

# 4. Test discovery
echo "[4/6] Test discovery"
if command -v pytest >/dev/null 2>&1; then
    pytest --collect-only -q 2>&1 | tail -5
else
    echo "  pytest no instalado"
fi
if command -v vitest >/dev/null 2>&1; then
    vitest --list 2>&1 | tail -5
else
    echo "  vitest no instalado"
fi

# 5. STATUS.md validation
echo "[5/6] STATUS.md validation"
if [ -f STATUS.md ]; then
    LINES=$(wc -l < STATUS.md)
    if [ "$LINES" -gt 100 ]; then
        echo "  ⚠ STATUS.md tiene $LINES líneas (máx 100)"
        ((ERRORS++))
    else
        echo "  ✓ STATUS.md: $LINES/100 líneas"
    fi
    # Check cuota_antigravity_usada
    if grep -q "cuota_antigravity_usada" STATUS.md; then
        echo "  ✓ cuota_antigravity_usada presente"
    else
        echo "  ⚠ cuota_antigravity_usada NO encontrada en STATUS.md"
    fi
else
    echo "  ✗ STATUS.md no encontrado"
    ((ERRORS++))
fi

# 6. Brain version
echo "[6/6] Brain version"
if [ -f .hermes.md ]; then
    VER=$(grep -E "^version:" .hermes.md | head -1 | awk '{print $2}')
    echo "  .hermes.md version: ${VER:-'no declarada'}"
else
    echo "  ✗ .hermes.md no encontrado"
    ((ERRORS++))
fi

echo ""
if [ $ERRORS -eq 0 ]; then
    echo "✅ Pre-flight PASSED — Listo para delegar"
    exit 0
else
    echo "❌ Pre-flight FAILED — $ERRORS error(es) bloqueante(s)"
    exit 1
fi
'''


def intent_classify_script():
    """Genera intent_classify.py"""
    return '''#!/usr/bin/env python3
"""Clasificador de intención embebido (Pre-P1) — C://GHOST v2.1

Devuelve JSON:
{
  "tipo": "Consulta|Exploración|Arquitectura|Macro-Construcción",
  "nivel_recomendado": 0|1|2|3|4,
  "skill": "none|opencode-cli|antigravity-cli|c-ghost-seed",
  "confianza": 0.0-1.0,
  "requiere_preflight": true|false
}
"""

import sys
import json
import re
from pathlib import Path

# Palabras clave por tipo
KEYWORDS = {
    "Consulta": [
        "qué", "cuál", "cómo", "dime", "explícame", "lista", "muestra",
        "ver", "verificar", "comprobar", "estado", "status"
    ],
    "Exploración": [
        "explora", "investiga", "analiza", "audita", "revisa", "busca",
        "encuentra", "descubre", "examina", "inspecciona"
    ],
    "Arquitectura": [
        "arquitectura", "diseña", "diseño", "estructura", "patrón",
        "decide", "decisión", "adr", "trade-off", "escalabilidad",
        "zero-trust", "seguridad", "modelo de datos"
    ],
    "Macro-Construcción": [
        "crea", "genera", "scaffolding", "boilerplate", "migra",
        "refactor", "test", "tests", "implementa", "construye",
        "desarrolla", "escribe código", "nuevo módulo", "nueva feature"
    ]
}

SKILL_HINTS = {
    "opencode-cli": ["scaffolding", "boilerplate", "test", "tests", "migra", "refactor", "multi-archivo"],
    "antigravity-cli": ["arquitectura", "zero-trust", "ui", "ux", "frontend", "whitepaper", "spec", "sql complejo", "algoritmo"],
    "c-ghost-seed": ["nuevo proyecto", "inicializa", "semilla", "bootstrap", "cerebro"]
}

NIVEL_HINTS = {
    0: ["lint", "typecheck", "verify", "comprobar"],
    1: ["chat", "pregunta", "respuesta", "análisis", "redacción"],
    2: ["scaffolding", "boilerplate", "test", "tests", "migra", "refactor", "≥3 archivos", ">80 líneas"],
    3: ["arquitectura", "zero-trust", "ui", "ux", "whitepaper", "spec", "sql complejo", "algoritmo", "crítico"],
    4: ["diagrama", "mermaid", "visual", "gráfico", "flujo", "arquitectura"]
}


def classify(text: str) -> dict:
    text_lower = text.lower()
    scores = {k: 0 for k in KEYWORDS}

    for tipo, kws in KEYWORDS.items():
        for kw in kws:
            if kw in text_lower:
                scores[tipo] += 1

    # Normalizar
    total = sum(scores.values()) or 1
    tipo = max(scores, key=scores.get)
    confianza = scores[tipo] / total

    # Nivel recomendado
    nivel_scores = {n: 0 for n in NIVEL_HINTS}
    for nivel, hints in NIVEL_HINTS.items():
        for h in hints:
            if h in text_lower:
                nivel_scores[nivel] += 1
    nivel = max(nivel_scores, key=nivel_scores.get)

    # Skill
    skill_scores = {s: 0 for s in SKILL_HINTS}
    for skill, hints in SKILL_HINTS.items():
        for h in hints:
            if h in text_lower:
                skill_scores[skill] += 1
    skill = max(skill_scores, key=skill_scores.get)
    if skill_scores[skill] == 0:
        skill = "none"

    # Preflight requerido para niveles 2, 3
    requiere_preflight = nivel >= 2

    return {
        "tipo": tipo,
        "nivel_recomendado": nivel,
        "skill": skill,
        "confianza": round(confianza, 2),
        "requiere_preflight": requiere_preflight
    }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        # Leer de stdin
        text = sys.stdin.read().strip()
    else:
        text = " ".join(sys.argv[1:])

    if not text:
        print(json.dumps({"error": "empty input"}, ensure_ascii=False))
        sys.exit(1)

    result = classify(text)
    print(json.dumps(result, ensure_ascii=False))
'''


def quota_tracker_script():
    """Genera quota_tracker.py"""
    return r'''#!/usr/bin/env python3
"""Rastreador de cuota Antigravity — C://GHOST v2.1

Lee/actualiza cuota_antigravity_usada en STATUS.md (tokens estimados por modelo).
"""

import sys
import re
from pathlib import Path
import json

# Estimación de tokens por modelo (input + output típico por tarea)
MODEL_TOKENS = {
    "gemini-4-carbon-high": 150000,
    "claude-sonnet-5-5-medium": 80000,
    "claude-opus-5-5-medium": 200000,
    "gemini-4-neon-medium": 120000,
    "gemini-4-argon-medium": 100000,
    "gemini-4-hydrogen-medium": 30000,
    "gpt-oss-120b-medium": 100000,
}

STATUS_PATH = Path("STATUS.md")


def read_quota():
    if not STATUS_PATH.exists():
        return 0
    content = STATUS_PATH.read_text(encoding="utf-8")
    m = re.search(r"cuota_antigravity_usada\s*[:\-]\s*(\d+)", content, re.IGNORECASE)
    return int(m.group(1)) if m else 0


def write_quota(tokens: int):
    if not STATUS_PATH.exists():
        return False
    content = STATUS_PATH.read_text(encoding="utf-8")
    if "cuota_antigravity_usada" in content:
        content = re.sub(
            r"cuota_antigravity_usada\s*[:\-]\s*\d+",
            f"cuota_antigravity_usada: {tokens}",
            content,
            flags=re.IGNORECASE
        )
    else:
        # Insertar después de la primera línea que contenga "Tarea Activa" o al final
        lines = content.splitlines()
        insert_idx = len(lines)
        for i, line in enumerate(lines):
            if "Tarea Activa" in line or "tarea activa" in line.lower():
                insert_idx = i + 1
                break
        lines.insert(insert_idx, f"cuota_antigravity_usada: {tokens}")
        content = "\n".join(lines)
    STATUS_PATH.write_text(content, encoding="utf-8")
    return True


def add_usage(model: str, custom_tokens: int = None):
    current = read_quota()
    tokens = custom_tokens or MODEL_TOKENS.get(model, 50000)
    new_total = current + tokens
    write_quota(new_total)
    return current, tokens, new_total


def check_threshold(threshold_pct=80):
    """Verifica si la cuota supera el umbral (requiere límite conocido)."""
    # Por ahora solo reporta; el límite real depende del plan Antigravity
    current = read_quota()
    return current, current > 0  # placeholder


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: quota_tracker.py <read|add|check> [modelo] [tokens]")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "read":
        print(read_quota())
    elif cmd == "add":
        if len(sys.argv) < 3:
            print("Modelo requerido para add")
            sys.exit(1)
        model = sys.argv[2]
        tokens = int(sys.argv[3]) if len(sys.argv) > 3 else None
        current, added, total = add_usage(model, tokens)
        print(f"Antes: {current} | Añadido: {added} | Total: {total}")
    elif cmd == "check":
        current, over = check_threshold()
        print(f"Cuota actual: {current} | Alerta: {'SÍ' if over else 'NO'}")
    else:
        print(f"Comando desconocido: {cmd}")
        sys.exit(1)
'''


def visual_gen_script():
    """Genera visual_gen.py"""
    return '''#!/usr/bin/env python3
"""Generador de artefactos visuales — C://GHOST v2.1

Dado un grafo Mermaid en stdin, exporta PNG (1920px ancho, scale 2) y PDF (A4)
a .agents/artifacts/. Requiere google-chrome o chromium en PATH.
"""

import sys
import tempfile
import subprocess
from pathlib import Path

ARTIFACTS_DIR = Path(".agents/artifacts")
ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)

def find_chrome():
    for cmd in ["google-chrome", "chromium", "chromium-browser", "/usr/sbin/google-chrome"]:
        if Path(cmd).exists() or subprocess.run(["which", cmd], capture_output=True).returncode == 0:
            return cmd
    return None


def render_mermaid(mermaid_code: str, base_name: str = "diagram"):
    chrome = find_chrome()
    if not chrome:
        print("❌ Chrome/Chromium no encontrado en PATH", file=sys.stderr)
        return False

    # HTML wrapper
    html = f"""<!DOCTYPE html>
<html><head><meta charset="UTF-8">
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
<style>
body {{ margin: 0; padding: 20px; background: white; }}
.mermaid {{ text-align: center; }}
</style>
</head><body>
<div class="mermaid">
{mermaid_code}
</div>
<script>mermaid.initialize({{startOnLoad:true,theme:'default',flowchart:{{useMaxWidth:true,htmlLabels:true,curve:'basis'}}}});</script>
</body></html>"""

    with tempfile.NamedTemporaryFile(mode="w", suffix=".html", delete=False) as f:
        f.write(html)
        html_path = f.name

    try:
        # PNG
        png_path = ARTIFACTS_DIR / f"{base_name}.png"
        subprocess.run([
            chrome, "--headless", "--disable-gpu",
            f"--screenshot={png_path}",
            "--window-size=1920,10800",
            "--device-scale-factor=2",
            f"file://{html_path}"
        ], check=True, capture_output=True, timeout=60)

        # PDF
        pdf_path = ARTIFACTS_DIR / f"{base_name}.pdf"
        subprocess.run([
            chrome, "--headless", "--disable-gpu",
            f"--print-to-pdf={pdf_path}",
            "--no-margins",
            f"file://{html_path}"
        ], check=True, capture_output=True, timeout=60)

        print(f"✅ Generado: {png_path} ({png_path.stat().st_size} bytes)")
        print(f"✅ Generado: {pdf_path} ({pdf_path.stat().st_size} bytes)")
        return True

    except subprocess.CalledProcessError as e:
        print(f"❌ Error generando artefactos: {e.stderr.decode()}", file=sys.stderr)
        return False
    except subprocess.TimeoutExpired:
        print("❌ Timeout generando artefactos", file=sys.stderr)
        return False
    finally:
        Path(html_path).unlink(missing_ok=True)


if __name__ == "__main__":
    mermaid_code = sys.stdin.read().strip()
    if not mermaid_code:
        print("Uso: echo 'mermaid code' | visual_gen.py [base_name]", file=sys.stderr)
        sys.exit(1)

    base_name = sys.argv[1] if len(sys.argv) > 1 else "diagram"
    success = render_mermaid(mermaid_code, base_name)
    sys.exit(0 if success else 1)
'''


def build_plan(project, org, stack, today, migrate=False):
    """Devuelve la lista de (ruta relativa, plantilla, valores) a generar."""
    common = {
        "PROJECT_NAME": project,
        "ORG": org,
        "STACK": stack,
        "DATE": today,
        "YEAR": today[:4],
        "BRAIN_VERSION": BRAIN_VERSION,
    }
    skill_values = dict(common)
    skill_values["SKILL_NAME"] = "01-core-domain"
    skill_values["PILAR"] = PILLARS[0]
    skill_values["SKILL_DESCRIPTION"] = clamp_description(
        f"Capacidades del pilar {PILLARS[0]} de {project}."
    )

    files = [
        (".hermes.md", ".hermes.template.md", common),
        ("AGENTS.md", "AGENTS.template.md", common),
        ("STATUS.md", "STATUS.template.md", common),
        ("IDEAS.md", "IDEAS.template.md", common),
        ("CHANGELOG.md", "CHANGELOG.template.md", common),
        (".agents/skills/01-core-domain/SKILL.md", "SKILL.template.md", skill_values),
        ("docs/whitepaper/README.md", None, common),
        # Nuevos scripts
        (".agents/scripts/preflight_check.sh", None, {"content": preflight_check_script()}),
        (".agents/scripts/intent_classify.py", None, {"content": intent_classify_script()}),
        (".agents/scripts/quota_tracker.py", None, {"content": quota_tracker_script()}),
        (".agents/scripts/visual_gen.py", None, {"content": visual_gen_script()}),
    ]

    if migrate:
        # En migración, no sobrescribir archivos de memoria vivos
        memory_files = {"STATUS.md", "IDEAS.md", "CHANGELOG.md", ".hermes.md", "AGENTS.md"}
        files = [(p, t, v) for (p, t, v) in files if p not in memory_files]

    return files


def migrate_existing(root: Path):
    """Genera diff de tres vías para archivos existentes."""
    print("\n=== MIGRACIÓN C://GHOST v2.1 ===")
    print("Analizando archivos existentes...\n")

    memory_files = ["STATUS.md", "IDEAS.md", "CHANGELOG.md", ".hermes.md", "AGENTS.md"]
    for mf in memory_files:
        target = root / mf
        if target.exists():
            print(f"  📄 {mf} existe — se preservará (usa --force para sobrescribir)")

    # Mostrar diff para .hermes.md si existe
    hermes = root / ".hermes.md"
    if hermes.exists():
        template = TEMPLATES_DIR / ".hermes.template.md"
        if template.exists():
            old = hermes.read_text(encoding="utf-8")
            new = render(template.read_text(encoding="utf-8"), {
                "PROJECT_NAME": "{{PROJECT_NAME}}",
                "ORG": "{{ORG}}",
                "STACK": "{{STACK}}",
                "DATE": "{{DATE}}",
                "YEAR": "{{YEAR}}",
                "BRAIN_VERSION": BRAIN_VERSION,
            })
            diff = list(difflib.unified_diff(
                old.splitlines(), new.splitlines(),
                fromfile=f"a/{mf}", tofile=f"b/{mf} (plantilla v2.1)", lineterm=""
            ))
            if diff:
                print(f"\n--- Diff .hermes.md (plantilla v2.1 vs actual) ---")
                for line in diff[:50]:
                    print(line)
                if len(diff) > 50:
                    print(f"... ({len(diff)} líneas totales)")

    print("\nSiguiente paso: revisa los diffs y decide qué migrar manualmente.")
    print("Los scripts nuevos (.agents/scripts/) SÍ se crearán/actualizarán.")


def main():
    parser = argparse.ArgumentParser(
        prog="init_c_ghost.py",
        description="Crea o migra el cerebro C://GHOST v2.1 en un proyecto.",
    )
    parser.add_argument("--dir", required=True, help="Directorio destino del proyecto.")
    parser.add_argument("--name", required=True, help="Nombre del proyecto.")
    parser.add_argument("--org", default="Personal", help="Organización responsable (default: Personal).")
    parser.add_argument("--stack", default="Por definir", help="Stack técnico (default: Por definir).")
    parser.add_argument("--force", action="store_true", help="Sobrescribe los archivos existentes.")
    parser.add_argument("--migrate", action="store_true", help="Modo migración: preserva memoria viva, muestra diffs.")

    args = parser.parse_args()

    project = args.name.strip()
    if not project:
        raise SystemExit("Error: --name no puede estar vacío.")
    org = args.org.strip() or "Personal"
    stack = args.stack.strip() or "Por definir"

    root = Path(args.dir).expanduser().resolve()
    if root.exists() and not root.is_dir():
        raise SystemExit(f"Error: {root} existe y no es un directorio.")
    root.mkdir(parents=True, exist_ok=True)

    if not TEMPLATES_DIR.is_dir():
        raise SystemExit(f"Error: no se encontró el directorio de plantillas: {TEMPLATES_DIR}")

    today = date.today().isoformat()

    if args.migrate:
        migrate_existing(root)

    results = []

    for rel_path, template_name, values in build_plan(project, org, stack, today, args.migrate):
        target = root / rel_path
        if target.exists() and not args.force:
            results.append(("omitido", rel_path))
            continue

        target.parent.mkdir(parents=True, exist_ok=True)

        if template_name is None:
            if "content" in values:
                content = values["content"]
            else:
                content = whitepaper(project, org, stack, today)
        else:
            source = TEMPLATES_DIR / template_name
            try:
                content = render(source.read_text(encoding="utf-8"), values)
            except FileNotFoundError:
                raise SystemExit(f"Error: falta la plantilla {source}")

        action = "sobrescrito" if target.exists() else "creado"
        target.write_text(content, encoding="utf-8")
        # Hacer ejecutables los scripts .sh
        if rel_path.endswith(".sh"):
            target.chmod(0o755)
        results.append((action, rel_path))

    created = sum(1 for action, _ in results if action == "creado")
    overwritten = sum(1 for action, _ in results if action == "sobrescrito")
    skipped = sum(1 for action, _ in results if action == "omitido")
    width = max(len(rel_path) for _, rel_path in results) if results else 0

    print(f"\nC://GHOST {BRAIN_VERSION} — semilla aplicada")
    print(f"Proyecto     : {project}")
    print(f"Organización : {org}")
    print(f"Stack        : {stack}")
    print(f"Directorio   : {root}")
    print("")
    for action, rel_path in results:
        print(f"  {action:<11} {rel_path:<{width}}")
    print("")
    print(f"Total: {len(results)} · creados: {created} · sobrescritos: {overwritten} · omitidos: {skipped}")

    if skipped and not args.migrate:
        print("Usa --force para reemplazar los archivos omitidos.")
    if args.migrate:
        print("Modo migración: archivos de memoria (STATUS.md, IDEAS.md, CHANGELOG.md, .hermes.md, AGENTS.md) preservados.")

    if not args.migrate:
        print("Siguiente paso: abre STATUS.md y define la Tarea Activa.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())