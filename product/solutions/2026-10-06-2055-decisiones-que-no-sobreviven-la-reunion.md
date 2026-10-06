---
opportunity: decisiones-que-no-sobreviven-la-reunion
status: testing-several
chosen: cierre-de-reunion, decisiones-extraidas-ia
tests:
---

# Soluciones para: lo decidido en la reunión no sobrevive hasta la ejecución

## Qué dice hoy la evidencia

- **El problema se sostiene con evidencia real.** Los 10 entrevistados tienen un caso reciente de una decisión ejecutada distinto o no ejecutada, casi siempre con costo (`real`, `product/insights/2026-09-29-2100-entrevistas-colaboracion-en-vivo-fuera-de-teams.md`). En la última reunión, lo decidido no quedó en ningún lado en el 24% de los casos y quedó en un chat fuera de Teams en el 23% (`survey`, n=182, `product/insights/2026-09-29-2040-colaboracion-en-vivo-fuera-de-teams.md`).
- **Creencia 8 (el resumen de IA no lo resuelve): sobrevivió al primer filtro.** Quienes usan el resumen de IA pierden más decisiones, no menos: 65% vs. 40%, y 56% vs. 46% reclasificando (`survey`, correlacional, `product/insights/2026-10-06-2100-cruce-recap-ia-decisiones.md`). Sin anotación: una encuesta autoseleccionada no confirma.
- **Abierto:** la viabilidad (creencias 9 y 6) no tiene evidencia. Toda la evidencia disponible es **sobre el dolor**: nadie reaccionó todavía a ninguna solución.

## Punto de comparación: lo que hacen hoy

El líder reescribe lo decidido a mano después de la reunión, entre 10 y 60 minutos ("nadie más lo hace": Tomás, Javier, Valeria), y lo reparte por correo, chat o Jira (`real`, insight 1 de entrevistas). Quien tiene el recap de Copilot lo corrige a mano (Paula 10 min, Javier 30 min) o lo abandona (Martina) (`real`, insight 2). En el 24% de los casos nadie registra nada (`survey`, Q9). Algunos líderes intentan cerrar la reunión de palabra, "medio a mano y a veces se me va" (Sofía, `real`).

## Alternativas

### A1. Cierre de reunión (`cierre-de-reunion`)
Un ritual de dos minutos antes de colgar: el grupo confirma en voz alta qué se decidió, quién lo hace y para cuándo, sobre una plantilla de tres columnas en las notas de reunión que Teams ya tiene. Ataca el **cierre que falta**, el mecanismo central del insight 1. No es software nuevo y es lo más chico que podría funcionar. Es para [[paulina-achondo]] y [[camila-ferreyra]] (primarias). Reemplaza la reescritura posterior del líder.

### A2. Decisiones extraídas por IA, confirmadas por personas (`decisiones-extraidas-ia`)
Durante la reunión, la IA arma una lista que separa **decisión, idea y tarea**, propone responsable y fecha y, cuando puede, se apoya en el estado del artefacto (votos, tickets). Al cierre, el líder o el grupo confirma antes de publicar. Ataca las fallas del recap actual (insight 2: pone todo al mismo nivel, no asigna responsable, no ve el artefacto). Es para Paulina y Camila (primarias); [[ricardo-melnick]] (secundaria) recibe una lista confiable. Reemplaza el recap de Copilot corregido a mano y la reescritura del líder.

### A3. Lo decidido viaja a donde vive el trabajo (`decision-al-sistema`)
Cada decisión confirmada se escribe en el ticket, el PRD o el canal donde se ejecuta, con el responsable como asignado. Ataca la decisión que termina en un chat fuera de Teams, que es la que más explica la diferencia del cruce (37% vs. 18%). Es para Camila (primaria), que hoy pasa todo a Jira. Reemplaza el copiado manual a Jira y Confluence.

### A4. Continuidad por serie (`continuidad-por-serie`)
Decisiones, notas y pizarra quedan atadas a la serie de reuniones o al canal, no a una reunión puntual, y lo pendiente reaparece al inicio de la siguiente. Ataca la pérdida entre sesiones (insight 3 de entrevistas: 6 de 10 perdieron un artefacto de Teams al reprogramar). Es para Camila y Paulina (primarias). Reemplaza el tablero único de Miro con un frame por sesión y las capturas pegadas en Confluence (Lucía). *Junta dos ideas candidatas del brief que funcionan igual: anclar a la serie y retomar lo pendiente.*

## Comparación

| Alternativa | Deseable | Factible | Viable (upgrade a Max) | Creencia más riesgosa |
|---|---|---|---|---|
| A1 `cierre-de-reunion` | `mixed`: pain evidenced, relief not tested (`real`, 10/10). Señal en contra: el cierre informal ya se intenta y se escapa (Sofía), y moderar y escribir a la vez cuesta (Lucía) (`real`) | `strong`: usa las notas de reunión existentes (encuesta Q10, `survey`); falta confirmar que estén disponibles en cada cuenta | `weak` (`assumption`): un ritual con plantilla no es algo por lo que se pague Max | Los Team Leads sostienen el cierre en la mayoría de sus reuniones grandes durante 4 semanas, **y** en esas reuniones bajan las decisiones ejecutadas distinto |
| A2 `decisiones-extraidas-ia` | `mixed`: pain evidenced, relief not tested. El sustituto cercano (recap de Copilot) falla por las razones exactas que A2 ataca (6/6, `real`), pero los usuarios del recap pierden más (`survey`): eso no prueba que una versión confirmada funcione | `to check with tech`. Microsoft ya construye algo vecino (Facilitator, `secondary`); quedan abiertos externos y celular | `unknown`: compite con Copilot (USD 18–30, `secondary`) y depende de la creencia 9, sin evidencia | Una lista de decisiones propuesta por IA la confirma el grupo en ≤2 min con pocas correcciones, **y se lee**, a diferencia del recap |
| A3 `decision-al-sistema` | `mixed`, con señal en contra de un sustituto cercano: el recap pegado en el ticket no lo leyó nadie (Martina) y la decisión en el PRD se perdió en un comentario resuelto (Sofía) (`real`) | `to check with tech`. Integraciones con Jira y Confluence que autoriza TI (restricción del brief) | `unknown` (`assumption`) | Cuando la decisión llega al ticket con responsable asignado, se ejecuta como se decidió: la pérdida es porque no llega, no porque llegue y no se lea |
| A4 `continuidad-por-serie` | `mixed`. Es la única con uso real de un sustituto (Miro "por la continuidad", Tomás y Javier, `real`), pero varios costos ocurren antes de la siguiente reunión (Diego a los 2 días, Andrés a los 4) | `to check with tech` | `weak` (`assumption`): parece un arreglo del producto base, difícil de cobrar | La mayoría de las decisiones perdidas se detectarían al reaparecer en la siguiente reunión de la serie, antes de que el costo ocurra |

Toda la columna de viabilidad está débil o desconocida: ninguna alternativa tiene hoy un camino claro al upgrade a Max. Por eso la creencia 9 se resuelve en paralelo con las pruebas.

## Decisión

Se eligen para probar **A1 y A2 en paralelo** (`testing-several`). Lo decidió Marcelo el 2026-10-06, en línea con la recomendación:
- **A1 es la prueba más barata del mecanismo central:** confirmar antes de colgar. Si un cierre manual no reduce la pérdida, automatizarlo tampoco lo hará.
- **A2 es la única alternativa con un camino posible a Max** y ataca exactamente las fallas que los usuarios ven en el recap. Su riesgo propio es distinto: precisión y lectura.

**Qué cambiaría la decisión:**
- Si TI responde "eso es Copilot" (creencia 9), A2 pierde viabilidad.
- Si los líderes no sostienen A1, eso refuerza A2: hace falta automatizar.
- Si el cierre confirmado no baja las pérdidas, se vuelve a investigación.

## Para probar

- **A1** — "Los Team Leads sostienen el cierre de ≤2 min en la mayoría de sus reuniones de más de 5 durante 4 semanas, y en esas reuniones bajan las decisiones ejecutadas distinto". Es la que la mata porque la evidencia ya muestra el cierre informal escapándose (Sofía). Si ni con el ritual explícito se sostiene o no mueve la pérdida, el mecanismo no alivia el dolor. Se diseña en `/design-solution-tests`.
- **A2** — "Una lista de decisiones propuesta por IA la confirma el grupo en ≤2 min con pocas correcciones, y se lee, a diferencia del recap". Es la que la mata porque el sustituto (el recap) ya existe y falla justo en precisión y lectura (insight 2; el recap que nadie leyó, R-025). Si la versión confirmada repite esas fallas, A2 es un recap más. Se diseña en `/design-solution-tests`.

## Propuesta de valor: A1 `cierre-de-reunion`

- **Dolor que alivia:** decisiones que cada uno entiende distinto y responsables que creen que lo hace el otro (Andrés, Lucía, Ricardo: `real`), más los 10–60 min de reescritura del líder.
- **Ganancia:** el grupo sale con la misma lista de qué, quién y cuándo. Lo dicho por todos queda visto por todos, incluidos los que no hablaron.
- **Reemplaza:** la reescritura posterior del líder y el correo de acuerdos que llega tarde (Diego: dos días). Por qué cambiarían: el costo se paga dentro de la reunión (2 min), no después en soledad.
- **Deliberadamente no:** no automatiza nada, no escribe en Jira, no resume la conversación ni ayuda a converger o votar.

## Propuesta de valor: A2 `decisiones-extraidas-ia`

- **Dolor que alivia:** el recap que pone todo al mismo nivel, convierte ideas en decisiones y no dice quién se comprometió (Paula, Javier, Lucía, Martina: `real`), y los 10–30 min de corrección manual.
- **Ganancia:** una lista corta de decisiones con responsable y fecha, confirmada antes de colgar, que el equipo puede tratar como fuente de verdad.
- **Reemplaza:** el recap de Copilot corregido a mano y la reescritura del líder. Por qué cambiarían: el recap ya se lee como verdad aunque esté mal (Javier, Paula); esta lista está confirmada.
- **Deliberadamente no:** no resume la conversación completa ni transcribe, no decide por el grupo (sin confirmación humana no se publica) y no reemplaza la gestión de tareas en Jira.

## Creencias

- `[opportunity: decisiones-que-no-sobreviven-la-reunion] [value]` Creencia 8 de `product/overview.md`, tal como está registrada.
- `[opportunity: decisiones-que-no-sobreviven-la-reunion] [viability]` Creencia 9 de `product/overview.md`, tal como está registrada.
- `[opportunity: colaboracion-en-vivo-fuera-de-teams] [viability]` Creencia 6 de `product/overview.md`, tal como está registrada.
- `[feature: cierre-de-reunion] [usability]` Los Team Leads del segmento sostienen un cierre confirmado de ≤2 min (qué, quién, cuándo) en la mayoría de sus reuniones de más de 5 durante 4 semanas, sin que se salte por falta de tiempo. *(propuesta)*
- `[feature: cierre-de-reunion] [value]` En las reuniones con cierre confirmado, la proporción de decisiones que en las 2 semanas siguientes se ejecutan distinto, tarde o no se ejecutan es menor que en las mismas series sin cierre. *(propuesta)*
- `[feature: decisiones-extraidas-ia] [value]` La lista de decisiones que propone la IA separa decisión de idea y asigna responsable con precisión suficiente para que el grupo la confirme en ≤2 min con correcciones menores. *(propuesta)*
- `[feature: decisiones-extraidas-ia] [value]` La lista confirmada la leen los participantes, incluidos los que no hablaron, a diferencia del recap actual. *(propuesta)*

## Descartadas o aparcadas

- **A3 `decision-al-sistema` — parked:** tiene una señal en contra de un sustituto cercano (la decisión estaba en el ticket o el PRD y aun así se perdió). Vuelve como complemento de A1 o A2 si las pruebas muestran que la lista confirmada se pierde por no llegar a donde se ejecuta.
- **A4 `continuidad-por-serie` — parked:** llega tarde para los costos que ocurren en días, y viabilidad débil. Vuelve si las pruebas muestran que las decisiones confirmadas se pierden *entre* reuniones de la serie. También como mejora del producto base, fuera de esta oportunidad.
- **A5 `votacion-nativa` — parked:** ataca otro problema (converger), que se dejó fuera al enmarcar la oportunidad, y tiene contrapunto fuerte (Paula, Ricardo: "con dieciséis personas no se puede decidir nada"). Vuelve si se enmarca una oportunidad sobre convergencia (insight 5 de entrevistas).

## Resultado
