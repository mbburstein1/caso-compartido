---
spec: product/specs/2026-10-13-2120-decisiones-extraidas-ia.md
exposure-plan: product/exposure-plans/2026-10-20-2125-decisiones-extraidas-ia.md
level: Nivel 1 — Lista propuesta, visible solo para el organizador
status: designed
---

# Métricas para: Decisiones extraídas por IA, confirmadas por el grupo

> **Supuestos abiertos de este diseño** (pendientes del plan de exposición): (1) el área piloto no está elegida, así que el tamaño de la audiencia es desconocido; (2) los eventos de abajo no están confirmados con tecnología; (3) el Nivel 1 no necesita línea base previa, pero los Niveles 3 y 4 sí, y hay que capturarla antes de revelar el Nivel 1. T2 no se corrió: estas métricas leen la precisión desde el uso del organizador, no contra una clave.

## Audiencia objetivo

**Organizadores** (quien inicia, no los participantes: en el Nivel 1 solo el organizador ve la lista) de reuniones de más de 5 participantes con la transcripción activada, que conducen al menos una serie semanal, en el área voluntaria del piloto, dentro de una cuenta del segmento de `product/overview.md` (Business Premium, 100+ licencias, tecnología, 3+ países).

**Denominador:** organizadores del área piloto con la función activada que condujeron al menos 1 reunión elegible (más de 5 participantes, transcripción activa) durante las 2 semanas del nivel. Si un organizador no tuvo ninguna reunión elegible, no entra al denominador. **Tamaño:** desconocido hasta elegir el área (`assumption`).

## Frecuencia esperada

**Semanal.** Los entrevistados conducen series semanales de más de 5 (sync, refinamiento, escalamientos, revisión de métricas: `product/insights/2026-09-29-2100-entrevistas-colaboracion-en-vivo-fuera-de-teams.md`, `real`). La encuesta tomó como candidato a quien conduce 2 o más reuniones de más de 5 por semana (R2, `survey`). La ventana de retención es la semana.

## Acquisition

- **Signal:** el organizador abre la lista propuesta durante una reunión elegible.
- **Expanded definition:** cuenta el organizador de la reunión, o quien él designó para el cierre si la función ya lo permite. Abrir la lista después de colgar no cuenta para la adquisición: el valor del Nivel 1 está en tenerla antes de cerrar.
- **Calculation:** organizadores que abrieron la lista en ≥ 1 reunión elegible / audiencia objetivo, en las 2 semanas del nivel.
- **Target:** 80% · **Why:** es un área voluntaria, a la que se le comunica el piloto, y la lista se anuncia sola faltando unos minutos. Menos del 80% indicaría un problema de visibilidad antes que de valor.
- **Events needed:** `reunion_elegible` (meeting_id, serie_id, organizer_id, area_id, n_participantes, transcripcion_activa, nivel, inicio, fin) · `lista_propuesta_generada` (meeting_id, minuto_relativo_al_fin, n_decisiones, n_tareas, n_ideas, n_sin_responsable, latencia_s) · `lista_abierta` (meeting_id, user_id, rol: organizador|designado, minuto_relativo_al_fin).

## Activation

- **Signal:** el organizador usa la lista como base: la copia (acción «Copiar lista») en una reunión donde la corrigió poco.
- **Expanded definition:** cuenta el organizador que, en al menos 2 reuniones elegibles distintas, abrió la lista, hizo ≤ 2 correcciones y la copió. Una corrección es editar el texto, cambiar el tipo, cambiar el responsable o la fecha, borrar un ítem o agregar uno.
- **Signal threshold:** ≤ 2 correcciones + copiar, en 2 reuniones · **Why:** el spec falla si «la mediana de correcciones supera 2 ítems por reunión», y la hipótesis es que el organizador deja de reconstruir desde cero. Copiar es el gesto observable de "la usé de base". Exigir 2 reuniones descarta el acierto de una vez. · **Excludes:** abrirla y no copiarla (la miró y siguió con lo suyo), copiarla después de rehacerla (más de 2 correcciones), y los usos en una sola reunión.
- **Calculation:** organizadores que cumplen el umbral / audiencia objetivo, en las 2 semanas del nivel.
- **Target:** 60% · **Why:** es coherente con el «avanza si» del nivel (mediana de ≤ 2 correcciones por reunión). Si menos de 6 de cada 10 organizadores logran usarla así dos veces, la mediana de las reuniones difícilmente queda en ≤ 2.
- **Events needed:** `lista_abierta` · `item_corregido` (meeting_id, item_id, accion: editar_texto|cambiar_tipo|cambiar_responsable|cambiar_fecha|borrar|agregar, tipo_antes, tipo_despues) · `lista_copiada` (meeting_id, user_id, n_items, minuto_relativo_al_fin).
- **Requisito:** «Copiar lista» tiene que estar en lo que revela el Nivel 1. Se agregó al plan de exposición el 2026-10-20.

## Retention

- **Signal:** el organizador abre la lista en al menos la mitad de sus reuniones elegibles de la semana.
- **Expanded definition:** cuenta el organizador activado (ver Activation) que, en cada una de las 2 semanas del nivel, abrió la lista en ≥ 50% de sus reuniones elegibles de esa semana.
- **Retention curve:** cohorte = semana de la primera activación. Se sigue semana a semana durante el nivel, y se prolonga durante el Nivel 2 para los mismos organizadores. Con 2 semanas y un área, la lectura es **direccional**.
- **Calculation:** organizadores que cumplen la señal en las 2 semanas / audiencia objetivo.
- **Target:** 50% · **Why:** es la puerta de entrada del Nivel 2 («organizadores que abrieron la lista en al menos la mitad de sus reuniones»). Con menos de la mitad de la audiencia, el Nivel 2 se correría sobre muy pocas personas.
- **Events needed:** `reunion_elegible` · `lista_abierta` (los mismos, agregados por organizador y semana).

## Satisfaction

- **Instrument:** encuesta en el producto, 1 pregunta cerrada y 1 abierta opcional · **Question:** «¿Qué tan útil fue esta lista como punto de partida para cerrar la reunión?» (1 = nada útil, 5 = muy útil) y «¿Qué tuviste que corregir?» · **When it shows:** al cerrar la lista por tercera vez (no antes: la primera impresión no es una opinión sobre el uso), una sola vez por organizador en el nivel · **Cut:** 4 o 5.
- **Expanded definition:** organizadores de la audiencia que respondieron con 4 o 5. La respuesta abierta va a `/analyze-feedback`, no al número.
- **Calculation:** organizadores con 4 o 5 / audiencia objetivo. Se reportan aparte la tasa de respuesta y el % entre quienes respondieron.
- **Target:** 50% · **Why:** por debajo de la activación (60%), porque no todos llegan a la tercera apertura ni responden. Si la satisfacción queda muy por debajo de la retención, es la señal de usuario cautivo.
- **Events needed:** `encuesta_mostrada` (user_id, meeting_id, n_apertura) · `encuesta_respondida` (user_id, puntaje, texto_abierto).

## Business metrics

Del overview y la oportunidad, tal como están declaradas: **upgrade de Business Premium a Business Max** (USD 8 por usuario/mes). Línea base del segmento: 3,1% de cuentas en 12 meses (`unverified`). **No se lee en el Nivel 1:** una sola área en 2 semanas no mueve un plan. La métrica de negocio que sí aparece en este nivel la pide la historia de TI: % de reuniones elegibles del área con lista abierta, exportable desde la administración. Se lee al lado, como insumo para la creencia 9.

## Conciliación con el plan de exposición

- **Avanza si la mediana de correcciones es ≤ 2 por reunión** → se calcula a nivel de reunión con `item_corregido` sobre las reuniones con `lista_abierta`. Es un indicador de calidad que se lee al lado del AARS. La activación usa la misma línea (≤ 2) por persona, y su meta del 60% es coherente con esa mediana.
- **Avanza si menos de 1 de cada 10 decisiones propuestas se reclasifica como idea** → `item_corregido` con accion = cambiar_tipo, tipo_antes = decision y tipo_despues = idea, sobre el total de decisiones propuestas (`lista_propuesta_generada.n_decisiones`). Es un indicador de calidad, no una métrica AARS.
- **Se detiene si la mediana es > 4 o si se reclasifican > 1 de cada 4** → los mismos dos indicadores. Un `activation` muy por debajo de su meta (< 30%) es coherente con esa detención, pero la regla la decide el indicador, no el AARS.
- **Entrada al Nivel 2** (organizadores que abrieron la lista en ≥ la mitad de sus reuniones) → la lee `retention`, con meta del 50%.
