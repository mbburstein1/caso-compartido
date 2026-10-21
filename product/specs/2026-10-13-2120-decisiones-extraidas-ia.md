---
feature: decisiones-extraidas-ia
opportunity: decisiones-que-no-sobreviven-la-reunion
solutions: product/solutions/2026-10-06-2055-decisiones-que-no-sobreviven-la-reunion.md
tests: product/tests/2026-10-06-2100-decisiones-que-no-sobreviven-la-reunion.md
status: draft — escrito antes de correr T2 (ver «Probado antes del spec»)
critique: product/insights/2026-10-20-2115-critique-decisiones-extraidas-ia.md (synthetic, 2026-10-20)
---

> **Revisión 2026-10-20, tras la crítica de personas.** Cambios: (1) la lista confirmada vive también fuera de la instancia de la reunión; (2) se agrega una historia para TI; (3) se agregan casos borde de atribución del responsable y el aviso de que no se lee el tablero; (4) se recorta la historia «Corregir después», que el panel no sostuvo. **Decisión sobre externos** (confirmada por Marcelo el 2026-10-20): el envío a externos queda **apagado por defecto** y lo habilita TI; cuando está habilitado, a un externo no se le asigna nada sin que lo acepte. La crítica es `synthetic`: estos cambios responden a riesgos señalados, no a evidencia nueva.

# Decisiones extraídas por IA, confirmadas por el grupo

## Problema

En las reuniones de más de cinco personas del segmento, lo que se decide se ejecuta distinto, tarde o no se ejecuta. Nadie confirma antes de colgar qué se decidió, quién lo hace y para cuándo. El responsable es el dato que más falla, y el líder sostiene lo decidido reescribiéndolo a mano después, entre 10 y 60 minutos por reunión. El recap de IA que ya existe no lo resuelve: pone todo al mismo nivel, convierte ideas en decisiones y no dice quién se comprometió, pero igual se lee como fuente de verdad. Quienes lo usan pierden más decisiones, no menos (65% vs. 40%).

> Evidencia: "Se habló en la sync, cada uno se fue con su versión y nadie lo escribió. Yo pensé que el arquitecto iba a hacer el ADR y él pensó que yo lo iba a mandar por correo" — Ricardo Salinas, `product/insights/2026-09-29-2100-entrevistas-colaboracion-en-vivo-fuera-de-teams.md` (insight 1, `real`)
>
> Evidencia: "Marca como decisión cosas que eran solo ideas. Alguien dice 'podríamos pasar el release al 20' y en el resumen aparece 'se decidió pasar el release al 20'" — Paula Benítez, mismo archivo (insight 2, `real`). Le costó ~1 semana de dos desarrolladores.
>
> Evidencia: "Me resumió la conversación, no las decisiones" — Martina Rojas, mismo archivo (insight 2, `real`)
>
> Evidencia: los que usan el resumen de IA pierden la decisión en el 65% de los casos vs. 40% de los que no lo usan (56% vs. 46% reclasificando) — `product/insights/2026-10-06-2100-cruce-recap-ia-decisiones.md` (`survey`, correlacional)

## Para quién

- **[[camila-ferreyra]] (primaria):** Engineering Manager que conduce las ceremonias de un equipo de 11 personas repartido en tres husos horarios. Modera y anota a la vez, y hoy pasa los compromisos a Jira en 25–35 minutos por ceremonia. Es el caso exacto del segmento.
- **[[paulina-achondo]] (primaria):** su objetivo principal es salir de la reunión "con algo decidido y escrito", y hoy reconstruye el acuerdo en 30–40 minutos.
- **[[ricardo-melnick]] (secundaria, receptor):** no conduce, pero recibe lo decidido. Hoy no confía en el acta y reenvía lo acordado con sus propias palabras. Entra desde el celular a un tercio de las reuniones. Si la lista no le sirve a él, no sirve como fuente de verdad.
- **[[nadia-espinoza]] (terciaria, TI):** no usa la función, pero la activa, decide si sale a externos y defiende el gasto en la renovación. Sin su historia, el spec no tiene camino a Business Max.

## Recorrido de la persona (Camila)

1. **Disparador:** Camila conduce el refinamiento semanal con su equipo de 11 personas en Teams, con Jira en pantalla compartida. La transcripción está activada. *(Mundo sistema de registro: Martina, Andrés, Diego, Sofía, `real`.)*
2. **Durante la reunión:** se discute y salen ideas ("podríamos pasar el release al 20"), compromisos ("yo lo veo") y cierres ("vamos con eso"). Camila modera y no alcanza a anotar. *("Escribir y moderar a la vez me cuesta": Lucía, `real`.)*
3. **Faltando dos minutos,** Camila abre la lista que propone la IA: las decisiones arriba, las tareas aparte y las ideas separadas al final. Dos decisiones aparecen marcadas «sin responsable». *(Hoy este paso no existe: nadie confirma antes de colgar. Insight 1, `real`.)*
4. **Confirmación con el grupo:** Camila lee las decisiones en voz alta. Alguien dice "eso no lo decidimos, era una idea", y ella la mueve a ideas. Para cada decisión sin responsable pregunta "¿quién lo toma?", y alguien la toma. **Aquí aterriza el valor:** el responsable queda dicho y oído por todos antes de colgar, que es justo lo que se perdió en los casos de Andrés, Lucía y Ricardo Salinas.
5. **Publicación:** Camila confirma. La lista llega al chat de la reunión, al correo de los invitados internos y al historial de la serie de reuniones, marcada como confirmada por el grupo, a diferencia del recap. Los dos contratistas externos la reciben solo porque TI de su cuenta habilitó el envío a externos.
6. **Resultado:** Camila cuelga sin nada que reescribir. Ricardo Melnick abre el correo en el celular y ve en una pantalla qué se decidió y qué le toca a él. Dos semanas después, quien quedó como responsable sabía que lo era.

*Camila sigue pasando lo decidido a Jira a mano. Escribir en el sistema donde vive el trabajo es la alternativa A3, que quedó aparcada.*

## Historias críticas

### Lista propuesta que separa decisión de idea

Como Camila, quiero que al cierre de la reunión la IA me proponga una lista que separe las decisiones de las tareas y de las ideas, con responsable y fecha, para no tener que reconstruir lo acordado ni corregir un resumen que mezcla todo.

Criterios de aceptación:
- [ ] Antes de terminar la reunión, el organizador puede abrir la lista propuesta, generada a partir de la transcripción hasta ese minuto.
- [ ] Cada ítem tiene un tipo (decisión, tarea o idea), una línea de texto, un responsable y una fecha.
- [ ] Las decisiones aparecen primero y las ideas en una sección aparte, con la etiqueta «idea».
- [ ] Si nadie tomó ni aceptó la decisión durante la reunión, el responsable aparece como «sin responsable». No se infiere de quién habló más ni de quién la propuso.
- [ ] Si no se dijo una fecha, aparece «sin fecha». No se inventa.
- [ ] Caso borde: en una reunión donde no se decidió nada, la lista dice «No se registraron decisiones» y no convierte ideas en decisiones para llenar.
- [ ] Caso borde, sala híbrida: si el compromiso lo tomó alguien a quien la transcripción no identifica (por ejemplo, varios en una sala con un solo micrófono), el responsable aparece «sin responsable». No se asigna a la sala ni a quien más se escuchó.
- [ ] La lista avisa, siempre visible: «Solo incluye lo que se dijo. Las decisiones tomadas en el tablero (votos, post-its) no aparecen acá.»

Traza adicional: crítica de personas 2026-10-20 (Paulina: sala híbrida; Camila: votos en Miro), `synthetic`

Traza: insight 2 de `product/insights/2026-09-29-2100-entrevistas-colaboracion-en-vivo-fuera-de-teams.md`

### Confirmar con el grupo en dos minutos

Como Paulina, quiero confirmar la lista con el grupo antes de colgar, corrigiendo lo que esté mal y asignando lo que quedó sin dueño, para que lo decidido quede validado por todos y no dependa de mi memoria.

Criterios de aceptación:
- [ ] Durante la confirmación se puede, sobre cada ítem: editar el texto, cambiar el tipo, asignar o cambiar el responsable, cambiar la fecha, borrarlo y agregar un ítem que falte.
- [ ] Las decisiones «sin responsable» quedan destacadas. Para confirmar, cada una necesita un responsable o una marca explícita de «queda sin dueño».
- [ ] Puede conducir la confirmación el organizador o un participante que él designe (para cuando el líder está moderando).
- [ ] Nada se publica a los participantes sin confirmación.
- [ ] Caso borde: si la reunión termina sin confirmar, la lista queda como borrador solo para el organizador y se le avisa por correo. No se publica como si estuviera confirmada.
- [ ] Cuando no hay nada que corregir, se confirma toda la lista con una sola acción.
- [ ] Si se asigna un ítem a alguien que no está conectado en ese momento, o que es externo, el ítem queda «por aceptar» hasta que esa persona lo acepte desde el correo o el chat. No se da por confirmado en su nombre.

Traza: insight 1 (falta de cierre, responsable) y «Para la próxima ronda» punto 1 (Lucía), mismo archivo

### Lista confirmada que llega a todos, incluidos los que no hablaron

Como Ricardo Melnick, quiero recibir una lista corta y confirmada de lo que se decidió y lo que me toca, donde ya la busco, para no tener que reconstruirla ni reenviarla con mis palabras.

Criterios de aceptación:
- [ ] Al confirmarse, la lista se publica en el chat de la reunión y se envía por correo a todos los invitados internos, hayan hablado o no.
- [ ] La lista confirmada también queda en el historial de la **serie** de reuniones (o del canal, si la reunión es de un canal). Se encuentra desde la reunión siguiente y sobrevive a reprogramar o recrear la serie.
- [ ] El asunto del correo empieza por lo que le toca a cada persona («Te toca: {ítem}, {fecha}») o, si no le toca nada, por «Decisiones confirmadas: {reunión}», para que se encuentre buscando en Outlook.
- [ ] La lista dice que fue «confirmada por el grupo», con la fecha y quién la confirmó, y no se confunde con el recap automático.
- [ ] Cada persona ve primero los ítems donde es responsable.
- [ ] En el celular, las decisiones y tareas de una reunión típica (hasta 8 ítems) se leen sin hacer zoom ni salir del correo o del chat.
- [ ] Caso borde: los participantes sin licencia Copilot también la reciben.
- [ ] Caso borde: los externos invitados la reciben solo si TI habilitó el envío a externos (ver historia de TI).

Traza adicional: insight 3 de entrevistas (lo nativo se pierde al quedar atado a una instancia de reunión, `real`) y crítica de personas 2026-10-20 (Camila, Ricardo, `synthetic`)

Traza: insight 2 ("el recap se lee como fuente de verdad aunque esté mal": Javier, Paula) y «Para la próxima ronda» punto 2 (el recap largo que nadie leyó: Martina), mismo archivo; restricción de la oportunidad (Facilitator deja fuera a los externos)

### Controlar y medir la función desde TI

Como Nadia, quiero activar la función por área, decidir si la lista se envía a externos y ver cuántas reuniones terminan con una lista confirmada, para correr un piloto acotado y llegar a la renovación con un dato y no con una anécdota.

Criterios de aceptación:
- [ ] Desde la administración del tenant, TI activa o desactiva la función por grupo o área. Por defecto está desactivada.
- [ ] TI decide si la lista se envía a invitados externos. Por defecto, no.
- [ ] TI ve, por área y por mes, y puede exportar: reuniones con transcripción, % con lista confirmada, % de decisiones con responsable y % de ítems «por aceptar» que nunca se aceptaron.
- [ ] La transcripción se procesa dentro del tenant y en la región de datos de la cuenta. Si no se puede, la función no se activa para esa región.
- [ ] Caso borde: si un área desactiva la función a mitad de una serie, las listas ya confirmadas se mantienen en el historial de la serie.

Traza: restricciones de la oportunidad (TI despliega, autoriza integraciones y le inquieta el perímetro; piloto con un área voluntaria), crítica de personas 2026-10-20 (Nadia, `synthetic`). **El plan en que vive la función queda abierto: depende de la creencia 9 («eso es Copilot»), que se prueba con las conversaciones con TI.**

> **Recortada en la revisión 2026-10-20:** la historia «Corregir después sin perder la confirmación». Ningún entrevistado describió corregir después y el panel de personas tampoco la sostuvo, como el propio spec anticipaba.

## Hipótesis

Creemos que **los Team Leads del segmento confirmarán con el grupo, antes de colgar, la lista de decisiones que propone la IA en la mayoría de sus reuniones de más de 5, y dejarán de reescribir lo decidido después**, porque la lista ya separa la decisión de la idea y solo les pide resolver lo que falta (sobre todo el responsable), en vez de obligarlos a reconstruir todo o a corregir un recap que mezcla todo.

**Estamos equivocados si**, en 5 series reales:
- la confirmación dura más de 2 minutos en más de la mitad de las reuniones;
- la mediana de correcciones supera 2 ítems por reunión;
- el líder sigue dedicando tiempo a reescribir lo decidido después;
- la proporción de decisiones perdidas a 14 días no baja respecto de las reuniones de la misma serie sin la lista; o
- en las 48 horas siguientes, no más participantes abren la lista confirmada que el recap actual.

## Alternativas consideradas

Exploradas en: `product/solutions/2026-10-06-2055-decisiones-que-no-sobreviven-la-reunion.md`
- A1 `cierre-de-reunion`: elegida y en prueba en paralelo (T1). Es el mismo cierre sin IA. Si falla, arrastra a esta alternativa.
- A3 `decision-al-sistema`: aparcada. La decisión estaba en el ticket o el PRD y aun así se perdió (Martina, Sofía).
- A4 `continuidad-por-serie`: aparcada. Llega tarde para costos que ocurren en días, y su viabilidad es débil.
- A5 `votacion-nativa`: aparcada. Ataca otro problema (converger), que quedó fuera de la oportunidad.

## Probado antes del spec

Probado en: `product/tests/2026-10-06-2100-decisiones-que-no-sobreviven-la-reunion.md`
- T2 `decisiones-extraidas-ia`, precisión contra clave real: **diseñada, sin correr** (status `ready`) · creencia 12, parte de precisión.
- T1 `cierre-de-reunion` (A1): **diseñada, sin correr**. No prueba esta alternativa, pero si falla la descarta.
- **La creencia más riesgosa no está probada (declarado).** Este spec se escribe antes de T2 y es una apuesta, no una conclusión.
- **El spec se mantiene dentro de lo que T2 prueba:** el mecanismo es una extracción desde la transcripción, tipificada (decisión, tarea, idea), con responsable y «sin responsable», y confirmada por personas. Leer el estado del artefacto (votos, filtros, tickets), que aparece en la descripción de A2, **queda fuera de esta versión** a propósito: T2 lo excluye y su resultado no lo cubriría.

## Supuestos

Registrados en `product/overview.md`:
- [feature: decisiones-extraidas-ia] [value] Creencia 12: la lista de decisiones que propone la IA separa decisión de idea y asigna responsable con precisión suficiente para que el grupo la confirme en ≤2 min con correcciones menores. — *dueño de la parte de precisión: Tech (T2)*
- [feature: decisiones-extraidas-ia] [value] Creencia 13: la lista confirmada la leen los participantes, incluidos los que no hablaron, a diferencia del recap actual.
- [opportunity: decisiones-que-no-sobreviven-la-reunion] [viability] Creencia 9: TI aceptaría esto como motivo para pagar Business Max y no lo vería como algo ya cubierto, o por cubrir, con Copilot.
- [opportunity: decisiones-que-no-sobreviven-la-reunion] [value] Creencia 8: el recap o Facilitator de Copilot no resuelve el problema.

Propuestos al registro mientras se escribía este spec (**no registrados**, esperan aprobación):
- [feature: decisiones-extraidas-ia] [feasibility] La lista propuesta se puede generar en menos de 30 segundos a partir de la transcripción en curso, dentro del tenant, y entregarse a participantes sin licencia Copilot y, cuando TI lo habilita, a externos.
- [feature: decisiones-extraidas-ia] [usability] Un participante que no es el organizador puede conducir la confirmación sin capacitación previa.
- [feature: decisiones-extraidas-ia] [usability] Un participante encuentra una lista confirmada de hace 3 semanas o más en menos de 1 minuto, desde Outlook o desde la serie de reuniones. *(Agregado tras la crítica 2026-10-20.)*
