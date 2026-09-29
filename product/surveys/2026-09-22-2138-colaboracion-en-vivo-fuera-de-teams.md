---
opportunity: colaboracion-en-vivo-fuera-de-teams
research: product/research/2026-09-16-0115-colaboracion-en-vivo-fuera-de-teams.md
beliefs: 1, 2 (product/overview.md) + reenmarque alternativo "recuperar lo acordado"
previous: product/surveys/2026-09-22-2105-colaboracion-en-vivo-fuera-de-teams.md (rediseñada desde cero; la anterior se conserva sin cambios)
date: 2026-09-22
status:
---

# Encuesta: trabajar en vivo sobre un tablero en reuniones de Teams, y qué pasa con lo acordado

- **Objetivos de aprendizaje:**
  1. **Co-edición vs. consulta** (creencia 2). En la última reunión con tablero externo, ¿cuántas personas lo editaron y qué hicieron en él? ¿Cambia según el tipo de reunión? → *Decisión:* si en la mayoría de las reuniones lo edita una persona o nadie, la creencia 2 cae y la oportunidad se reenmarca hacia "recuperar lo acordado" (objetivo 3).
  2. **Por qué el link y no el stage** (creencia 1, `weakened`). ¿Cómo se abre el tablero, cuánto cuesta entrar, cuánto pesan los externos y el móvil, se conocen las apps de tablero dentro de Teams y Whiteboard, y el tablero sobrevive a la reunión? → *Decisión:* si el problema es de **capacidad** (Teams no lo resuelve), de **acceso o descubrimiento** (existe y no se usa o no se conoce), o de que el tablero **vive afuera por la memoria del equipo** (ningún arreglo en la reunión lo trae de vuelta).
  3. **Recuperar lo acordado** (reenmarque alternativo). Después de la reunión, ¿dónde terminan los acuerdos, cuánto tiempo le cuesta al Team Lead pasarlos y qué usa hoy para capturarlos (notas de Teams, Facilitator/Copilot)? → *Decisión:* si la creencia 2 cae, ¿el problema alternativo es grande en este segmento, o ya lo cubre Facilitator para quienes tienen Copilot?
- **Encuestados:** Team Leads y mandos medios que convocan y conducen reuniones, en empresas de tecnología con operación en 3+ países que usan Teams como herramienta principal de reuniones, y que en el último mes organizaron al menos una reunión de más de 5 personas en la que se compartió un tablero externo. El filtro deja fuera a quien solo participa ([[ricardo-melnick]]); R1 deja fuera de las entrevistas a externos y consultores ([[tomas-iriarte]]). El plan Business Premium no se filtra (los encuestados no suelen saberlo): en CS viene dado por la cuenta (campo oculto `cuenta`); en el panel queda como supuesto.
- **Duración estimada:** 5 preguntas de filtro + 12 preguntas + 3 de opt-in, ~6 min.
- **Límite conocido:** sale antes de cualquier entrevista real. Las opciones de respuesta vienen de las personas sintéticas y del research secundario, así que son hipótesis: todas las cerradas llevan "Otro" o "No sé", y un "Otro" frecuente es un hallazgo en sí mismo. La encuesta dice *cuántos*; los *por qué* van a `/design-interview`.

## Filtro

S1. En el último mes, ¿cuántas reuniones de más de 5 personas organizaste tú (enviaste la invitación y condujiste la reunión)? [opción única]
   - Ninguna · 1–2 · 3–5 · 6–10 · Más de 10
   → descalificar si "Ninguna"

S2. ¿Qué herramienta usa tu empresa principalmente para reuniones internas? [opción única]
   - Microsoft Teams · Zoom · Google Meet · Otra
   → descalificar si no es "Microsoft Teams"

S3. ¿En qué industria está tu empresa? [opción única]
   - Tecnología / software · Servicios financieros · Retail / consumo · Manufactura / logística · Salud · Otra
   → descalificar si no es "Tecnología / software"

S4. ¿En cuántos países opera tu empresa? [opción única]
   - 1 · 2 · 3–5 · Más de 5 · No sé
   → descalificar si "1", "2" o "No sé"

S5. En el último mes, en alguna reunión que tú organizaste, ¿alguien compartió un tablero digital (Miro, Mural, FigJam, Lucidspark u otro parecido)? [opción única]
   - Sí · No · No sé
   → descalificar si "No" o "No sé"

> S3 y S4 se mantienen también en el link de CS (la cuenta ya es del segmento) para que ambos canales sean comparables.

## Preguntas

Q1. En un mes típico, ¿en cuántas de las reuniones que organizas se usa un tablero digital? [opción única]
   - 1–2 · 3–5 · 6–10 · Más de 10
   > Goal: 1 — frecuencia, para ponderar "la última reunión" y dimensionar

*Las preguntas Q2 a Q11 se refieren a **la última reunión que organizaste en la que se usó un tablero digital**.*

Q2. ¿Qué tipo de reunión era? [opción única]
   - Retrospectiva · Planning o refinamiento · Taller o lluvia de ideas · Seguimiento o revisión de estado · Reunión con clientes o personas externas · Otra: ___
   > Goal: 1 — cortar la co-edición por tipo de reunión

Q3. Durante esa reunión, ¿cuántas personas, contándote a ti, agregaron, movieron o votaron algo en el tablero? [opción única]
   - Nadie, solo se miró · Solo yo · 2–3 · 4–6 · 7 o más · No sé
   > Goal: 1 — **pregunta central de la creencia 2**

Q4. ¿Qué se hizo en el tablero durante esa reunión? [selección múltiple]
   - Agregar ideas o notas · Agrupar u ordenar notas · Votar o priorizar · Revisar contenido que ya estaba (sin cambiarlo) · Anotar acuerdos o tareas · Otro: ___
   > Goal: 1 — qué se hace en el artefacto; "Revisar contenido" solo = consulta

Q5. ¿Cómo vieron el tablero los participantes? [selección múltiple]
   - Cada uno abrió el link en su navegador · Yo compartí pantalla mostrando el tablero · Lo abrimos dentro de la reunión de Teams (app de Miro/Mural/FigJam agregada a la reunión o "compartir en el escenario") · Otra: ___ · No sé
   > Goal: 2 — link vs. stage en la práctica

Q6. Desde que se compartió el tablero hasta que todos los que debían estar dentro lo estuvieron, ¿cuánto tiempo pasó, aproximadamente? [opción única]
   - Menos de 1 minuto · 1–3 minutos · 3–5 minutos · 5–10 minutos · Más de 10 minutos · No sé
   > Goal: 2 — minutos de peaje de acceso

Q7. En esa reunión, ¿pasó alguna de estas cosas? [selección múltiple]
   - Alguien tuvo que pedir acceso al tablero · Alguien entró como anónimo o invitado · Alguien no logró entrar · Alguien conectado desde el celular no pudo editar · Participó gente externa a la empresa · Ninguna de estas · Otra: ___
   > Goal: 2 — peso de las fricciones de acceso, externos y móvil

Q8. ¿Cuánto has usado cada una de estas opciones de Teams en los últimos 3 meses? [matriz, una respuesta por fila]
   - Filas: (a) Whiteboard de Microsoft dentro de una reunión · (b) Abrir un tablero de Miro, Mural o FigJam *dentro* de la reunión de Teams (app agregada a la reunión o "compartir en el escenario") · (c) Notas de la reunión de Teams (notas compartidas que todos pueden editar) · (d) Facilitator o el resumen automático de Copilot en la reunión
   - Columnas: No sabía que existía · Sabía, pero no la he probado · La probé y dejé de usarla · La uso a veces · La uso habitualmente · No la tenemos disponible
   > Goal: 2 (filas a–b: descubrimiento vs. abandono) y 3 (filas c–d: ¿la captura ya está cubierta por lo nativo?)

Q9. Después de esa reunión, ¿qué pasó con el tablero? [opción única]
   - Se sigue usando en próximas reuniones (acumula el trabajo del equipo) · Se pasó lo importante a otro lugar y el tablero quedó sin uso · Quedó ahí, sin uso · No sé · Otro: ___
   > Goal: 2 — ¿el tablero vive afuera por razones ajenas a la reunión? (y 3)

Q10. ¿Dónde quedaron registrados los acuerdos o tareas de esa reunión? [selección múltiple]
   - Jira u otra herramienta de tickets · Un documento (Confluence, Word, Loop, Notion, Google Docs) · Un mensaje en el chat de Teams o un correo · Las notas o el resumen automático de Teams/Copilot · Quedaron solo en el tablero · No se registraron · No hubo acuerdos que registrar · Otro: ___
   > Goal: 3 — destino de lo acordado

Q11. Después de esa reunión, ¿cuánto tiempo dedicaste tú a pasar lo acordado a otro lugar? [opción única]
   - Nada: no hacía falta · Nada: lo hizo otra persona · Menos de 10 minutos · 10–20 minutos · 20–40 minutos · Más de 40 minutos · No recuerdo
   > Goal: 3 — minutos de peaje posterior (contrasta con los 25–35 min sintéticos de [[camila-ferreyra]])

Q12. ¿Qué es lo más difícil de lograr que tu equipo trabaje junto en vivo durante una reunión? [abierta, opcional]
   > Goal: 1, 2 y 3 — temas que no anticipamos; insumo para las entrevistas

## Filtro + opt-in (reclutamiento para entrevistas)

R1. ¿Cuál es tu relación con la empresa en la que trabajas? [opción única]
   - Empleado/a · Contratista o consultor/a externo/a · Otra
   → no es candidato/a si no es "Empleado/a"

R2. ¿Aceptarías una conversación de 30 minutos sobre este tema? [sí / no]

R3. Si respondiste que sí, ¿cómo te podemos contactar? [abierta, opcional — solo se muestra si R2 = sí]

> Panel: el contacto se hace por la mensajería de re-contacto del proveedor, según sus términos; R3 solo se muestra en el link de CS.
> Prioridad de entrevista (para `/analyze-survey`): primero quienes **contradicen** las creencias — Q3 = "Nadie" o "Solo yo"; Q5 incluye "dentro de la reunión de Teams" o Q8b = "La uso habitualmente"; Q9 = "Se sigue usando"; Q11 = "Nada: no hacía falta".

## Distribución

| Canal | A quién llega y su sesgo | Alcance aprox. | Link |
|---|---|---|---|
| Correo vía Customer Success: los account managers del segmento envían la encuesta a sus contactos y les piden reenviarla a sus Team Leads | Cuentas del segmento (Business Premium, tech, 3+ países). **Sesgo:** canal propio y con intermediarios; llega sobre todo a contactos de TI (tipo [[nadia-espinoza]]) y a cuentas con buena relación comercial; sobrerrepresenta a los satisfechos y deja fuera a las cuentas sin account manager. El reenvío interno no se controla | desconocido | `…?canal=cs&cuenta={id_cuenta}` (campo oculto por cuenta, para cortar por cuenta y cruzar con telemetría) |
| Panel externo B2B (p. ej. User Interviews o Respondent), filtrado por rol (Engineering Manager, Team Lead, jefatura) e industria tech | Team Leads sin relación con nosotros, incluidos los de cuentas insatisfechas y no-clientes que usan Teams. **Sesgo:** incentivo pagado (riesgo de respuestas apuradas: agregar una pregunta de atención si el proveedor no la trae); plan M365 no verificable; sobrerrepresenta a quienes participan en paneles | cuota comprada: 150 completas que pasen el filtro | `…?canal=panel` |

- **Meta de respuestas:** n≥200 que pasen el filtro. Cortes que importan, **≥30 cada uno**: por canal (CS vs. panel); por tipo de reunión en Q2 ("retro / planning / taller" vs. "seguimiento"); con fricción de externos o móvil en Q7; y quienes en Q3 marcan "Nadie" o "Solo yo" (la base para dimensionar el objetivo 3 si la creencia 2 cae). Por debajo de 30 por corte, los resultados son direccionales.
- **Factibilidad:** el panel aporta hasta 150; llegar a 200 depende de que CS aporte **≥50**, y su alcance es desconocido. Si el 2026-10-06 CS lleva menos de 30, hay dos salidas: subir la cuota del panel, o sumar como tercer canal una invitación dentro de Teams al organizador que pegó un link a un tablero (con su propio link).
- **Primera revisión:** 2026-10-06
- **Cierre:** al llegar a n=200 o el 2026-10-20, lo que ocurra primero.
