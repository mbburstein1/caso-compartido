---
opportunity: colaboracion-en-vivo-fuera-de-teams
research: product/research/2026-09-16-0115-colaboracion-en-vivo-fuera-de-teams.md
beliefs: 1, 2, 4, 5, 6 (product/overview.md)
date: 2026-09-22
---

# Encuesta: el trabajo en vivo sobre tableros externos en reuniones de Teams

- **Objetivos de aprendizaje:**
  1. **Co-edición vs. consulta** (creencia 2). ¿En cuántas reuniones con tablero externo editan dos o más personas y en cuántas solo se consulta? ¿Cambia según el tipo de reunión? → *Decisión:* si predomina la consulta, la oportunidad se reenmarca hacia "recuperar lo acordado".
  2. **Por qué el link y no el stage** (creencia 1, `weakened`). ¿Cuánto cuesta entrar al tablero? ¿Cuánto pesan los externos y el móvil? ¿Conocen o probaron Whiteboard y la app en la reunión? ¿El tablero sobrevive a la reunión? → *Decisión:* si el problema es de capacidad, de acceso o descubrimiento, o de que el artefacto vive afuera por la memoria del equipo.
  3. **Quién paga y cuántos facilitan** (creencias 4, 5 y 6). ¿Quién paga hoy la herramienta externa? ¿Cuántas personas conducen sesiones por equipo? ¿El Team Lead ya actuó ante TI? → *Decisión:* cobrar por facilitador o por usuario, y si el Team Lead origina la compra o solo la sufre.
- **Encuestados:** Team Leads y mandos medios que convocan y conducen reuniones, en empresas de tecnología con operación en 3+ países que usan Teams como herramienta principal de reuniones, y que en el último mes organizaron al menos una reunión de más de 5 personas en la que se compartió un tablero externo. El filtro deja fuera a quien solo participa ([[ricardo-melnick]]). La pregunta R1 deja fuera de las entrevistas a los externos ([[tomas-iriarte]]). El plan Business Premium no se filtra en la encuesta porque los encuestados no suelen saber qué plan tienen. En CS viene dado por la cuenta; en el panel queda como supuesto.
- **Duración estimada:** 5 preguntas de filtro + 12 preguntas + 3 de opt-in, ~5 min. El tamaño de empresa no se pregunta: sale del perfil del panel y, en CS, de la cuenta (campo oculto `cuenta`).
- **Límite conocido:** esta encuesta sale antes de las entrevistas reales. Las opciones de respuesta vienen de las personas sintéticas y del research secundario, así que son hipótesis. Por eso todas las preguntas cerradas tienen "Otro" o "No sé", y un "Otro" frecuente es un hallazgo en sí mismo.

## Filtro

S1. En el último mes, ¿cuántas reuniones de más de 5 personas organizaste tú (tú enviaste la invitación y condujiste la reunión)? [opción única]
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

S5. En el último mes, en alguna reunión que tú organizaste, ¿alguien compartió un link a un tablero (Miro, Mural, FigJam, Lucidspark u otro parecido)? [opción única]
   - Sí · No · No sé
   → descalificar si "No" o "No sé"

> Nota: S3 y S4 se pueden omitir en el link de CS (la cuenta ya es del segmento), pero conviene mantenerlos para que ambos canales sean comparables.

## Preguntas

Q1. En un mes típico, ¿en cuántas de las reuniones que organizas se usa un tablero externo (Miro, Mural, FigJam u otro)? [opción única]
   - 1–2 · 3–5 · 6–10 · Más de 10
   > Goal: 1 y 3 — frecuencia, para dimensionar

*Las preguntas Q2 a Q7 se refieren a **la última reunión que organizaste en la que se compartió un tablero externo**.*

Q2. ¿Qué tipo de reunión era? [opción única]
   - Retrospectiva · Planning o refinamiento · Taller o lluvia de ideas · Seguimiento o revisión de estado · Reunión con clientes o personas externas · Otra: ___
   > Goal: 1 — cortar la co-edición por tipo de reunión

Q3. Durante esa reunión, ¿cuántas personas, contándote a ti, agregaron, movieron o votaron algo en el tablero? [opción única]
   - Nadie, solo se miró · Solo yo · 2–3 · 4–6 · 7 o más · No sé
   > Goal: 1 — **pregunta central de la creencia 2**

Q4. ¿Cómo vieron el tablero los participantes? [selección múltiple]
   - Cada uno abrió el link en su navegador · Yo compartí pantalla mostrando el tablero · Lo abrimos dentro de la reunión de Teams (app de Miro/Mural/FigJam, "compartir en el escenario") · Otra: ___ · No sé
   > Goal: 2 — link vs. stage en la práctica

Q5. Desde que se compartió el tablero hasta que todos los que debían estar dentro lo estuvieron, ¿cuánto tiempo pasó, aproximadamente? [opción única]
   - Menos de 1 minuto · 1–3 minutos · 3–5 minutos · 5–10 minutos · Más de 10 minutos · No sé
   > Goal: 2 — minutos de peaje de acceso

Q6. En esa reunión, ¿pasó alguna de estas cosas? [selección múltiple]
   - Alguien tuvo que pedir acceso al tablero · Alguien entró como anónimo o invitado · Alguien no logró entrar · Alguien conectado desde el celular no pudo editar · Participó gente externa a la empresa · Ninguna de estas · Otra: ___
   > Goal: 2 — peso de las fricciones de acceso, externos y móvil (+ segmento ≥30 con externos/móvil)

Q7. Después de esa reunión, ¿qué pasó con el tablero? [opción única]
   - Se usa de nuevo en próximas reuniones (acumula el trabajo del equipo) · Se pasó lo importante a otro lugar (Jira, un documento) y el tablero quedó sin uso · Quedó ahí, sin uso · No sé · Otro: ___
   > Goal: 2 — ¿el tablero vive afuera por razones ajenas a la reunión?

Q8. ¿Cuánto has usado cada una de estas opciones de Teams en los últimos 3 meses? [matriz, una respuesta por fila]
   - Filas: (a) Whiteboard de Microsoft dentro de una reunión · (b) Abrir un tablero de Miro, Mural o FigJam *dentro* de la reunión de Teams (app agregada a la reunión, "compartir en el escenario")
   - Columnas: No sabía que existía · Sabía, pero no la he probado · La probé y dejé de usarla · La uso a veces · La uso habitualmente
   > Goal: 2 — descubrimiento vs. abandono (capacidad vs. acceso)

Q9. ¿Quién paga la herramienta de tablero que más usa tu equipo? [opción única]
   - TI, con una licencia corporativa · Mi área, con presupuesto propio · Alguien con tarjeta corporativa o reembolso de gastos · Usamos un plan gratuito · No sé · Otro: ___
   > Goal: 3 — quién compra hoy

Q10. En tu equipo, ¿cuántas personas crean o conducen sesiones en el tablero (no solo participan)? [opción única]
   - Solo yo · 2 · 3–5 · 6 o más · No sé
   > Goal: 3 — facilitadores por equipo: precio por facilitador vs. por usuario

Q11. En los últimos 12 meses, ¿hiciste alguna de estas cosas? [selección múltiple]
   - Pedí a TI una herramienta para colaborar en reuniones · Pagué, o pedí a mi área que pagara, una herramienta de tablero · Pedí a TI que habilitara una app dentro de Teams · Reporté a TI o a Microsoft un problema de colaboración en reuniones · Ninguna de estas · Otra: ___
   > Goal: 3 — ¿el Team Lead actúa sobre el problema (creencia 4) y empuja la compra (creencias 5 y 6)?

Q12. ¿Qué es lo más difícil de lograr que tu equipo trabaje junto en vivo durante una reunión? [abierta, opcional]
   > Goal: 1 y 2 — temas que no anticipamos; insumo para las entrevistas

## Filtro + opt-in (reclutamiento para entrevistas)

R1. ¿Cuál es tu relación con la empresa en la que trabajas? [opción única]
   - Empleado/a · Contratista o consultor/a externo/a · Otra
   → no es candidato/a si no es "Empleado/a"

R2. ¿Aceptarías una conversación de 30 minutos sobre este tema? [sí / no]

R3. Si respondiste que sí, ¿cómo te podemos contactar? [abierta, opcional — solo se muestra si R2 = sí]

> Panel: el contacto se hace por la mensajería de re-contacto del proveedor del panel, según sus términos; R3 solo se muestra en el link de CS.
> Prioridad de entrevista (para `/analyze-survey`): primero quienes **contradicen** las creencias. Por ejemplo, Q3 = "Nadie" o "Solo yo", Q8b = "La uso habitualmente" o Q7 = "Se usa de nuevo".

## Distribución

| Canal | A quién llega y su sesgo | Alcance aprox. | Link |
|---|---|---|---|
| Correo vía Customer Success: los account managers del segmento reenvían la encuesta a sus contactos y les piden que la hagan llegar a sus Team Leads | Cuentas del segmento (Business Premium, tech, 3+ países). **Sesgo:** canal propio y con intermediarios; llega sobre todo a contactos de TI (tipo [[nadia-espinoza]]) y a cuentas con buena relación comercial; sobrerrepresenta a los satisfechos y deja fuera a las cuentas sin account manager. El reenvío interno no se controla | desconocido | `…?canal=cs&cuenta={id_cuenta}` (un campo oculto por cuenta, para cortar por cuenta y cruzar con telemetría) |
| Panel externo B2B (p. ej. User Interviews o Respondent), filtrado por rol de Engineering Manager, Team Lead o jefatura y por industria tech | Team Leads sin relación con nosotros, incluidos los de cuentas insatisfechas o de no-clientes que usan Teams. **Sesgo:** incentivo pagado (riesgo de respuestas rápidas y poco cuidadas: incluir una pregunta de atención si el proveedor no la trae); el plan M365 no es verificable; sobrerrepresenta a quienes participan en paneles | cuota comprada: 150 completas que pasen el filtro | `…?canal=panel` |

- **Meta de respuestas:** n≥200 que pasen el filtro en total; **≥30 por canal** (para comparar CS contra panel); **≥30 que en Q6 marquen "participó gente externa" o "desde el celular no pudo editar"**. Tipo de reunión (Q2): ≥30 en "retro / planning" y ≥30 en "seguimiento", para cortar Q3. Por debajo de 30 por segmento, los resultados son direccionales.
- **Factibilidad:** el panel aporta hasta 150, así que llegar a 200 depende de que CS aporte **≥50** y su alcance es desconocido. Si el 2026-10-06 CS lleva menos de 30, hay dos salidas: subir la cuota del panel o sumar la invitación dentro de Teams al organizador que pegó un link a un tablero (tercer canal, con su propio link).
- **Primera revisión:** 2026-10-06
- **Cierre:** al llegar a n=200 o el 2026-10-14, lo que ocurra primero.
