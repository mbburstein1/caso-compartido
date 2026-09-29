---
status: framed
segment: Cuentas M365 Business Premium, 100+ licencias, sector tecnología, operación en 3+ países, facturación >USD 100M anuales. 12.400 cuentas · 2,1 M licencias. Equipos distribuidos, híbrido o remoto. Las reuniones las convocan y conducen Team Leads y mandos medios.
personas: camila-ferreyra (primaria del segmento), paulina-achondo (proxy), ricardo-melnick (restricción de adopción), nadia-espinoza (guardián de la compra), tomas-iriarte (anti-persona)
---

# Oportunidad: el trabajo en vivo se hace fuera de Teams

En las cuentas de tecnología multipaís con Business Premium, el Team Lead que necesita que su equipo distribuido aporte en vivo saca el trabajo fuera de Teams —en el 38% de sus reuniones de más de cinco personas se pega un link a Miro, Mural o FigJam *durante* la llamada, y la actividad en Teams cae mientras dura— pagando un peaje de acceso y de atención en cada reunión. Importa ahora porque este segmento ya sube de plan por sobre el promedio del parque (3,1% vs 2,4%) y "colaboración" aparece en esas conversaciones de renovación.

## Segmento y personas

**Sufre el problema:** el Team Lead / mando medio que convoca y conduce. Es quien decide sacar el trabajo afuera, quien paga el peaje y quien puede empujar el caso ante TI. [[camila-ferreyra]] es la persona primaria dentro del segmento: Engineering Manager en una SaaS con Business Premium, equipo de once en cuatro países, edita el tablero en vivo en planning y retro y solo lo consulta en el resto de sus reuniones. Además, el tablero guarda la memoria del equipo entre sprints, así que pone a prueba las creencias 1 y 2 desde ambos lados. [[paulina-achondo]] se usa como portadora del mecanismo (convoca 10–14 reuniones semanales, equipo híbrido de nueve, pega el link y pierde 4–7 minutos en que la gente entre) — el mecanismo no depende del rubro.

**No es sujeto del problema, pero lo acota:** [[ricardo-melnick]]. No sufre el peaje, sufre quedar de espectador cuando el tablero se abre. Cualquier solución que le exija aprender algo nuevo muere con él dentro — entra como restricción, no como usuario objetivo.

**Guardián:** [[nadia-espinoza]] decide el plan y autoriza integraciones en el tenant. La creencia de viabilidad se prueba contra ella.

**Contraste:** [[tomas-iriarte]] (anti-persona) quiere exactamente lo contrario — que Teams ceda la colaboración a herramientas externas. Si una idea futura solo lo entusiasma a él, es mala señal.

> **Persona faltante — cubierta.** [[camila-ferreyra]] se generó con `/generate-personas` el 2026-09-16 para cubrir el hueco del segmento (tecnología, 3+ países, Business Premium). Sigue pendiente validarla contra las entrevistas reales de la agenda.

## Señales

| Señal | Procedencia | Fuente |
|---|---|---|
| En el 38% de las reuniones del segmento con >5 participantes se comparte un link a Miro/Mural/FigJam durante la llamada; la actividad en Teams cae mientras dura | `real` | telemetría (9 pts sobre el 29% del parque completo, `product/overview.md`) |
| 4.700 solicitudes de "colaboración durante reuniones" en 12 meses — 3ª categoría más frecuente del portal de feedback del segmento. Las más repetidas: editar un documento entre varios durante la llamada, votar o priorizar en vivo, no salir de Teams para una sesión de trabajo | `real` | portal de feedback |
| Whiteboard se abre en el 6% de las reuniones del segmento; en la mitad de esas se cierra antes de los 2 minutos | `real` | telemetría |
| 22% de los comentarios negativos post-reunión del segmento mencionan colaboración en vivo ("para hacer algo juntos terminamos en otra herramienta", "la pizarra es difícil de encontrar y nadie la usa", "pierdo tiempo pasando lo que decidimos a un documento después") | `survey` | encuesta post-reunión — **n no declarado** |
| 3,1% de las cuentas del segmento subió de Premium a Max en 12 meses (parque completo: 2,4%) | `unverified` | declarado en sesión, fuente sin nombrar |
| 12.400 cuentas / 2,1 M licencias en el segmento | `unverified` | declarado en sesión, fuente sin nombrar |
| "Colaboración" aparece en conversaciones de renovación de cuentas grandes sobre el plan Max | `unverified` | Ventas — sin registro de frecuencia |
| Insatisfacción post-reunión del parque: colaboración durante la reunión 19% | `unverified` | brief del caso, vía `product/overview.md` |
| Paulina pierde 4–7 min por link externo; 2 veces al mes alguien no logra entrar | `synthetic` | `product/personas/paulina-achondo.md` |
| Camila pierde ~10 min por retro conduciendo desde el navegador y 25–35 min por ceremonia pasando acuerdos a Jira; su tablero persiste entre sprints | `synthetic` | `product/personas/camila-ferreyra.md` |
| Ricardo se vuelve espectador cuando se abre un tablero colaborativo | `synthetic` | `product/personas/ricardo-melnick.md` |

## Outcome de negocio

**Upgrade de Business Premium a Business Max** (USD 8 usuario/mes). Línea base del segmento: 3,1% de cuentas en 12 meses. Es el outcome con la línea más corta al problema — si resolver la colaboración en vivo es lo que hace que el Team Lead deje de salirse, es también lo que le da argumento para empujar el upgrade ante TI.

Secundario, no perseguido en esta oportunidad: el 3,6% del parque que baja de plan o no renueva citando "pagamos por funciones que no usamos".

## Restricciones

Hechos que acotan cualquier solución futura. No son decisiones sobre ella.

- IT contrata y despliega; el usuario final no instala nada. Toda solución llega por el tenant.
- Operación en 3+ países: husos horarios y, probablemente, requisitos de residencia de datos.
- Nadia autoriza o bloquea integraciones de terceros dentro del tenant, y le inquieta que documentos de trabajo vivan fuera de su perímetro de gobierno.
- 37% de las organizaciones tiene además Slack o Google Chat activo en al menos un equipo: Teams no es el único canal.
- El escalón comercial existente es Business Max a USD 8 usuario/mes. No hay otro peldaño.
- Ricardo: alfabetización técnica baja, entra desde el celular a un tercio de sus reuniones.
- La vía de entrada de cualquier experimento es el piloto acotado con un área voluntaria, que es como Nadia despliega.

## Creencias

Referenciadas desde `product/overview.md`, el registro único de creencias.

- `[opportunity: colaboracion-en-vivo-fuera-de-teams] [value]` En la mayoría del 38% de reuniones del segmento donde se comparte un link a Miro/Mural/FigJam durante la llamada, dos o más participantes editan ese artefacto mientras dura la reunión — no solo lo consultan.
- `[opportunity: colaboracion-en-vivo-fuera-de-teams] [viability]` En las cuentas del segmento que subieron de Business Premium a Business Max en los últimos 12 meses, la conversación la inició o la justificó un mando medio con una necesidad concreta de reunión, no IT por consolidación de costo.

## Agenda de investigación

| Creencia | Instrumento | Decisión que desbloquea | Plazo |
|---|---|---|---|
| value | **Datos propios.** Cruzar telemetría de link externo con señales de edición del artefacto durante la ventana de la reunión | Si predomina la consulta y no la co-edición, la creencia #1 del overview cae y esta oportunidad se descarta — se reenmarca hacia "recuperar lo acordado" | 2 sem |
| value | **Datos propios.** ¿El convocante que cierra Whiteboard antes de 2 min es el mismo que pega el link externo en esa reunión? | Si no se solapan, son dos problemas distintos y hay que separar la oportunidad en dos | 2 sem |
| value | `/research-market` — cómo Miro/Mural/FigJam describen y monetizan el uso *dentro de la llamada* | Acota la agenda antes de gastar en campo; si el mercado ya lo resolvió, cambia el ángulo | 1 sem, en paralelo |
| value | `/design-survey` al segmento (Team Leads, n≥200): frecuencia, minutos de peaje, qué hacen en el artefacto. Con bloque de opt-in | Dimensiona el problema y recluta el pool de entrevistas | 4 sem |
| value | `/design-interview`, 8–12 Team Leads reclutados del opt-in, priorizando a quienes contradicen la creencia | Entender *por qué* se salen — insumo para `/clarify-idea` | 6 sem |
| viability | Revisión de notas de venta de las ~384 cuentas del segmento que subieron a Max + 6–8 entrevistas con quien empujó la conversación | Si el upgrade lo decide IT sola, el segmento se rediseña hacia Nadia y el problema a resolver cambia | 4 sem |

## Ideas candidatas (no evaluadas)

- "Herramientas colaborativas integradas" — de la formulación original con que llegó la oportunidad, aparcada
- Editar un documento entre varios durante la llamada — del portal de feedback
- Votar o priorizar en vivo — del portal de feedback
- Sesión de trabajo completa sin salir de Teams — del portal de feedback
- Arreglar el descubrimiento de Whiteboard ("es difícil de encontrar y nadie la usa")
