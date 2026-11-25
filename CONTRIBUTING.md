# 🤝 Guía de Contribución — `C://GHOST Brain`

¡Las contribuciones de la comunidad son bienvenidas! Si deseas proponer un nuevo adaptador para otro ecosistema de agentes (Cursor, Claude Code, Codex, Windsurf, Aider, etc.), mejorar los scripts de seguridad *Zero-Trust* o enriquecer los manuales:

## Reglas de Oro para Pull Requests
1. **Neutralidad Estricta (Zero Lock-In):** El núcleo raíz (`01_PROMPT_*`, `02_PROMPT_*`, `plant-seed.sh`, `templates/`) debe permanecer **100% agnóstico** de proveedores cloud, lenguajes, gestores de tareas y rutas personales.
2. **Adaptadores Separados:** Cualquier integración específica de un motor de agentes debe vivir bajo `adapters/<nombre-del-motor>/` con su propio manual paso a paso.
3. **Cero Secretos ni PII:** Antes de abrir un PR, verifica que no existan rutas absolutas personales, claves API, tokens ni nombres de proyectos privados.
4. **Verificación Obligatoria:**
   ```bash
   bash -n plant-seed.sh templates/hooks/*.sh
   python3 -m json.tool templates/hooks.universal.json >/dev/null
   python3 -m py_compile adapters/hermes/skills/c-ghost-seed/scripts/init_c_ghost.py
   ```
5. **Licencia:** Al contribuir aceptas publicar código/scripts bajo **MIT** y documentación/manuales bajo **CC BY-SA 4.0** (ver [`LICENSE`](./LICENSE)).
