# Clave de respuesta — cómo se arma

Una clave por transcripción, para las 12 (las de ajuste también la necesitan para ajustar el prompt). Se arma **antes de correr el prompt sobre las reservadas**, y quienes la arman no ven ninguna salida de la IA ni de Copilot.

## Quiénes

- **El líder** de la serie y **la persona observadora** de T1, cada uno por su lado.
- En transcripciones sin persona observadora (pool de la encuesta), la reemplaza alguien del equipo que lee la transcripción completa. No puede ser quien ajusta el prompt.

## Qué es cada tipo (las definiciones son las mismas que usa el prompt)

| Tipo | Es… | Ejemplo |
|---|---|---|
| **decision** | Una elección que el grupo da por cerrada: desde ahí se actúa distinto. Puede tener o no tener responsable. | «Vamos con la opción B para el onboarding.» |
| **tarea** | Algo concreto que una persona se compromete a hacer, sin que se elija entre opciones. | «Yo le mando el acta a legal mañana.» |
| **idea** | Una propuesta, opinión o posibilidad que **no** se dio por cerrada. | «Podríamos probar sacar el paso 3.» |

**Responsable:** el código de quien quedó a cargo **según lo que se dijo en la reunión**, o `sin_responsable` si nadie lo tomó. No vale lo que el líder sabe que pasó después.
**Fecha:** la que se dijo («jueves», «15/10», «próximo sprint»), o `sin_fecha`.

## Pasos

1. Cada uno, **por separado**, recorre la transcripción y anota en `clave-respuesta.csv` cada ítem relevante con su tipo, responsable, fecha y el minuto donde aparece (`tipo_lider` o `tipo_observadora`, `responsable_lider` o `responsable_observadora`). En reuniones de T1 se parte de la lista de la observadora y de la confirmada en el cierre, y se completa con la transcripción.
2. **Se juntan las dos listas.** Si coinciden en tipo y responsable, se cierra el ítem con `tipo_final` y `responsable_final`.
3. **Si no coinciden, se discute.** Si llegan a acuerdo, se anota el acuerdo. Si **sigue el desacuerdo**, el ítem queda `tipo_final = excluido` y no cuenta para ninguna métrica (regla del diseño).
4. Para la fecha basta con que la anote uno de los dos, salvo que se contradigan. En ese caso, `fecha_final = excluida`.

Ritmo esperado: unos 20 minutos por reunión de una hora.

## Planilla

`clave-respuesta.csv`: una fila por ítem. La primera fila es un ejemplo: bórrala al empezar.
