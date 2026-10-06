---
date: 2026-10-06
source: survey
survey_design: product/surveys/2026-09-23-1944-colaboracion-en-vivo-fuera-de-teams.md
results: product/surveys/2026-09-26-1800-respuestas-colaboracion-en-vivo-fuera-de-teams.csv
n: 182 que trabajaron fuera de Teams (170 con al menos una decisión)
opportunity: decisiones-que-no-sobreviven-la-reunion
belief: 8 (product/overview.md)
---

# Cruce: ¿quienes usan el resumen de IA pierden menos decisiones?

**Pregunta.** La creencia 8 sostiene que el recap o Facilitator de Copilot no resuelve el problema. Si quienes usan el resumen de IA perdieran claramente menos decisiones, la oportunidad se acotaría al segmento sin Copilot o se descartaría (regla de la agenda de `product/opportunities/2026-10-06-2050-decisiones-que-no-sobreviven-la-reunion.md`).

**Cómo se cruzó.** Q10 (resumen o asistente de IA) agrupado en "la usa" (algunas o la mayoría de las reuniones), "la dejó" y "no la usa" (no sabía que existía o nunca la usó) × Q9 (dónde quedó lo decidido). Se excluyen las 12 reuniones en las que no se decidió nada. "Decisión perdida" = Q9 incluye "No quedó registrado en ningún lado" o "En un chat fuera de Teams".

## Resultado

| Q10 | n | Sin registro | Chat fuera de Teams | **Perdida (cualquiera)** | Jira, actas o la herramienta |
|---|---|---|---|---|---|
| La usa | 62 | 27% | 37% | **65%** | 39% |
| La dejó | 25 | 36% | 16% | 52% | 48% |
| No la usa | 83 | 22% | 18% | **40%** | 55% |

**Quienes usan el resumen de IA no pierden menos decisiones: pierden más** (65% vs. 40%). La creencia 8 sobrevive al primer filtro.

## Por qué no es un artefacto obvio

- **Se repite en los dos canales:** email 65% vs. 42%; panel 64% vs. 38%.
- **Se repite en los dos mundos:** pizarra 71% vs. 41% (n=21/39); sistema de registro 61% vs. 43% (n=41/69).
- **Los grupos son comparables** en lo observable: pizarra 32% vs. 34%, salen en más de la mitad de sus reuniones 38% vs. 38%, externos 20% vs. 22%.
- **Ruido de medición:** 11 personas que en Q10 dicen no usar IA dejaron la decisión en un recap o resumen de IA (Q9 "Otro"). Q10 mide autopercepción, y el recap puede llegar sin que la persona lo active. Si se reclasifica a todos los que usan IA por Q10 o por Q9, la brecha se achica pero no se invierte: **56% (42/75) vs. 46% (44/95)**.

## Límites

- Muestra autoseleccionada y correlacional: no prueba que el recap *cause* más pérdida. Es plausible el camino inverso, que los equipos con más dispersión adopten más el recap, o que haya una tercera variable (organizaciones con Slack, que llevan la decisión a "chat fuera de Teams").
- Q10 pregunta por el uso general, no por *esa* reunión.
- La diferencia la empuja sobre todo "chat fuera de Teams" (37% vs. 18%). "Sin registro" por sí solo es parecido (27% vs. 22%).
- Una encuesta autoseleccionada no confirma una creencia. Esto **no** es un `confirmed`: es una señal de que la regla de descarte no se activa.

## Qué decisión sigue

- **No acotar la oportunidad al segmento sin Copilot.** Con esta evidencia, tener el resumen de IA no protege la decisión.
- La pista de "chat fuera de Teams" sugiere que, con o sin recap, la decisión viaja a donde el equipo conversa después (Slack, WhatsApp), no a donde se ejecuta. Se suma como pregunta para la ronda 2 de entrevistas: ¿qué pasa entre el recap y el hilo?
- Sigue pendiente la telemetría (recap × tareas en Planner o tickets editados en 48 h), que mide el comportamiento real y no la autopercepción.

> Evidencia: "En el resumen de IA, que nadie leyó" — R-025 · "En el resumen de Copilot, que después pegamos en el canal" — R-048 · "En el recap automático, pero después lo tuve que corregir" — R-211 · "En el recap pero le faltaba quien hacia que" — R-231
