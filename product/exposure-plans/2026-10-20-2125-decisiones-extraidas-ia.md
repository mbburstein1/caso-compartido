---
spec: product/specs/2026-10-13-2120-decisiones-extraidas-ia.md
date: 2026-10-20
status: draft
---

# Plan de exposición: Decisiones extraídas por IA, confirmadas por el grupo

## Hipótesis (del spec, textual)

Creemos que **los Team Leads del segmento confirmarán con el grupo, antes de colgar, la lista de decisiones que propone la IA en la mayoría de sus reuniones de más de 5, y dejarán de reescribir lo decidido después**, porque la lista ya separa la decisión de la idea y solo les pide resolver lo que falta (sobre todo el responsable), en vez de obligarlos a reconstruir todo o a corregir un recap que mezcla todo.

> **Antes del Nivel 1:** T2 (precisión contra una clave real) no se corrió; se decidió pasar al spec el 2026-10-20 (`product/corrections.md`). Por eso el Nivel 1 también lee la precisión, desde el lado del organizador, sin haberla aislado antes.

## Niveles

### Nivel 1 — Lista propuesta, visible solo para el organizador

- **Qué se revela:** faltando unos minutos, el organizador ve la lista propuesta (decisión / tarea / idea, responsable o «sin responsable», fecha o «sin fecha») y el aviso de que no incluye lo decidido en el tablero. Puede editarla para él y copiarla («Copiar lista», agregado el 2026-10-20 para poder medir la activación). **Sigue oscuro:** la confirmación con el grupo, la publicación y el historial de la serie. Nadie más ve la lista.
- **Creencia:** los organizadores encuentran la lista lo bastante correcta como para usarla de base: la corrigen poco y dejan de partir de cero.
- **Audiencia:** organizadores de reuniones de más de 5 con la transcripción activada, que conducen al menos una serie semanal, en un área voluntaria de una cuenta del segmento.
- **Duración:** 2 semanas.
- **Validación:** **Avanza si** la mediana de correcciones es ≤ 2 ítems por reunión **y** los organizadores marcan como «era una idea, no una decisión» menos de 1 de cada 10 decisiones propuestas. **Se detiene si** la mediana supera 4 ítems o si convierte ideas en decisiones en más de 1 de cada 4: reproduce la falla del recap.

### Nivel 2 — Confirmación con el grupo antes de colgar

- **Qué se revela (además del Nivel 1):** el flujo de confirmación frente al grupo: decisiones «sin responsable» destacadas, confirmar todo con una sola acción, designar a otra persona para conducirla, ítems «por aceptar» para quien no está conectado, y borrador por correo si la reunión se corta. **Sigue oscuro:** la publicación a los participantes y el historial de la serie. La lista confirmada queda solo para el organizador.
- **Creencia:** los organizadores confirman la lista con el grupo antes de colgar en la mayoría de sus reuniones de más de 5, en no más de 2 minutos.
- **Audiencia:** los mismos organizadores del Nivel 1 que llegaron a abrir la lista en al menos la mitad de sus reuniones.
- **Duración:** 3 semanas.
- **Validación:** **Avanza si** se confirma la lista en ≥ 60% de las reuniones de más de 5 de esos organizadores **y** la confirmación dura ≤ 2 min en más de la mitad. **Se detiene si** se confirma en < 40% de las reuniones o dura más de 2 min en más de la mitad (falsador del spec).

### Nivel 3 — La lista confirmada llega a todos los invitados

- **Qué se revela (además del Nivel 2):** al confirmarse, la lista se publica en el chat de la reunión y se envía por correo a los invitados internos, marcada como «confirmada por el grupo», con lo de cada persona primero y legible en el celular. Externos, solo si TI lo habilitó. **Sigue oscuro:** el historial de la serie y el asunto «Te toca».
- **Creencia:** los participantes, incluidos los que no hablaron, leen la lista confirmada más que el recap actual.
- **Audiencia:** los invitados internos de las reuniones del Nivel 2 en que se confirmó la lista.
- **Duración:** 2 semanas.
- **Validación:** **Avanza si** el % de invitados que abre la lista en 48 h supera al % que abre el recap en las mismas series (línea base previa) **y** ≥ 50% de los invitados que no hablaron la abre. **Se detiene si** no supera al recap: una lista confirmada que nadie lee es otro recap (creencia 13).

### Nivel 4 — La lista vive en la serie y le dice a cada uno qué le toca

- **Qué se revela (además del Nivel 3):** la lista confirmada queda en el historial de la serie (o del canal) y sobrevive a reprogramar o recrear la serie, y el asunto del correo empieza por «Te toca: {ítem}, {fecha}».
- **Creencia:** las decisiones confirmadas se ejecutan como se decidieron: en las series con la función, la proporción de decisiones perdidas a 14 días baja frente a las mismas series antes de la exposición.
- **Audiencia:** las series del Nivel 3 que confirmaron la lista en al menos 2 reuniones.
- **Duración:** 3 semanas (2 de exposición más el seguimiento a 14 días).
- **Validación:** **Avanza si** la tasa de decisiones perdidas a 14 días (distinto + tarde + no ejecutada) es ≤ la mitad de la línea base **y** el organizador deja de dedicar tiempo a reescribir después (mediana ≤ 5 min por reunión). **Se detiene si** la reducción relativa es < 25%. Son los mismos umbrales de T1, para poder comparar.

## Mecanismo de revelación

**Feature flags.** Lo que decide es que los niveles exponen a subgrupos distintos: el Nivel 1 solo al organizador, el Nivel 2 solo a los organizadores que ya usan la lista, el Nivel 3 a los invitados. Una entrega incremental mostraría todo a todos. La activación por área que pide la historia de TI se alinea con esto: es la misma llave, vista desde la administración. La decisión final es de ingeniería.

## Validaciones en paralelo

- **Viabilidad: «eso es Copilot» (creencia 9) y quién empuja el upgrade (creencia 6).** Las entrevistas a TI con la guía `product/interview-guides/2026-10-20-2120-ti-decisiones-que-no-sobreviven-la-reunion.md`. Si TI lo asigna a Copilot, un Nivel 4 que pase no tiene camino a Max.
- **Precondición regulatoria:** que la transcripción se procese en el tenant y en la región de datos de la cuenta. Sin eso no se activa el Nivel 1 en esa región. Se confirma con tecnología antes de elegir el área piloto.
- **Costo operativo:** costo de procesar transcripciones por reunión a escala del segmento. Se estima con tecnología durante el Nivel 1.

## Preguntas abiertas para el equipo de producto

- **Línea base:** los Niveles 3 y 4 comparan contra «antes». Hay que capturar, en las semanas previas al Nivel 1, la apertura del recap y la pérdida de decisiones a 14 días en las mismas series. ¿Existe esa telemetría de apertura del recap, o se mide a mano?
- **Seguimiento a 14 días:** no es telemetría, requiere consultar al líder y al responsable (como en T1). ¿Quién lo hace y con qué capacidad?
- **Área piloto:** ¿qué cuenta y área voluntaria, con transcripción activada y sin bloqueo de compliance? Las entrevistas a TI pueden dar la candidata.
- **T2 sin correr:** si el Nivel 1 se detiene, no se va a saber si falló la precisión de la IA o la forma de mostrarla. Correr T2 sobre las mismas reuniones del Nivel 1 lo separaría a bajo costo.
