# Guion del concierge — T1 `cierre-de-reunion`

Para la persona del equipo que **hace de "sistema"**: observa la reunión base, conduce el cierre en las dos siguientes y hace el seguimiento a 14 días. El líder no tiene que hacer nada distinto, salvo dejarte entrar y presentarte.

**Lo que esta prueba mide** (fijado en el diseño, no se cambia acá): % de decisiones que a 14 días se ejecutaron distinto, tarde o no se ejecutaron, comparando reuniones con cierre contra la reunión base de la misma serie.

---

## 0. Antes de empezar la serie

1. El líder firmó el consentimiento (`consentimiento.md`) y avisó al grupo: "en las próximas tres reuniones nos acompaña [nombre], que está estudiando cómo cerramos las reuniones".
2. Abre una fila por reunión en `planilla-reuniones.csv` (serie, n.º de reunión, fecha, tipo).
3. Pide al líder la invitación como asistente. Entrarás con cámara apagada.

## 1. Reunión base (reunión 1 de la serie) — solo observar

| Momento | Qué ve el grupo | Qué haces tú |
|---|---|---|
| Toda la reunión | Una persona más, en silencio | Anotas en `planilla-captura.csv` cada decisión que escuchas, con responsable y fecha **solo si se dijeron**. Si no se dijo, dejas la celda vacía. |
| Al cierre | El líder cierra como siempre | Nada. No intervienes, no preguntas, no envías nada. |
| Después | — | Al día siguiente, preguntas al líder: "¿cuántos minutos te tomó, después de la reunión, dejar escrito lo acordado?" y lo anotas en `planilla-reuniones.csv` (`min_lider_post`). |

**Qué cuenta como decisión:** algo que el grupo da por resuelto y que obliga a alguien a hacer o dejar de hacer algo ("lo pasamos al sprint 14", "el ADR lo escribe Juan", "la campaña de Chile se pausa"). **No cuenta:** ideas ("podríamos…"), temas que quedaron para la próxima, información.

## 2. Reuniones con cierre (reuniones 2 y 3 de la serie)

| Momento | Qué ve el grupo | Qué haces tú | Tiempo |
|---|---|---|---|
| Inicio | La plantilla pegada en las notas | Pegas `plantilla-cierre.md` en las notas de la reunión antes de que empiece. | — |
| Durante | Una persona más, en silencio | Anotas en `planilla-captura.csv` las decisiones que escuchas, **igual que en la reunión base** (criterio de §1), con `origen = observada`. No las muestras ni las usas para guiar el cierre. | — |
| Faltando ~3 minutos | El líder te da la palabra ("cerramos con [nombre]") | Acordado con el líder antes: si a 3 minutos del final no te da la palabra, le escribes por chat privado "¿cerramos?". | — |
| Cierre | Tú compartes las notas y dices el texto de abajo | Escribes en la plantilla lo que el grupo dice, en voz alta. | **Máx. 2 min** — cronometra |
| Fin | La lista queda en las notas de la reunión | Cruzas la lista confirmada con tu lista: si una decisión confirmada ya estaba anotada, cambias su `origen` a `ambas` y actualizas responsable y fecha con lo confirmado; si es nueva, la agregas con `origen = confirmada`. Las observadas que el cierre no recogió quedan con `origen = observada`. Anotas `duracion_cierre_seg`. | — |
| Al día siguiente | — | Preguntas al líder los minutos posteriores (igual que en la base). | — |

**Texto del cierre (decirlo así, sin agregar):**

> "Antes de colgar, dos minutos para que todos salgamos con lo mismo. ¿Qué decidimos hoy?"
>
> Por cada decisión que alguien diga: **"¿Quién lo hace?"** · **"¿Para cuándo?"**
>
> Si nadie toma una decisión: **"Queda sin dueño: ¿quién la toma?"** — si nadie la toma, se escribe *sin dueño* y se sigue.
>
> Si aparece algo que no es decisión ("podríamos…"): **"¿Eso lo decidimos o queda abierto?"** — si queda abierto, no se escribe.
>
> Al terminar, lees la lista completa en voz alta: **"¿Alguien lo entendió distinto?"** — se corrige si alguien dice que sí.

**No haces:** usar tu lista para completar o corregir el cierre (si el grupo no menciona una decisión que anotaste, no la recuerdas), resumir la reunión, opinar sobre las decisiones, proponer responsables, abrir votaciones, enviar la lista por correo o pasarla a Jira. La lista queda solo en las notas de la reunión.

**Si el cierre pasa de 2 minutos:** lo terminas igual y anotas la duración real. Es un dato de la prueba (la regla de decisión lo usa), no un error.

## 3. Seguimiento a 14 días de cada reunión

Para **cada decisión** de la planilla, cualquiera sea su `origen` (anotada en la base; observada, confirmada o ambas en las reuniones con cierre), 14 días después de la reunión (±2 días), dos mensajes cortos por chat o correo, por separado:

**Al líder:**
> "Hola [nombre]. Hace dos semanas, en [reunión], quedó: '[decisión]' ([responsable], [fecha si la hubo]). Hoy, ¿cuál de estas describe mejor lo que pasó? (a) se hizo como se decidió · (b) se hizo distinto · (c) se hizo tarde · (d) no se hizo · (e) no sé"

**Al responsable** (si hay responsable; si quedó *sin dueño*, solo al líder):
> El mismo mensaje.

**Regla para el estado final** (columna `estado_final`):
- Si los dos responden lo mismo → esa respuesta.
- Si responden distinto → **distinto**.
- Si solo responde uno → su respuesta, y se marca `una_sola_fuente = si`.
- Si ninguno responde en 3 días hábiles, un recordatorio. Si sigue sin respuesta → **sin_dato** (no cuenta ni como perdida ni como cumplida).
- "No sé" de los dos → **sin_dato**.

**Una decisión está perdida** si su estado final es *distinto*, *tarde* o *no se hizo*. Esa es la única cuenta que importa para el umbral. Las decisiones con `origen = observada` en reuniones con cierre se siguen igual que las demás: son las que el cierre dejó fuera, y si se pierden, cuentan.

En las decisiones observadas sin responsable dicho, el mensaje va solo al líder.

## 4. Cierre de la serie

Agradeces al líder y al grupo. No compartes resultados de la serie con el grupo hasta que terminen todas las series (para no afectar a las demás).
