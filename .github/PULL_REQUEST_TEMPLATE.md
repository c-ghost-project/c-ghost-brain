## Resumen del Cambio
<!-- Explica en 2-3 líneas qué aporta o corrige este Pull Request -->

## Tipo de Contribución
- [ ] Nuevo adaptador de ecosistema (`adapters/<nombre>/`)
- [ ] Mejora al núcleo universal `v3.0` (`templates/`, `plant-seed.sh`, prompts)
- [ ] Mejora de seguridad *Zero-Trust* en hooks (`pre-tool-guard.sh` / `stop-gate.sh`)
- [ ] Mejora o traducción de manuales / documentación (`docs/`)
- [ ] Corrección de bug

## Checklist Obligatorio antes de Revisión
- [ ] Mis commits están firmados con DCO (`git commit -s` — `Signed-off-by`).
- [ ] No introduje dependencias externas (`pip`/`npm`) en los scripts sembradores ni hooks.
- [ ] El núcleo raíz permanece 100% agnóstico de nube, lenguaje y gestor de tareas.
- [ ] Verifiqué ausencia total de rutas locales personales (`/home/...`, `/Users/...`) y secretos.
- [ ] Ejecuté localmente las validaciones de `CONTRIBUTING.md` (y pasan en verde).
- [ ] Acepto publicar el código bajo **Apache 2.0** (conservando `NOTICE`) y la documentación bajo **CC BY-SA 4.0**.
