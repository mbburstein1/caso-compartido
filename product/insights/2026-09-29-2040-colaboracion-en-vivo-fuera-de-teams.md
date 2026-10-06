---
date: 2026-09-29
source: survey
survey_design: product/surveys/2026-09-23-1944-colaboracion-en-vivo-fuera-de-teams.md
results: product/surveys/2026-09-26-1800-respuestas-colaboracion-en-vivo-fuera-de-teams.csv
n: 210 completas (76 email · 134 panel) — 182 trabajaron fuera de Teams · 28 no
opportunity: colaboracion-en-vivo-fuera-de-teams
---

# Análisis de encuesta: trabajo colaborativo fuera de Teams en reuniones de más de 5

## Denominador y límites

| | Email (canal propio) | Panel B2B | Total |
|---|---|---|---|
| Filas en el export | 85 | 164 | 249 |
| Descalificadas en el filtro | 8 | 26 | 34 |
| Parciales (excluidas) | 1 | 4 | 5 |
| **Completas (base del análisis)** | **76** | **134** | **210** |
| Trabajaron fuera de Teams (Q1 ≠ "En ninguna") | 65 | 117 | 182 |
| No trabajaron fuera (Q1 = "En ninguna") | 11 | 17 | 28 |

- **Campo:** 23/09 12:39 → 25/09 09:39. Cerró antes de lo planeado (26/09).
- **Tasa de respuesta:** no se puede calcular para el email: el alcance quedó `unknown` en el diseño y no se confirmó. El panel entregó 134 completas de una cuota de 150.
- **Metas del diseño:**
  - ≥150 que trabajan fuera: **cumplida (182)**.
  - ≥30 que no trabajan fuera: **no cumplida (28)**. Ese grupo es **direccional**.
  - ≥30 por canal: cumplida (76 y 134).
  - El email tenía que aportar ~150 y aportó 76. La muestra queda cargada al panel (64%).
- **Sesgos de canal:** el email sobrerrepresenta a quienes están conformes con Teams. El panel suma panelistas profesionales y su firmografía es autodeclarada. Ninguna cifra representa al segmento completo: todo lo que sigue es una **muestra autoseleccionada**, útil para ver patrones y dimensiones gruesas, no para estimar prevalencias con precisión.
- **Calidad:** 9 completas tardaron menos de 90 s. Sacarlas no mueve ninguna cifra clave (artefacto preexistente 53% → 52%; ≥5 min de acceso 28% → 27%), así que se mantienen. 4 respuestas repiten la misma opción en toda la matriz de Q10.
- **Subgrupos con n < 30, siempre direccionales:** los que no salen (28), los que abrieron la herramienta como app dentro de Teams (15) y los comentarios sobre compliance (5).
- **Unidad de medida:** Q2–Q9 describen *la última reunión* en que el grupo trabajó fuera, no todas. Los porcentajes de Q2–Q9 son sobre 182.

### Diferencias entre canales (hablan de la muestra antes que del segmento)

| Indicador | Email | Panel |
|---|---|---|
| Q1: salen en más de la mitad o en todas | 21% | 40% |
| Q4: el artefacto ya existía | 43% | 59% |
| Q8: con 2 o más externos | 5% | 16% |
| Q9: lo decidido quedó en el chat o las notas de Teams | 23% | 7% |
| Q10 IA: "no sabía que existía" | 5% | 16% |

El canal propio reporta menos salidas, más registro dentro de Teams y más conocimiento de las funciones nativas, que es lo que el diseño anticipaba de su sesgo. Por eso los hallazgos de abajo se apoyan en patrones que se repiten **en los dos canales**. Cuando un hallazgo aparece en uno solo, se indica.

---

## O1. Origen del artefacto: ¿se crea para la reunión o ya vivía afuera?

**Qué creíamos.** Creencia 1 del overview: el Team Lead saca el trabajo porque Teams no le resuelve colaborar en vivo, no porque el artefacto ya viva afuera. Ya estaba `weakened` por la investigación secundaria.

**Qué muestran los datos.**

| Q4 (n=182) | % |
|---|---|
| Ya existía y se siguió usando | 51% |
| Ya existía y no se volvió a usar | 3% |
| Se creó para la reunión y se siguió usando | 24% |
| Se creó para la reunión y no se volvió a usar | 15% |
| No lo sé | 7% |

**53% de los artefactos ya existían antes de la reunión.** Pero el promedio esconde dos mundos que casi no se tocan. El corte lo da Q2: si se usó una pizarra (Miro, Mural, FigJam o Lucidspark) o no.

| | Pizarra (n=61, 34%) | Sistema de registro (n=121, 66%) |
|---|---|---|
| Herramientas típicas | Miro, FigJam, Mural | Google Docs, Jira, dashboards, Confluence, Notion |
| Artefacto creado para la reunión | **82%** | 18% |
| Artefacto preexistente | 13% | **74%** |
| Qué hace el grupo (Q5) | aportar ideas 57%, votar 52%, agrupar 49% | revisar datos 51%, editar documento 40%, actualizar tickets 38% |
| ≥5 min hasta que todos entran | 49% | 17% |

Herramientas de Q2 (multirrespuesta, n=182): Google Docs/Sheets/Slides 32%, Jira 29%, Miro 20%, dashboard 16%, Confluence 14%, FigJam 12%, Notion 12%, Slido/Mentimeter 9%, Mural 9%, Lucidspark 4%. "Otra" 5% (Canva, ClickUp, Excel en SharePoint, Retrotool, Trello): la lista está completa.

**Qué decisión sigue.** El mecanismo de la creencia 1 ("salgo porque Teams no me deja colaborar en vivo") describe a un tercio de los casos: el de las pizarras creadas para la reunión. En los otros dos tercios el trabajo vive en Jira, Docs o un dashboard antes y después de la reunión, y según la regla de decisión del diseño ese es un **problema de integración** con los sistemas donde ya está el trabajo, no de colaboración en vivo. Cualquier solución de "colaboración en vivo" tiene que acotarse al mundo pizarra. El mundo sistema necesita otra hipótesis.

## O2. Costo de acceso: minutos, gente afuera, peso de los externos

**Qué creíamos.** Entrar cuesta ≥5 minutos (umbral tomado de la persona Paulina, sintética). Si la fricción se concentra en reuniones con externos, es otro segmento.

**Qué muestran los datos (n=182).**

- **Q6, tiempo hasta que todos entran:** <1 min 19% · 1–2 min 27% · 3–4 min 20% · 5–9 min 21% · 10+ min 6% · no sé 7%. **28% llega o supera los 5 minutos.** Para la mayoría (66%) es menos.
- **Q7:** en **51% de los casos al menos una persona no logró entrar** y siguió mirando la pantalla de otro. En 23% fueron dos o más.
- **Corte por externos (Q8):**

| | ≥5 min | Alguien quedó afuera |
|---|---|---|
| Con externos (n=39) | **62%** | 64% |
| Sin externos (n=137) | 18% | **46%** |

- **Corte por vía de acceso (Q3):**

| Q3 | n | ≥5 min | Alguien afuera |
|---|---|---|---|
| Enlace pegado en el chat | 98 (54%) | 32% | 48% |
| Ya la tenían abierta | 40 (22%) | 15% | 42% |
| Pantalla compartida, cada uno la abre | 28 (15%) | 25% | 50% |
| **App dentro de la reunión de Teams** | **15 (8%)** | 40% | **87%** |

Esa última fila es **direccional (n=15)**, pero va contra lo esperado: la vía integrada no deja a menos gente afuera.

**Punto ciego de la telemetría.** 46% de los casos no pasó por un enlace en el chat (ya abierta, pantalla compartida o app). La telemetría de "link pegado" subestima cuánto se trabaja afuera.

**Qué decisión sigue.**
- El **umbral de 5 minutos no describe la reunión interna típica** (18%). Sí describe la reunión con externos (62%) y la de pizarra (49%). Según la regla del diseño, la demora larga es mayormente un problema de consultoras y agencias, no del Team Lead con su equipo.
- Pero **dejar a alguien afuera sí es interno**: pasa en casi la mitad de las reuniones sin externos. Es la señal de la persona Ricardo (el que se vuelve espectador), no la de Paulina (el que pierde minutos esperando). La métrica de acceso a perseguir es "cuántos no entran", no "cuántos minutos".

## O3. Qué se hace afuera y dónde queda la decisión

**Qué hace el grupo (Q5, multirrespuesta, n=182):**

| Actividad | % |
|---|---|
| Votar o priorizar | 40% |
| Editar un documento entre varios | 35% |
| Revisar datos o métricas | 34% |
| Anotar decisiones o acuerdos | 33% |
| Aportar ideas o notas | 29% |
| Actualizar tareas o tickets | 25% |
| Agrupar u ordenar ideas | 22% |
| Dibujar un diagrama | 13% |
| Otro | 5% |

"Otro" incluye revisar incidentes, armar el roadmap, planning poker, estimar historias y revisar el presupuesto. La lista está completa. Por mundo, la pizarra se usa para divergir y converger (ideas, agrupar, votar) y el sistema de registro para revisar y actualizar.

**Dónde quedó lo decidido (Q9, multirrespuesta, n=182):**

| Registro | % |
|---|---|
| **No quedó registrado en ningún lado** | **24%** |
| Chat fuera de Teams (Slack, WhatsApp) | 23% |
| Jira u otro gestor | 23% |
| **Otro** | **18%** (supera el umbral de 15%) |
| ↳ resumen o recap de IA (Copilot, recap de Teams) | 12% (21 menciones) |
| ↳ transcripción o grabación | 3% |
| ↳ OneNote, Loop, cuaderno, nota de voz | 3% |
| En la misma herramienta externa | 15% |
| En el chat o las notas de la reunión de Teams | 13% (email 23% · panel 7%) |
| Documento de actas | 12% |
| Correo | 10% |
| No se tomaron decisiones | 7% |

**La lista de Q9 estaba incompleta.** Faltaba "en el resumen de IA", y así lo pide la nota de método. Los verbatims de esa opción son casi todos de desconfianza: *"En el recap de Copilot, que resume todo pero no distingue lo decidido"*, *"En el resumen del asistente de IA pero con errores"*, *"En el recap pero le faltaba quién hacía qué"*.

**Lo más difícil para trabajar juntos y decidir (Q11, abierta: 95 de 210 respondieron). Temas codificados, una respuesta puede tener más de uno:**

| Tema | Menciones | Evidencia |
|---|---|---|
| **Que lo decidido sobreviva: registro, seguimiento, continuidad entre reuniones** | **35 (37%)** | "Lo más difícil no es decidir, es que después se haga lo que se decidió. Dos semanas después cada uno se acuerda distinto" (R-022, email) · "Tuvimos un release que salió con el alcance viejo porque la decisión quedó en un comentario" (R-144, panel) |
| Fuera del alcance (husos horarios, idioma, demasiadas reuniones, audio, "no hay problema") | 16 (17%) | "Honestamente la mayoría de estas reuniones podrían ser un mail" (R-157) |
| Converger: votar, priorizar, cerrar | 12 (13%) | "Divergir es fácil, todos tiran ideas. Ordenarlas y elegir es lo que nos cuesta" (R-011) · "Usamos reacciones en el chat pero nadie sabe cuántos votaron ni qué ganó" (R-053) |
| Entrar a la herramienta externa (externos, permisos, SSO) | 12 (13%) | "Con la agencia externa perdemos 5 o 10 minutos solo en que entren al FigJam" (R-072) · "Los permisos del Miro. Siempre hay alguien que no puede editar y pierde los primeros 10 minutos" (R-244) |
| Carencias de la pizarra de Teams | 12 (13%) | "Probamos la whiteboard de Teams hace un tiempo, no tenía plantillas ni votación y a la retro siguiente no la encontramos. Desde ahí todo en Miro" (R-113) |
| ↳ la pizarra nativa no se encuentra la semana siguiente | 5 | "Está colgada del chat de esa reunión y si la serie cambió la perdí" (R-065) |
| Participación y dinámica (hablan los mismos, cámaras apagadas) | 11 (12%) | "Hay 12 personas y opinan 3, el resto escucha o está en otra cosa" (R-049) |
| Compliance o regulación limita las herramientas externas | 3 (+2 en Q12) | "Compliance no nos deja meter datos de clientes en Miro, así que o lo hacemos en Teams o no se hace. Y en Teams cuesta" (R-190) |
| El resumen de IA no distingue lo decidido de lo conversado | 3 (+~10 en Q9) | "El resumen de IA me ayuda pero marca como decisión cosas que eran solo ideas, lo tengo que revisar siempre" (R-153) |

El tema de registro y continuidad aparece con fuerza parecida en los dos canales (14 de email, 21 de panel) y también entre los que no salen (6 de 15).

**Qué decisión sigue.** Cualquier solución tiene que cubrir **converger** (votar y priorizar: 40% de los casos, 13% de las menciones abiertas) y, sobre todo, **lo que pasa con la decisión después de la reunión**. Ahí está el dolor más repetido de la encuesta y el lugar más claro para la IA: no para resumir (eso ya existe y lo usa 36%), sino para separar lo decidido de lo conversado, con responsable y fecha, y retomarlo en la próxima reunión de la serie.

## O4. Conocimiento y uso de lo nativo: "no me sirve" vs. "no sé que existe"

Q10, n=210:

| Función | No sabía que existía | Sé que existe, nunca la usé | La usé y la dejé | La uso a veces o en la mayoría |
|---|---|---|---|---|
| Whiteboard | 8% | 27% | **43%** | 21% |
| Notas de la reunión (Loop) | **31%** | 28% | 14% | 27% |
| Apps de otras herramientas en la reunión | **40%** | 28% | 9% | 23% |
| Resumen o asistente de IA | 12% | 39% | 13% | **36%** |

Los que no salen (n=28, direccional) muestran el mismo perfil: 50% dejó Whiteboard y 43% no conocía las apps.

**Qué decisión sigue.**
- **Whiteboard es un "no me sirve".** Casi todos la conocen y el 43% la probó y la abandonó. Las razones abiertas son concretas: no permite votar ni agrupar, no tiene plantillas, se traba con más de 8 personas y no se encuentra la semana siguiente.
- **Las apps dentro de la reunión y Loop son un "no sé que existe".** Sumando "no sabía" y "nunca la usé", llegan al 68% y al 59%.

Son dos palancas distintas: arreglar un producto por un lado, hacerlo visible por el otro. Hay una advertencia: la poca gente que sí usa la app integrada no reporta menos fricción de acceso (O2, n=15). Hacer visibles las apps no es suficiente sin entender por qué fallan.

---

## Insights, priorizados por impacto

## 1. El dolor más repetido está después de la reunión: la decisión no sobrevive, y el resumen de IA no alcanza

En 24% de las últimas reuniones lo decidido no quedó en ningún lado y en otro 23% quedó en un chat fuera de Teams. Es el tema abierto más mencionado (37% de las respuestas a Q11), parejo en los dos canales y presente también entre los que no salen. Quienes confían la decisión al recap de IA (12%, una opción que el cuestionario no ofrecía) dicen que el recap no separa lo decidido de lo conversado ni asigna responsable. Esto reordena la oportunidad: además de, o antes que, colaborar en vivo, está **recuperar lo acordado**, que la agenda de investigación ya tenía como reencuadre posible. La capacidad de IA a explorar es una captura de decisiones con responsable y fecha, que se retome en la reunión siguiente de la serie.

> Evidencia: "Muchas veces creemos que decidimos y en realidad cada uno entendió algo distinto. Lo descubrimos en la siguiente reunión" — R-099 (panel) · "Tenemos la grabación y el resumen de Copilot pero el resumen pone todo al mismo nivel, no se distingue qué se decidió y qué se habló nomás" — R-109 (panel)

## 2. "Salir de Teams" son dos problemas: pizarras ad hoc (un tercio) y sistemas de registro que ya existían (dos tercios)

En 66% de los casos el grupo trabajó sobre Docs, Jira, un dashboard o Confluence que ya existían (74% preexistentes) para revisar datos y actualizar tickets. Ese caso es de integración y no se resuelve con colaboración en vivo. Solo el 34% usó una pizarra, casi siempre creada para esa reunión (82%), para aportar ideas, agrupar y votar. La creencia 1 solo aplica a ese tercio. La oportunidad debería partirse, o acotar explícitamente su segmento al mundo pizarra, antes de pasar a una spec.

> Evidencia: pizarra → artefacto creado para la reunión 82% · sistema de registro → preexistente 74% (Q2 × Q4, n=182, patrón presente en ambos canales)

## 3. La fricción de acceso es "alguien queda afuera", no "cinco minutos esperando"

El umbral de ≥5 minutos solo se cumple en 18% de las reuniones internas. Sube a 62% con externos y a 49% con pizarras. En cambio, en 46% de las reuniones **sin externos** al menos una persona no logra entrar y termina mirando la pantalla de otro. Eso es un problema del Team Lead con su propio equipo (el perfil de Ricardo) y sugiere medir "participantes que no entran" en vez de minutos. La vía integrada (app dentro de Teams) no muestra mejor resultado (87% con alguien afuera, n=15, direccional).

> Evidencia: "Algunos no saben usar Miro y se quedan mirando. Pierdo gente en el camino" — R-147 (email) · "Que los que se conectan desde el celular participen. Ven todo chiquito y no pueden hacer nada" — R-079 (panel)

## 4. Whiteboard se probó y se abandonó por razones concretas; las apps integradas ni se conocen

43% dejó Whiteboard. Las razones abiertas convergen: sin votación ni agrupación, sin plantillas, lenta con muchos participantes y, sobre todo, **no se encuentra después** porque queda colgada del chat de una reunión puntual. Esa última razón conecta con el insight 1: en Miro "el tablero tiene un link fijo" y guarda la continuidad entre reuniones. Las apps de terceros dentro de la reunión las desconoce 40%. Si se trabaja sobre lo nativo, las palancas son persistencia ligada a la serie de reuniones y mecanismos para converger, no más funciones de dibujo.

> Evidencia: "Si usamos la pizarra nativa después nadie la encuentra. En Miro por lo menos el tablero tiene un link fijo" — R-218 (email) · "El whiteboard no deja ordenar ni votar, es una hoja en blanco y ya" — R-239 (panel)

## 5. Señal débil: para algunos, compliance hace que Teams sea la única opción

Cinco respuestas (3 en Q11 y 2 en Q12, entre ellos respondentes de España y Colombia) cuentan que compliance o la normativa europea les prohíbe usar Miro o FigJam con datos de clientes, así que colaboran en Teams "o no se hace". Es poco para dimensionar, pero es el grupo con la necesidad más pura y enlaza con la restricción de Nadia (gobierno de datos). Vale la pena entrevistarlo.

> Evidencia: "Con la normativa europea tenemos las herramientas externas muy limitadas. Lo que hay dentro de Teams tendría que funcionar mejor" — R-173 (panel)

---

## "Por qué" abiertos: candidatos para entrevistas

1. ¿Por qué la decisión no queda registrada? ¿Falta de responsable, de herramienta o de costumbre? ¿Qué haría confiable un registro automático?
2. ¿Por qué la vía integrada (app dentro de Teams) deja a más gente afuera? ¿Permisos, licencias, celular?
3. ¿Qué hace que la pizarra nativa "no se encuentre"? ¿Cómo manejan hoy la continuidad entre reuniones de una serie?
4. Entre los que no salen: ¿no lo necesitan, o no pueden (compliance)? ¿Dónde y cómo se toma después la "decisión real" en el grupo chico (R-073, R-207)?
5. En el mundo sistema de registro, ¿qué se pierde al trabajar sobre Jira o un dashboard compartido? (R-036: "Cada uno abre el dashboard con su filtro y estamos hablando de números distintos")

## Pool de reclutamiento (opt-in)

- 77 aceptaron una conversación (R3 = Sí). Se descartan 6 que administran M365 (R1) y 9 que conducen 0–1 reuniones grandes por semana (R2).
- Quedan **64 candidatos, 58 con contacto**. Los contactos están en el CSV de resultados.
- Etiquetas según el diseño: contradice si Q1 = "En ninguna", si Q4 = "Ya existía…" o si Q6 < 3 min. **47 de 64 contradicen al menos una creencia.**

**Primero: contradicen (orden sugerido)**

| Prioridad | Grupo | Candidatos |
|---|---|---|
| 1 | No salen (Q1 "En ninguna") — incluye los dos casos de compliance | **R-009** y **R-143** (compliance), R-046, R-153 (desconfía del resumen de IA), R-120, R-085, R-088, R-110 (sin contacto), R-135, R-170, R-196, R-242 |
| 2 | Artefacto preexistente **y** acceso < 3 min (contradicen dos creencias) | R-036, R-094, R-131, R-144 (release con alcance viejo), R-176, R-229, R-240, R-247, R-180, R-234, R-102, R-151, R-224, R-057, R-128, R-194 (sin contacto), R-235 |
| 3 | Solo artefacto preexistente | R-065, R-227 (sin contacto), R-244, R-042, R-171, R-086, R-132 (sin contacto), R-201, R-228, R-238, R-159 |
| 4 | Solo acceso < 3 min | R-074, R-089, R-230, R-013, R-090, R-093, R-173 (normativa europea) |

**Después: no contradicen (17), como contraste.** Confirmadores más claros (pizarra + acceso ≥5 min o externos): R-024 (pasa una hora del FigJam a Jira), R-031, R-077, R-097, R-101, R-103, R-113 (abandonó Whiteboard), R-205, R-245 (sin contacto). Resto: R-011, R-019, R-038, R-070, R-099, R-204, R-006, R-076 (sin contacto).

Para una ronda de 8–12 entrevistas: 3–4 del grupo 1, 3–4 del grupo 2 y 2–3 confirmadores, balanceando canal y país.
