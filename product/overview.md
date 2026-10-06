# Microsoft Teams

mode: existing · commercial

Herramienta de comunicación y colaboración de Microsoft 365: chat, reuniones, llamadas y archivos, integrada con Word, Excel, PowerPoint y Outlook. En el mercado desde 2017, en producción con cientos de millones de usuarios activos mensuales. Se vende por licencia de usuario dentro de los planes de M365 y lo despliega el área de IT de cada organización, no el usuario final.

## Para quién

Organizaciones que ya usan Microsoft 365. IT contrata y despliega; los empleados reciben Teams instalado. Dentro de la organización el usuario que más importa es el **Team Lead / mando medio que convoca y conduce reuniones** — el resto participa. Concentración de cuentas: 71% con menos de 100 licencias, 24% entre 100 y 1.000, 5% con más de 1.000; ese último 5% concentra el 58% de las licencias.

## Lo que sabemos

- Reuniones es el módulo dominante: 82% de los usuarios activos participa en al menos una reunión semanal; chat diario 64%, archivos 31%, llamadas 1:1 22% — *brief del caso*
- El usuario corporativo promedio pasa 11,4 h semanales en reuniones de Teams; 41% de las reuniones supera los 8 participantes y 23% supera la hora — *brief del caso*
- Dentro de la reunión se usa lo básico y casi nada de lo colaborativo: compartir pantalla 67%, chat 44%, reacciones 38%, grabación 21%, salas 9%, notas 8%, Whiteboard 5% — *brief del caso*
- En el 29% de las reuniones de más de cinco participantes se pega un enlace externo en el chat: documentos (Google Docs, Notion), tableros (Miro, Mural, FigJam), tickets (Jira), dashboards — *brief del caso*
- 37% de las organizaciones tiene además Slack o Google Chat activo en al menos un equipo — *brief del caso*
- 46% de los tickets de soporte del módulo Archivos es "no encuentro el archivo" (los archivos viven en SharePoint) — *brief del caso*
- Insatisfacción post-reunión: audio/video 34%, "demasiadas reuniones" o demasiado largas 26%, colaboración durante la reunión 19%, notificaciones y ruido 12%, otros 9% — *brief del caso*
- Renovación anual: 94% renueva, 2,4% sube de plan, 3,6% baja o no renueva. Quienes bajan citan, en orden: "pagamos por funciones que no usamos", "costo", "el equipo ya usa otras herramientas" — *brief del caso*
- El salto de Business Premium a Business Max (capacidades avanzadas de reuniones) cuesta USD 8 por usuario/mes — *brief del caso*

## Creencias no verificadas

Ordenadas por impacto × incertidumbre. La primera es la que hay que atacar.

1. **[product] [value]** Cuando un Team Lead pega un link de Miro, Notion o Jira en el chat de la reunión, lo hace porque Teams no le resuelve trabajar en vivo sobre ese contenido — no porque el artefacto simplemente viva ahí por razones ajenas a la reunión. Si Teams resolviera la colaboración en vivo, dejaría de salirse. — weakened by [product/research/2026-09-16-0115-colaboracion-en-vivo-fuera-de-teams.md] (2026-09-16) — weakened by [product/insights/2026-09-29-2040-colaboracion-en-vivo-fuera-de-teams.md] (2026-09-29) — contradicted by [product/insights/2026-09-29-2100-entrevistas-colaboracion-en-vivo-fuera-de-teams.md] (2026-09-29)
2. **[opportunity: colaboracion-en-vivo-fuera-de-teams] [value]** En la mayoría del 38% de reuniones del segmento donde se comparte un link a Miro/Mural/FigJam durante la llamada, dos o más participantes editan ese artefacto mientras dura la reunión — no solo lo consultan. *(Versión medible y acotada al segmento de la creencia 1.)*
3. **[product] [viability]** Las cuentas que bajan de plan o no renuevan tienen un problema de valor percibido, no de precio: "pagamos por funciones que no usamos" es literal — si las usaran, renovarían al mismo precio.
4. **[product] [value]** El Team Lead percibe la colaboración durante la reunión como un problema propio que quiere resolver, y no como algo normal del trabajo. Los números de uso (salas 9%, notas 8%, Whiteboard 5%) reflejan que esas funciones no sirven, no que no exista la necesidad. — weakened by [product/insights/2026-09-29-2040-colaboracion-en-vivo-fuera-de-teams.md] (2026-09-29) — contradicted by [product/insights/2026-09-29-2100-entrevistas-colaboracion-en-vivo-fuera-de-teams.md] (2026-09-29)
5. **[product] [viability]** Existe disposición a pagar los USD 8/usuario/mes de Business Max si lo que se resuelve es la colaboración en vivo dentro de la reunión — y esa decisión la puede empujar el Team Lead ante IT, no solo IT por su cuenta.
6. **[opportunity: colaboracion-en-vivo-fuera-de-teams] [viability]** En las cuentas del segmento que subieron de Business Premium a Business Max en los últimos 12 meses, la conversación la inició o la justificó un mando medio con una necesidad concreta de reunión, no IT por consolidación de costo. *(Versión medible y acotada al segmento de la creencia 5.)*
7. **[product] [value]** "No encuentro el archivo" es un problema de búsqueda y navegación en SharePoint, y no la consecuencia de que el archivo relevante viva fuera de Teams (en Google Docs, Notion o Drive), en cuyo caso ningún arreglo de búsqueda lo resolvería. — weakened by [product/insights/2026-09-29-2100-entrevistas-colaboracion-en-vivo-fuera-de-teams.md] (2026-09-29)
8. **[opportunity: decisiones-que-no-sobreviven-la-reunion] [value]** En las reuniones de más de 5 del segmento donde se usó el resumen o Facilitator de Copilot, la proporción de decisiones que no quedan registradas o se ejecutan distinto no es menor que donde no se usó: el recap de IA no resuelve el problema. *(Por impacto × incertidumbre iría arriba; se agrega al final para no romper las referencias numéricas.)*
9. **[opportunity: decisiones-que-no-sobreviven-la-reunion] [viability]** En las cuentas del segmento, quien decide el plan (TI) aceptaría "que las decisiones de reunión queden con responsable y se cumplan" como motivo para pagar Business Max, y no lo vería como algo ya cubierto —o por cubrir— con Copilot.
10. **[feature: cierre-de-reunion] [usability]** Los Team Leads del segmento sostienen un cierre confirmado de ≤2 min (qué, quién, cuándo) en la mayoría de sus reuniones de más de 5 durante 4 semanas, sin que se salte por falta de tiempo.
11. **[feature: cierre-de-reunion] [value]** En las reuniones con cierre confirmado, la proporción de decisiones que en las 2 semanas siguientes se ejecutan distinto, tarde o no se ejecutan es menor que en las mismas series sin cierre.
12. **[feature: decisiones-extraidas-ia] [value]** La lista de decisiones que propone la IA separa decisión de idea y asigna responsable con precisión suficiente para que el grupo la confirme en ≤2 min con correcciones menores.
13. **[feature: decisiones-extraidas-ia] [value]** La lista confirmada la leen los participantes, incluidos los que no hablaron, a diferencia del recap actual.
