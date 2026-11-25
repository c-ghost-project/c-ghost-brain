---
name: nombre-de-la-skill
description: Descripción concisa del dominio técnico de esta skill y cuándo debe cargarse automáticamente por divulgación progresiva.
---

# Skill: [Nombre de la Especialidad Técnica]

## 1. Disparadores Automáticos (Cuándo Invocarla)
- Invocar automáticamente al intervenir archivos de **[Pilar X / Módulo Y]**.
- Invocar cuando la instrucción involucre **[tecnologías clave, ej. JWT RS256, Cloudflare D1, AES-256-GCM, WordPress, Tailwind CSS]**.

## 2. Reglas de Oro (Inquebrantables)
1. **Compartimentación Física de Datos:** Usar exclusivamente la base de datos aislada del pilar correspondiente y vincular registros mediante `user_uuid`.
2. **Seguridad Zero-Trust:** Validar todas las entradas con esquemas estrictos (Zod / consultas parametrizadas). Prohibido exponer secretos en código.
3. **Coherencia Visual y Accesibilidad:** Soportar Modo Claro (predeterminado), Modo Oscuro y Modo Automático con contraste WCAG AA.

## 3. Contrato Técnico y Patrón de Referencia
```typescript
// Incluir aquí el contrato de interfaz o patrón base del módulo
export interface SovereignRecord {
  id: string;
  user_uuid: string;
  created_at: string;
}
```

## 4. Gate de Verificación (Protocolo 7)
Antes de cerrar la tarea en `STATUS.md`, verificar sin errores:
- `pnpm --filter <paquete> typecheck`
- `pnpm --filter <paquete> test`
