---
status: framed
segment: Cuentas M365 Business Premium, 100+ licencias, sector tecnología, operación en 3+ países, facturación >USD 100M anuales. 12.400 cuentas · 2,1 M licencias. Las reuniones de más de 5 las convocan y conducen Team Leads y mandos medios.
personas: camila-ferreyra (primaria, sufre), paulina-achondo (primaria, sufre), ricardo-melnick (secundaria, sufre como receptor), nadia-espinoza (terciaria, no sufre; responde la viabilidad), tomas-iriarte (negativa, no sufre)
derived_from: product/opportunities/2026-09-16-0054-colaboracion-en-vivo-fuera-de-teams.md
evidence: product/insights/2026-09-29-2040-colaboracion-en-vivo-fuera-de-teams.md (survey) · product/insights/2026-09-29-2100-entrevistas-colaboracion-en-vivo-fuera-de-teams.md (real) · product/research/2026-09-16-0115-colaboracion-en-vivo-fuera-de-teams.md (secondary)
---

# Oportunidad: lo decidido en la reunión no sobrevive hasta la ejecución

En las cuentas de tecnología multipaís con Business Premium, lo que se decide en las reuniones de más de cinco personas se ejecuta distinto, tarde o no se ejecuta. Nadie confirma antes de colgar qué se decidió, quién lo hace y para cuándo, y que la decisión se sostenga depende de que el Team Lead la reescriba a mano después, entre 10 y 60 minutos por reunión. El dato que más falla es el responsable. Importa ahora porque es el único dolor que aparece en las diez entrevistas reales y el tema abierto más repetido de la encuesta (37%), y porque el recap de IA, que se presenta como la respuesta, se usa pero no se confía en él. Además, la oportunidad anterior (colaboración en vivo) perdió su creencia central.

> **Origen.** Llegó como "cerrar la reunión / recuperar lo acordado". "Cerrar la reunión" es una forma de solución (un ritual de cierre) y queda aparcada abajo como idea candidata. Este problema ya estaba en la agenda de la oportunidad [[2026-09-16-0054-colaboracion-en-vivo-fuera-de-teams]] como reenfoque: "si la creencia 1 cae, se reenfoca hacia recuperar lo acordado". La creencia 1 está `contradicted` desde el 2026-09-29.

## Segmento y personas

**Segmento:** el mismo de la oportunidad original. Toda la evidencia `real` y `survey` viene de ahí. Si el problema ocurre igual en otros rubros es una pregunta abierta, no un supuesto.

| Persona | Tipo | ¿Sufre el problema? |
|---|---|---|
| [[camila-ferreyra]] | primaria | **Sí.** Pasa los compromisos a Jira en 25–35 min por ceremonia y, si no lo hace ese día, "los acuerdos se diluyen" (`synthetic`) |
| [[paulina-achondo]] | primaria | **Sí, es su objetivo principal:** "si en esa hora no salimos con algo decidido y escrito, la perdí". Reconstruye el acuerdo en 30–40 min; las decisiones "acordadas" se caen dos semanas después (`synthetic`) |
| [[ricardo-melnick]] | secundaria | **Sí, como receptor:** "Necesito que quede claro qué decidimos y poder encontrarlo". No conduce, pero no confía en el acta y reenvía lo acordado con sus palabras |
| [[nadia-espinoza]] | terciaria | **No.** Es quien responde la creencia de viabilidad: decide si esto justifica pagar Max o si "eso es Copilot" |
| [[tomas-iriarte]] | negativa | **No.** Su trabajo vive en sus herramientas y su problema es el acceso como externo |

> **Persona faltante.** Quien **ejecuta** lo decidido sin haber hablado en la reunión, como el desarrollador que "se quedó con cara de no" (Martina) o la persona que objeta después en un café (Valeria). Ricardo la cubre a medias, pero él es senior y externo al equipo. Sugerencia: `/generate-personas` para cubrir ese hueco (no ejecutado).

## Señales

| Señal | Procedencia | Fuente |
|---|---|---|
| Los 10 entrevistados contaron un caso reciente de una decisión ejecutada distinto o no ejecutada, casi siempre con costo: cliente 4 días sin atención, 2 semanas de trabajo rehecho, entrega 2 semanas tarde, presupuesto de campaña gastado de más, fin de semana de guardia | `real` | entrevistas, insight 1 |
| El líder reescribe lo decidido entre 10 y 60 min por reunión; "nadie más lo hace" (Tomás, Javier, Valeria) | `real` | entrevistas, insight 1 |
| El dato que más falla es el responsable: en 3 casos cada uno creyó que lo hacía el otro (Andrés, Lucía, Ricardo) | `real` | entrevistas, insight 1 |
| Los 6 entrevistados que usan el recap de Copilot/Teams tienen una queja concreta: no separa decisión de idea, no asigna responsable, no ve el artefacto (votos, filtros, tickets). Dos lo corrigen a mano (10 y 30 min) y una lo abandonó. Se lee como fuente de verdad aunque esté mal | `real` | entrevistas, insight 2 |
| En la última reunión, lo decidido **no quedó registrado en ningún lado** en el 24% de los casos y quedó en un chat fuera de Teams en el 23% (n=182) | `survey` | encuesta Q9, muestra autoseleccionada |
| "Que lo decidido sobreviva" es el tema abierto más mencionado: 35 de 95 respuestas (37%), parejo entre canales y presente también entre los que no salen de Teams | `survey` | encuesta Q11 |
| 12% deja la decisión en el recap de IA (una opción que el cuestionario no ofrecía) y los verbatims son de desconfianza | `survey` | encuesta Q9 "Otro" |
| 36% usa el resumen o asistente de IA en algunas o en la mayoría de sus reuniones | `survey` | encuesta Q10 |
| Facilitator (Copilot) ya ofrece notas coeditables, tareas hacia Planner y documento Word. Requiere licencia Copilot, deja fuera a los externos y en móvil es solo lectura | `secondary` | research §2 |
| Los facilitadores con IA aumentaron un 22% el intercambio de información sin cambiar las decisiones: "AI currently works better for individuals than it does for teams" | `secondary` | research, Microsoft New Future of Work 2025 |
| Google Meet "Take notes for me" genera un Doc con "decisions, action items" | `secondary` | research |
| "Pierdo tiempo pasando lo que decidimos a un documento después" aparece entre los comentarios negativos post-reunión del segmento | `survey` | encuesta post-reunión, **n no declarado** |
| 5 respondentes (España, Colombia) solo pueden colaborar dentro de Teams por compliance; Lucía tarda meses en aprobar una herramienta externa | `survey` (direccional) + `real` | encuesta Q11/Q12 · entrevista Lucía |
| Camila pierde 25–35 min por ceremonia y Paulina 30–40 min por reunión reconstruyendo acuerdos. El rango real (10–60 min) los contiene | `synthetic` | personas |
| 3,1% de las cuentas del segmento subió de Premium a Max en 12 meses | `unverified` | declarado en sesión, fuente sin nombrar |

## Outcome de negocio

**Upgrade de Business Premium a Business Max** (USD 8 usuario/mes). Línea base del segmento: 3,1% de cuentas en 12 meses (`unverified`). Es el único escalón comercial registrado y Max se vende como "capacidades avanzadas de reuniones".

**Riesgo explícito:** Microsoft ya cobra la facilitación y captura con IA a través de Copilot (USD 18–30). Si TI ve este problema como "eso es Copilot", el outcome deja de ser Max. Eso es lo que prueba la creencia de viabilidad.

Secundario, no perseguido: el 3,6% del parque que baja de plan o no renueva.

## Restricciones

Hechos que acotan cualquier solución futura. No son decisiones sobre ella.

- TI contrata y despliega; el usuario final no instala nada. Toda solución llega por el tenant.
- Nadia (TI) autoriza o bloquea integraciones de terceros y le inquieta que el trabajo viva fuera de su perímetro.
- **El trabajo y las decisiones viven fuera de Teams:** en el 66% de los casos el artefacto es Jira, Docs, Confluence o un dashboard que ya existía. Una decisión que no llega ahí no llega a donde se ejecuta.
- **Facilitator y el recap requieren licencia Copilot,** dejan fuera a los externos y en móvil son solo lectura. Desde julio de 2026 se pueden apagar en plena reunión.
- En algunas cuentas (UE/EEE, regulados), compliance impide usar herramientas externas con datos de clientes: lo nativo es la única opción.
- Operación en 3+ países: husos horarios y probablemente residencia de datos.
- Participantes desde el celular y con alfabetización técnica baja (Ricardo).
- El escalón comercial existente es Business Max a USD 8 usuario/mes. No hay otro.
- La vía de entrada de cualquier experimento es un piloto acotado con un área voluntaria.

## Creencias

Referenciadas desde `product/overview.md`, el registro único.

**Nuevas** (registradas como creencias 8 y 9 de `product/overview.md` el 2026-10-06):
- `[opportunity: decisiones-que-no-sobreviven-la-reunion] [value]` En las reuniones de más de 5 del segmento donde se usó el resumen o Facilitator de Copilot, la proporción de decisiones que no quedan registradas o se ejecutan distinto no es menor que donde no se usó: el recap de IA no resuelve el problema.
- `[opportunity: decisiones-que-no-sobreviven-la-reunion] [viability]` En las cuentas del segmento, quien decide el plan (TI) aceptaría "que las decisiones de reunión queden con responsable y se cumplan" como motivo para pagar Business Max, y no lo vería como algo ya cubierto, o por cubrir, con Copilot.

**Existentes que esta oportunidad usa:**
- Creencia 6 `[opportunity: colaboracion-en-vivo-fuera-de-teams] [viability]`: el upgrade a Max lo inicia o justifica un mando medio con una necesidad concreta de reunión. Es el mismo mecanismo de compra y se referencia tal como está.
- Creencia 4 `[product] [value]`: el Team Lead percibe la colaboración en la reunión como un problema propio. Está relacionada: la mitad de los entrevistados dice que "la herramienta no es mi problema", pero los diez reconocen este dolor.

## Agenda de investigación

| Creencia | Instrumento | Decisión que desbloquea | Plazo |
|---|---|---|---|
| value (nueva) | **Datos que ya tenemos.** Cruce en el CSV de la encuesta: Q10 (uso del resumen de IA) × Q9 (no quedó registrado / chat fuera de Teams), n=182, más los verbatims de quienes usan IA | Si quienes usan el recap pierden claramente menos, la oportunidad se acota al segmento sin Copilot o se descarta | **Hecho 2026-10-06:** no pierden menos (65% vs. 40%; 56% vs. 46% reclasificando). La regla no se activa. Ver `product/insights/2026-10-06-2100-cruce-recap-ia-decisiones.md` |
| value (nueva) | **Datos propios.** Penetración de licencias Copilot en el segmento y telemetría de reuniones con recap/Facilitator × tareas de Planner creadas o tickets enlazados editados en las 48 h siguientes | Dimensiona cuánto del segmento podría tener el problema "resuelto" y si el recap genera acciones o solo texto | 2 sem |
| value (nueva) | `/design-interview` ronda 2 (6–8), reclutada del opt-in entre quienes usan el resumen de IA (R-153, R-099, R-109…) más los referidos que conducen distinto (Natalia, Carla, Mariana) | El *por qué* del cruce: ¿el recap falla por estructura, por ceguera al artefacto o porque nadie confirma? | 3 sem |
| value (prevalencia, opcional) | Estudio de diario de 2 semanas con 15–20 Team Leads, siguiendo cada decisión hasta su ejecución | Solo si el cruce no concluye: pasa de recurrencia (10/10) a prevalencia | 5 sem |
| viability (nueva) | 6–8 conversaciones con TI o compradores del segmento (tipo Nadia): ¿esto justifica Max o "eso es Copilot"? | Si TI lo asigna a Copilot, el outcome deja de ser Max y la oportunidad se replantea comercialmente | 4 sem |
| viability (6) | Revisión de notas de venta de las ~384 cuentas que subieron a Max, más 6–8 entrevistas con quien empujó la conversación (heredada de la oportunidad original, sin empezar) | Si el upgrade lo decide TI sola, el segmento se rediseña hacia Nadia | 4 sem |
| abierta | `/research-market` acotado: captura de decisiones y acciones en herramientas de reunión (Fellow, Read.ai, Otter, Meet/Gemini) y su monetización | Acota la agenda y muestra si el mercado separa "resumen" de "decisión con responsable" | 1 sem, en paralelo |

## Ideas candidatas (no evaluadas)

Aparcadas durante el encuadre. Son el punto de partida de `/explore-solutions`, no una lista corta.

- "Cerrar la reunión": confirmar con el grupo qué se decidió, quién lo hace y para cuándo antes de colgar. Es la formulación con que llegó la oportunidad. → A1 `cierre-de-reunion` — **chosen** (para probar), ver `product/solutions/2026-10-06-2055-decisiones-que-no-sobreviven-la-reunion.md`
- Extraer decisiones tipificadas (decisión / idea / tarea) con responsable y fecha, con confirmación humana antes de publicarlas (insight 2 de entrevistas). → A2 `decisiones-extraidas-ia` — **chosen** (para probar), ver `product/solutions/2026-10-06-2055-decisiones-que-no-sobreviven-la-reunion.md`
- Escribir lo decidido de vuelta donde vive el trabajo: el ticket, el PRD, el canal (Martina). → A3 `decision-al-sistema` — **parked**, ver `product/solutions/2026-10-06-2055-decisiones-que-no-sobreviven-la-reunion.md`
- Retomar las decisiones pendientes al inicio de la siguiente reunión de la serie (insight 1 de la encuesta). → A4 `continuidad-por-serie` — **parked**, ver `product/solutions/2026-10-06-2055-decisiones-que-no-sobreviven-la-reunion.md`
- Anclar notas y pizarra a la serie o al canal, y no a una instancia de reunión (insight 3 de entrevistas). → A4 `continuidad-por-serie` — **parked**, ver `product/solutions/2026-10-06-2055-decisiones-que-no-sobreviven-la-reunion.md`
- Votación nativa liviana con el resultado pegado a la decisión (insight 5 de entrevistas). → A5 `votacion-nativa` — **parked**, ver `product/solutions/2026-10-06-2055-decisiones-que-no-sobreviven-la-reunion.md`
