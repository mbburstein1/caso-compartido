---
opportunity: decisiones-que-no-sobreviven-la-reunion
solutions: product/solutions/2026-10-06-2055-decisiones-que-no-sobreviven-la-reunion.md
status: ready
---

# Pruebas de solución para: lo decidido en la reunión no sobrevive hasta la ejecución

## Por qué probar

Se prueban dos alternativas en paralelo: A1 `cierre-de-reunion` y A2 `decisiones-extraidas-ia`. La evidencia prueba el **problema** (10/10 entrevistas `real`; 47% de decisiones perdidas en la encuesta `survey`), pero nadie reaccionó todavía a ninguna de las dos **soluciones**. Para A1 no sabemos si confirmar qué, quién y cuándo antes de colgar reduce las pérdidas, y el único antecedente (el cierre informal de Sofía) "a veces se le va". Para A2 no sabemos si una IA puede separar decisión de idea y asignar responsable mejor que el recap de Copilot, que falla exactamente ahí (6/6 entrevistados).

Va primero, en cada alternativa, la creencia que la mataría más rápido. Las otras (10 y 13) quedan como siguiente paso.

## T1. cierre-de-reunion: cierre conducido por nosotros en series reales

- **Estado de la prueba:** ready
- **Creencia bajo prueba:** creencia 11 de `product/overview.md`, «En las reuniones con cierre confirmado, la proporción de decisiones que en las 2 semanas siguientes se ejecutan distinto, tarde o no se ejecutan es menor que en las mismas series sin cierre.»
- **Riesgo:** [value]
- **Tipo de prueba:** concierge
- **Qué hacemos:**
  1. En cada serie, **reunión base** (sin intervención): una persona del equipo asiste como observadora en silencio y anota las decisiones que escucha, con responsable y fecha si se dijeron. El líder cierra como siempre.
  2. **Dos reuniones con cierre** (las siguientes de la misma serie): durante la reunión, la persona del equipo anota en silencio las decisiones que escucha, igual que en la base y sin mostrarlas al grupo. En los últimos 2 minutos conduce el cierre sobre la plantilla en las notas de reunión de Teams («¿Qué decidimos? ¿Quién lo hace? ¿Para cuándo?»). El grupo confirma o corrige en voz alta y la lista queda en las notas. El líder no tiene que hacer nada.
  3. **Seguimiento a 14 días de cada reunión**: por cada decisión anotada (base), o anotada por la observadora **o** confirmada en el cierre (reuniones con cierre: la unión de las dos listas, sin duplicados), una consulta corta al líder y al responsable: ¿se ejecutó como se decidió, distinto, tarde o no se ejecutó? Si no hay acuerdo entre los dos, se registra como «distinto».
  4. Se registran los minutos que el líder dedicó después de cada reunión a reescribir lo acordado (punto de comparación) y cuánto duró el cierre.
- **Con quién:** 5 Team Leads del segmento con una serie semanal de más de 5 participantes, reclutados entre los 10 entrevistados (los diez reportaron una decisión perdida y ya aceptaron conversar). Se busca mezclar los dos tipos de reunión: pizarra (Tomás, retro; Valeria, planning) y sistema de registro (Martina, planning; Andrés, escalamientos; Diego, métricas; Sofía, revisión de PRD). Al menos uno fuera de España para no depender de compliance, y Lucía solo si su compliance permite un observador externo. Si hay menos de 5, se completa con el pool de la encuesta (grupo 2 del insight 2026-09-29-2040).
- **Material necesario:** (a) plantilla de tres columnas (Decisión · Responsable · Para cuándo) para las notas de reunión de Teams; (b) guion de cierre de 2 minutos con las tres preguntas y qué hacer si una decisión queda sin responsable («queda sin dueño: ¿quién lo toma?»); (c) texto de consentimiento para observar y hacer seguimiento; (d) planilla de captura por decisión: serie, reunión, tipo (base / cierre), texto, responsable, fecha, duración del cierre, minutos posteriores del líder, estado a 14 días según el líder y según el responsable. **Se deja fuera a propósito:** cualquier IA, la escritura en Jira, votación, resumen de la conversación.
- **Material:** `product/tests/materials/t1-cierre-de-reunion/` (guion del concierge, plantilla, consentimiento, planillas de captura con cómo leer el umbral, mensaje de reclutamiento)
- **Duración:** 5 semanas: semanas 1–3 las tres reuniones de cada serie, semanas 3–5 los seguimientos a 14 días.
- **Señal y umbral:** % de decisiones perdidas (distinto + tarde + no ejecutada) a 14 días, en reuniones con cierre vs. reuniones base, sumando todas las series. En las reuniones con cierre el denominador es la **unión** de lo observado y lo confirmado: una decisión que se conversó pero quedó fuera del cierre cuenta, y si se pierde, cuenta como perdida. *(Corregido el 2026-10-06 antes de correr la prueba: la versión anterior seguía solo lo confirmado, lo que podía hacer parecer menor la pérdida con cierre.)* Diagnóstico, no umbral: % de decisiones observadas que el cierre dejó fuera, y su tasa de pérdida.
  - **Pasa** si la tasa con cierre es **≤ la mitad** de la tasa base **y** baja en al menos 4 de las 5 series.
  - **Falla** si la reducción relativa es **< 25%** o baja en 2 series o menos.
  - **Mínimo para leerla:** ≥ 30 decisiones en reuniones con cierre y ≥ 15 en reuniones base. Por debajo, `inconclusive`.
- **Regla de decisión:**
  - **continue** si pasa: A1 sigue a la prueba de adopción (creencia 10).
  - **change** si queda entre los umbrales, si el cierre supera los 2 minutos en más de la mitad de las reuniones, o si lo que se sigue perdiendo es sobre todo por el responsable. En ese caso se prueba una versión distinta (por ejemplo, un rol de registro rotativo que no sea el líder) con su propia prueba.
  - **discard** si falla: confirmar antes de colgar no alivia el dolor, y esa conclusión arrastra a A2 (automatizar un cierre que no sirve no sirve). Se vuelve a `product/solutions/` con A3 y A4.
- **Procedencia esperada:** real
- **Siguiente paso si pasa:** creencia 10 (`[usability]`): los mismos líderes conducen el cierre solos durante 4 semanas con la plantilla y el guion. Se mide en cuántas de sus reuniones grandes lo sostienen.

## T2. decisiones-extraidas-ia: precisión de la extracción contra una clave real

- **Estado de la prueba:** ready
- **Creencia bajo prueba:** creencia 12 de `product/overview.md`, «La lista de decisiones que propone la IA separa decisión de idea y asigna responsable con precisión suficiente para que el grupo la confirme en ≤2 min con correcciones menores.» Esta prueba cubre la parte de **precisión**; la confirmación en ≤2 min con el grupo es el siguiente paso.
- **Riesgo:** [value] (con componente técnico: lo conduce tecnología)
- **Tipo de prueba:** technical-test
- **Qué hacemos:**
  1. Se juntan **12 transcripciones** de reuniones reales de más de 5 del segmento: exportación de la transcripción de Teams, con consentimiento del grupo. Se priorizan las reuniones base y con cierre de T1, porque ahí la lista de la persona observadora y la confirmada por el grupo sirven de clave.
  2. **Clave de respuesta:** el líder y la persona observadora marcan cada ítem relevante como decisión, idea o tarea, con responsable y fecha. Si no están de acuerdo, se discute; si sigue el desacuerdo, el ítem queda fuera.
  3. Se separan **4 transcripciones para ajustar** el prompt y **8 que se reservan**: el resultado solo se lee sobre las 8 reservadas, nunca sobre las de ajuste.
  4. Se corre el prompt de extracción a ciegas sobre las 8. Si la cuenta tiene Copilot, se corre también el recap o Facilitator sobre las mismas 8 como punto de comparación.
- **Con quién:** sin participantes en vivo. Las transcripciones salen de los líderes de T1 y, si faltan, de 2–3 líderes más del pool de la encuesta. **Responsable: tecnología.** Las transcripciones tienen datos de clientes: se anonimizan antes de salir del tenant, y se excluyen las cuentas cuyo compliance no lo permita (Lucía).
- **Material necesario:** (a) prompt de extracción que devuelve una lista de ítems tipificados (decisión / idea / tarea) con responsable y fecha, y «sin responsable» cuando no se dijo; (b) set de entrada: las 12 transcripciones anonimizadas, separadas en ajuste (4) y reservadas (8); (c) clave de respuesta por transcripción; (d) planilla de puntaje por ítem y por reunión. **Se deja fuera a propósito:** interfaz, integración con Teams, publicación, lectura del estado del artefacto (votos, tickets) y el flujo de confirmación.
- **Material:** `product/tests/materials/t2-decisiones-extraidas-ia/` (solicitud y consentimiento, armado y anonimización del set 4 + 8, protocolo y planilla de la clave, prompt v0 para ajustar y congelar, planilla de puntaje con reglas de emparejamiento y de lectura de Copilot, script que calcula las métricas contra el umbral)
- **Duración:** 2 semanas: la recolección se superpone con las semanas 1–2 de T1, y la corrida y el puntaje toman 2–3 días.
- **Señal y umbral:** sobre las 8 transcripciones reservadas:
  - **Precisión de decisión:** de lo que la IA marca como decisión, qué % lo es según la clave. Es la falla de Paula: «marca como decisión cosas que eran solo ideas».
  - **Cobertura de decisión:** de las decisiones de la clave, qué % encontró.
  - **Responsable correcto:** sobre las decisiones encontradas, qué % tiene el responsable correcto (o «sin responsable» cuando corresponde).
  - **Correcciones por reunión:** ítems que habría que agregar, quitar o corregir. Es un indicador indirecto de confirmar en ≤2 min.
  - **Pasa** si precisión ≥ 90%, cobertura ≥ 80%, responsable correcto ≥ 80% **y** mediana de correcciones ≤ 2 por reunión.
  - **Falla** si precisión < 75% **o** cobertura < 60%.
  - Si hay punto de comparación con Copilot y A2 no lo supera en precisión, cuenta como falla aunque cumpla los demás umbrales.
- **Regla de decisión:**
  - **continue** si pasa: A2 sigue a la prueba con personas.
  - **change** si queda entre los umbrales, o si pasa en todo menos responsable correcto: se ajusta el prompt (por ejemplo, que pregunte en el cierre en vez de inferir el responsable) y se prueba otra vez sobre un **set reservado nuevo**, nunca el mismo.
  - **discard** si falla: la IA reproduce la falla del recap y A2 sería un resumen más.
- **Procedencia esperada:** real
- **Siguiente paso si pasa:** Wizard of Oz en 5 series reales (pueden ser las de T1). Una persona entrega la lista que generó la IA, el grupo la confirma al cierre y se mide el tiempo de confirmación (creencia 12, del lado humano) y cuántos participantes la abren en 48 h comparado con el recap (creencia 13).

## Fuera de estas pruebas, pero en paralelo

La viabilidad de A2 depende de la **creencia 9**: si TI pagaría Max por esto o diría «eso es Copilot». No es una creencia de las alternativas y no se prueba acá. Ya está en la agenda de la oportunidad: 6–8 conversaciones con TI, 4 semanas. Conviene empezarla ya, porque una respuesta de «eso es Copilot» cambia qué se hace con un T2 que pase.

## Resultados

*(Lo agrega /analyze-solution-tests)*

## Decisión

*(Lo agrega /analyze-solution-tests)*
