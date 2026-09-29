---
source: secondary
method: mixed
date: 2026-09-16
question: ¿El mercado ya resolvió el trabajo colaborativo en vivo dentro de la reunión de Teams? ¿Cómo lo monetiza, quién lo compra y qué evidencia pública hay de co-edición en reuniones?
opportunity: colaboracion-en-vivo-fuera-de-teams
---

# Research: colaboración en vivo dentro (y fuera) de la reunión de Teams

> **Método.** Búsqueda y lectura web, hecha el 2026-09-16 por cuatro agentes en paralelo, uno por línea: (1) competidores dentro de la llamada, (2) alternativas nativas y no-consumo, (3) pricing y quién compra, (4) tendencias y evidencia de uso. Cada afirmación lleva su procedencia. `[verificado: URL — fecha]` indica una fuente consultada. `[conocimiento del modelo — verificar]` indica que el dato viene de la memoria del modelo. "Desconocido" significa que no se encontró. **Este documento describe el mercado. No verifica creencias sobre nuestros usuarios.** "Business Max" y todos los datos internos del caso son ficticios, así que no se buscaron.

## Resumen: los hallazgos que cambian decisiones

1. **La capacidad ya existe desde 2021. Lo que falla es la adopción o el acceso.** Miro, Mural, FigJam y Lucidspark tienen apps de Teams con *Share to Stage*: el tablero se proyecta en el escenario de la reunión y los asistentes lo editan sin salir de Teams. Aun así, en el caso los Team Leads pegan el link en el chat. La causa probable no es que "Teams no permita trabajar en vivo sobre el tablero". Más bien hay fricciones documentadas:
   - La app se agrega reunión por reunión.
   - En Miro hace falta aprobación de dos administradores (Microsoft y Miro Enterprise) y un perfil en la herramienta.
   - En móvil, Miro solo permite ver.
   - La documentación sobre invitados se contradice.
   - Otra explicación posible: el tablero vive afuera por razones ajenas a la reunión.

   Esto obliga a reformular la creencia 1 antes de salir a campo.
2. **Microsoft ya cubre la parte de capturar y facilitar, pero cobra aparte por ella. Y su pizarra quedó atrás en facilitación.**
   - **Facilitator**, el agente de Copilot, ya ofrece notas coeditables, agenda con temporizador, tareas hacia Planner y un documento Word. Requiere licencia Copilot y deja fuera a los externos.
   - **Whiteboard** no tiene votación ni temporizador confiables dentro del tablero. Zoom sí los ofrece, con más de 250 plantillas y acceso para visitantes.
   - **Retiro de apps:** Microsoft retira las apps independientes de Whiteboard entre octubre y noviembre de 2026.
   - **Consecuencia:** una solución centrada en "pasar lo acordado a un documento" duplica a Facilitator. El espacio que parece libre es otro: facilitar dentro del tablero para todos (externos y móvil incluidos) y conectar lo que pasa en el tablero de terceros con la reunión.
3. **Cobrar USD 8 por usuario choca con cómo cobra el mercado.**
   - Miro, Mural, FigJam y Klaxoon cobran a quien crea o facilita, entre USD 3 y 25 al mes. Quien participa entra gratis, y en Mural, FigJam y Klaxoon también puede editar gratis.
   - USD 8 aplicado a toda la organización equivale a +36% sobre Business Premium (USD 22) y se compara con Teams Premium (USD 10), que hoy vende IA y seguridad, no lienzo colaborativo.
   - La evidencia de que la compra nace abajo es sólida, pero viene de productos PLG (crecimiento impulsado por el producto), no de Microsoft. Ejemplo: el 70% de los clientes Enterprise nuevos de Figma ya tenía un usuario pagando.

Además, **no hay evidencia pública sobre cuántos participantes co-editan y cuántos solo consultan durante una reunión.** La creencia 2 solo se resuelve con datos propios y campo.

---

## 1. Competidores directos: el tablero dentro de la reunión de Teams

**Plataforma Microsoft (base de todas las integraciones)**
- *Share to Stage* es interactivo: "All attendees can view and interact". Microsoft lo recomienda para whiteboarding en reuniones chicas. La app necesita estar instalada en la reunión y tener el permiso RSC `MeetingStage.Write.Chat`. "Anonymous users cannot initiate sharing". La tabla de clientes marca escritorio, web y móvil, pero no Mac, Teams clásico ni VDI [verificado: https://learn.microsoft.com/en-us/microsoftteams/platform/apps-in-teams-meetings/build-apps-for-teams-meeting-stage — 2026-09-16, doc actualizada 2026-02-27].
- Live Share SDK sirve para "co-watch, co-create, and co-edit". Los únicos ejemplos que da son apps de Microsoft (Whiteboard, PowerPoint Live, Loop). Tiene un tope de 100 asistentes, admite invitados excepto en reuniones de canal y no funciona en Teams Rooms [verificado: https://learn.microsoft.com/en-us/microsoftteams/platform/apps-in-teams-meetings/teams-live-share-overview y …/teams-live-share-faq — 2026-09-16, docs de 2024-05 y 2025-01].
- No existe una lista oficial de apps de terceros compatibles con stage o Live Share: **desconocido**.

**Miro**
- *Propuesta:* "share-to-stage your Miro board and collaborate live with your teammates… without having to context switch" [verificado: https://miro.com/marketplace/microsoft-teams/ — 2026-09-16].
- *Qué hace en Teams:* el tablero va en el panel lateral y se lleva al stage. "Any Teams user with a Miro profile can share a board to center stage" [verificado: https://help.miro.com/hc/en-us/articles/4411292563602 — 2026-09-16].
- *Limitaciones:*
  - Móvil: "can only view an attached Miro board and cannot edit or comment on it".
  - Invitados: Miro afirma que "Microsoft doesn't support the ability for guest users to use apps in a Teams meeting", lo que contradice la doc de Microsoft de 2026 [misma URL].
  - Doble aprobación de admin: Microsoft y Miro Enterprise [verificado: https://help.miro.com/hc/en-us/articles/4406387610002 — 2026-09-16].
- *Prueba / no prueba:* la integración mejor documentada demuestra que hay demanda. No demuestra que se use.

**Mural**
- *Propuesta:* "Add a shared digital canvas directly into any … live video meeting" y "no one's excluded" [verificado: https://www.mural.co/partners/microsoft/teams — 2026-09-16].
- *Qué hace en Teams:* share-to-stage y mural fijado en la invitación. Fuente: post de 2021 [verificado: https://www.mural.co/blog/mural-app-for-microsoft-teams — 2026-09-16].
- *Limitaciones:* invitados, móvil y admin **desconocidos**. La documentación pública es escasa y vieja.
- Se presenta como socio cercano de Microsoft (lanzó funciones de facilitación con IA en Microsoft Build) [verificado: https://www.mural.co/press-releases/mural-unveils-ai-powered-capabilities-for-enterprise-collaboration-at-microsoft-build — 2026-09-16].

**FigJam (Figma)**
- *Qué hace en Teams:* panel lateral y "Share to Stage", en la app de escritorio de Teams. En FigJam los editores trabajan "as you normally would". Con *open sessions* se puede invitar a editar "including those without Figma accounts". Los archivos de Figma Design solo admiten ver y comentar. "+ Add App" funciona únicamente en reuniones programadas [verificado: https://help.figma.com/hc/en-us/articles/7405452518423 — 2026-09-16].
- Móvil: **desconocido**.

**Lucidspark / Klaxoon / herramientas de retro**
- Lucidspark: stage en reuniones de Teams "without ever leaving Teams", según un comunicado de 2021 [verificado: https://www.prnewswire.com/news-releases/lucid-announces-updated-lucidspark-integration-with-microsoft-teams-301421337.html — 2026-09-16].
- Klaxoon: sesión lanzada desde la videollamada, según una reseña de terceros de 2023 [verificado: https://www.uctoday.com/reviews/klaxoon-for-microsoft-teams-review-kill-meeting-fatigue-with-unique-and-effective-gamification/ — 2026-09-16]. Si usa el stage: desconocido.
- Parabol y TeamRetro solo ofrecen notificaciones o resúmenes en canales, no una app dentro de la reunión. EasyRetro funciona como pestaña [verificado: parabol.co/integrations/microsoft-teams, teamretro.com/integrations/microsoft-teams, easyretro.io/integrations/microsoft-teams — 2026-09-16].

| Herramienta | App en reunión | Co-edición en stage | Invitados/externos | Móvil | Licencia por editor | Aprobación admin |
|---|---|---|---|---|---|---|
| Miro | Sí (panel + stage) | Sí, con perfil Miro | Contradictorio (Miro: no; Microsoft: sí) | Solo ver | Desconocido | Sí, doble |
| Mural | Sí (2021) | Sí, según marketing | Desconocido | Desconocido | Desconocido | Desconocido |
| FigJam | Sí (escritorio) | Sí en FigJam | Sí, vía open sessions | Desconocido | Asiento Collab (ver §3) | Desconocido |
| Lucidspark | Sí (2021) | Sí, según comunicado | Desconocido | Desconocido | Desconocido | Desconocido |
| Klaxoon | Sí, según reseña | Desconocido | Participantes gratis (ver §3) | Desconocido | Por anfitrión | Desconocido |
| Parabol / TeamRetro | No | No | — | — | — | — |

**Qué prueba y qué no.** Que cuatro proveedores grandes hayan invertido en stage desde 2021 prueba que la demanda existe y que "sin salir de Teams" es un mensaje que vende. No prueba que el stage se use. No se encontraron datos de adopción. Tampoco prueba que resuelva el caso de externos y móvil, ni que los Team Leads sepan que existe.

## 2. Alternativas y no-consumo

**Nativo Microsoft**
- **Whiteboard en reuniones.**
  - *Funciones:* plantillas, reacciones, cursores, encuestas de Forms como componente Loop y colaboración con externos si el administrador la configura [verificado: https://support.microsoft.com/en-us/whiteboard/what-s-new-in-microsoft-whiteboard — 2026-09-16, página 2025-02; https://support.microsoft.com/en-us/whiteboard/use-whiteboard-in-a-teams-meeting — 2026-09-16].
  - *Votación, evidencia contradictoria:* un recopilador de avisos la reporta como "limited to Android" desde 2023 [verificado: https://m365admin.handsontek.net/whiteboard-voting/ — 2026-09-16]. Un moderador de Microsoft Q&A escribió en 2023: "there's no out of box way to achieve this", y sugirió usar reacciones [verificado: https://learn.microsoft.com/en-us/answers/questions/5269738/ — 2026-09-16].
  - *Temporizador dentro de la pizarra:* no se encontró.
- **Retiro de apps independientes de Whiteboard.**
  - Se mantienen Whiteboard dentro de Teams y en la web. Las pizarras antiguas que no estén en OneDrive se borran.
  - *Fechas inconsistentes:* 16-oct-2026 según soporte [verificado: https://support.microsoft.com/en-us/whiteboard/retirement-standalone-microsoft-whiteboard-apps — 2026-09-16, actualizada 2026-08-24]; 30-nov-2026 según el aviso MC1441775 [verificado: https://mc.merill.net/message/MC1441775 — 2026-09-16]; septiembre de 2026 según prensa [verificado: https://www.ghacks.net/2026/08/03/microsoft-whiteboard-retires-legacy-whiteboards-and-standalone-app-by-september-2026/ — 2026-09-16].
- **Temporizador de la reunión (sin Copilot):** cuenta regresiva de hasta 100 minutos, solo en reuniones programadas, en roadmap 494842 para sep–oct 2025. No se confirmó que haya llegado a todos los tenants [verificado: https://learn.microsoft.com/en-us/answers/questions/5544288/ — 2026-09-16].
- **Loop y notas colaborativas:** los componentes Loop en Teams, incluidas las notas de reunión, solo requieren licencia de OneDrive o SharePoint [verificado: https://learn.microsoft.com/en-us/microsoft-365/loop/loop-requirements — 2026-09-16, actualizada 2026-08-18]. Que la app Loop esté incluida en Business Premium: [conocimiento del modelo — verificar].
- **Facilitator (agente Copilot).**
  - *Qué hace:* notas en vivo coeditables en Loop, agenda con temporizador, tareas hacia Planner y un Word por tema.
  - *Licencia y acceso:* "A Microsoft Copilot license is required to add Facilitator". Los internos sin licencia ven las notas y los externos no tienen acceso.
  - *Restricciones:* solo reuniones programadas. En móvil, solo lectura de notas [verificado: https://support.microsoft.com/en-us/teams/copilot/facilitator-in-microsoft-teams-meetings — 2026-09-16, página 2026-08-13].
  - *Sin votación ni pizarra:* no se documentan.
  - *Desactivación:* en julio de 2026, tras las críticas, Microsoft permitió apagar Copilot, Facilitator y el recap en plena reunión [verificado: https://www.windowslatest.com/2026/07/05/microsoft-caves-after-teams-ai-backlash-will-let-you-turn-off-copilot-facilitator-and-recap-mid-meeting/ — 2026-09-16].
- **PowerPoint Live y encuestas de Forms,** incluidas en la licencia base: [conocimiento del modelo — verificar].

**Otras plataformas de reunión**
- **Zoom.**
  - *Whiteboard:* más de 250 plantillas, votación, temporizador, enlaces para visitantes, acceso temporal dentro de la reunión y tablero generado por IA desde la reunión [verificado: https://www.zoom.com/en/products/online-whiteboard/ — 2026-09-16]. Sin iniciar sesión se puede votar durante la reunión [verificado: https://community.zoom.com/t5/Zoom-Whiteboard/Whiteboard-Voting/m-p/210727 — 2026-09-16, post 2024-10].
  - *AI Companion 3.0:* AI Docs, Sheets y Slides a partir de la conversación [verificado: https://news.zoom.com/ec26-zoom-ai/ — 2026-09-16].
- **Google Meet.** Cerró Jamboard (2024) y deriva a FigJam, Lucidspark y Miro, que se abren "directly within a Google Meet call" [verificado: https://workspace.google.com/blog/product-announcements/next-phase-digital-whiteboarding — 2026-09-16]. "Take notes for me" genera un Doc con "decisions, action items" [verificado: https://support.google.com/meet/answer/14754931 — 2026-09-16].
- **Slack huddles.** Genera notas con IA en un canvas con action items, solo en planes pagos, sin pizarra [verificado: https://slack.com/help/articles/31377193680019 — 2026-09-16].

| Plataforma | Pizarra nativa | Plantillas | Votación | Temporizador | Invitados | Móvil | Captura de acuerdos / IA | Licencia |
|---|---|---|---|---|---|---|---|---|
| Teams + Whiteboard | Sí | Básicas | Contradictorio | En la reunión, no en la pizarra | Si el admin lo configura | Desconocido (existe página de soporte) | Notas Loop manuales | Base [modelo — verificar] |
| Teams + Facilitator | No | Desconocido | No | Sí (agenda) | No | Solo lectura | Notas, Planner, Word, recap | Copilot |
| Zoom | Sí | 250+ | Sí | Sí | Sí (visitante) | Apps | AI Companion / AI Docs | Free limitado / pago |
| Google Meet | No (vía socios) | Socios | Socios | Desconocido | Desconocido | Desconocido | Gemini: Doc con decisiones | Edición elegible |
| Slack huddles | No | — | Desconocido | Desconocido | Desconocido | Desconocido | Canvas con tareas | Pago |

**No-consumo y workarounds (señal, no hecho)**
- **G2:** Whiteboard 4,0/5 (52 reseñas) frente a Miro 4,6/5 (13.503). Las quejas contra Whiteboard son "limited features" y "fewer templates" [verificado: https://www.g2.com/compare/microsoft-whiteboard-vs-miro — 2026-09-16].
- **Blogs de competidores (sesgados):**
  - "Timers keep exercises honest, dot voting resolves debates".
  - Las pizarras de Whiteboard son "flat files in OneDrive".
  - Colaborar "outside your tenant" es "awkward" [verificado: https://storyflow.so/blog/microsoft-whiteboard-vs-miro-for-team-whiteboarding — 2026-09-16].
  - Whiteboard "slow to load" [verificado: https://www.jotboard.com/blog/microsoft-whiteboard-2026 — 2026-09-16].
- **Workarounds:**
  - Reacciones en lugar de votar (Q&A citado arriba).
  - Miro como pestaña en reuniones, chats y calendario, "all Microsoft 365 plans" [verificado: https://help.miro.com/hc/en-us/articles/4406387211538 — 2026-09-16].
  - Compartir pantalla con el tablero y pasar acuerdos a mano a Jira: [conocimiento del modelo — verificar]. No se encontraron hilos citables.

## 3. Pricing, modelos de negocio y quién compra

Precios vistos el 2026-09-16. Solo Figma muestra fecha de vigencia.

| Herramienta | Plan | USD usuario/mes | Invitados / visitantes | Enterprise | Fuente |
|---|---|---|---|---|---|
| Miro | Free / Starter / Business / Enterprise | 0 / 8 / 20 (anual) | Free: sin invitados. Starter y Business: visitantes editan tableros públicos. Enterprise: invitados ilimitados | A medida, **mín. 30 miembros**. SSO (Entra ID), SCIM, auditoría, residencia UE/EE.UU./AU/JP | [verificado: https://miro.com/pricing/ — 2026-09-16] |
| Mural | Free / Team+ / Business / Enterprise | 0 / 9,99 anual (12 mensual) / 17,99 / a medida | Visitantes gratis. En Team+ editan. Business: invitados ilimitados | SSO desde Business. Residencia de datos y SCIM en Enterprise | [verificado: https://www.mural.co/pricing — 2026-09-16] |
| FigJam | Asiento Collab (Professional / Org / Enterprise) | 3 anual o 5 mensual / 5 / 5 | Ver y comentar gratis. *Open sessions* de 24 h | SSO, SCIM, alojamiento en UE | [verificado: https://www.figma.com/pricing/ — 2026-09-16]. Vigente desde 2025-03-11 [verificado: https://help.figma.com/hc/en-us/articles/27468498501527 — 2026-09-16] |
| Lucidspark | — | Desconocido (Team ~10–12, mín. 3 [conocimiento del modelo — verificar]) | Desconocido | Desconocido | lucid.app/pricing sin contenido utilizable |
| Klaxoon | Free / Starter / Enterprise | 0 / **24,90 por anfitrión** / a medida | Los participantes editan gratis: 5 / 20 / ilimitados (tope 1.000 simultáneos) | Mín. 5 usuarios Pro. SSO, datos en EMEA o EE.UU. | [verificado: https://klaxoon.com/pricing — 2026-09-16] |

**Patrón:** se cobra a quien crea o facilita, y participar es gratis (en tres de cinco, incluso editar).

**Referencias de precio Microsoft (reales)**
- **M365 Business Premium:** USD 22 por usuario al mes con Teams, **tope de 300 usuarios**. No subió en el ajuste del 2026-07-01 [verificado: https://www.microsoft.com/en-us/microsoft-365/business/microsoft-365-business-premium — 2026-09-16; https://samexpert.com/microsoft-365-july-2026-price-increase/ — 2026-09-16, consultora].
- **Teams Premium:** USD 10 por usuario al mes. Incluye Intelligent Recap, traducción en vivo, marca, marcas de agua, E2EE y control de grabación. **No incluye lienzo colaborativo** [verificado: https://www.microsoft.com/en-us/microsoft-teams/premium — 2026-09-16].
- **Microsoft 365 Copilot:** versión Business "originally $21.00, now starting from $18.00" (anual); paquete Business Premium + Copilot a USD 32 [verificado: https://www.microsoft.com/en-us/microsoft-365/copilot/business — 2026-09-16]. Versión Enterprise a USD 30 [verificado: https://www.microsoft.com/en-us/microsoft-365/copilot/enterprise — 2026-09-16].
- **Lectura contra los USD 8 del caso:**
  - Suben un 36% sobre Business Premium.
  - Quedan por debajo de Teams Premium y de Copilot.
  - Igualan a Miro Starter, pero se cobrarían a toda la organización y no solo a quien facilita.
- **Nota de consistencia del caso:** en el mundo real Business Premium tiene tope de 300 usuarios. Una cuenta como la de Camila (~2.400 licencias en Business Premium) no existiría así. Si el caso quiere realismo, el segmento grande correspondería a planes Enterprise (E3/E5).

**Quién compra**
- **Figma** creció por autoservicio: "The power of the URL, combined with a self-serve option… fueled adoption". Su primer vendedor llegó en 2018 [verificado: https://www.mostlymetrics.com/p/figma-ipo-s1-breakdown — 2026-09-16]. El "70% of new Organization and Enterprise customers" ya incluía al menos un usuario Professional [verificado: https://www.saastr.com/top-10-interesting-learnings-from-figmas-s-1-that-you-may-have-missed — 2026-09-16; resumen del S-1, no contrastado contra la SEC].
  - *Resultados Q1 2026:* USD 333 M de ingresos (+46%), NDR 139%, y "New Pro team conversions grew more than 150%" [verificado: https://www.sec.gov/Archives/edgar/data/1579878/000162828026035087/q126pressrelease.htm — 2026-09-16].
- **Miro:** freemium que parte del usuario final y agrega ventas enterprise. ARR estimado de ~USD 665 M en 2024 (estimación de Sacra) [verificado: https://sacra.com/c/miro/ — 2026-09-16]. Split de ingresos entre autoservicio y ventas: **desconocido**.
- **Notion:** "About 90% of Notion's business comes from 'multiplayer usage'" [verificado: https://www.techbuzz.ai/articles/notion-hits-500m-revenue-riding-ai-wave-as-microsoft-rivalry-heats-up — 2026-09-16].
- **Compras fuera de TI.** Zylo y Torii venden gestión de SaaS, así que tienen interés en que el problema se vea grande.
  - *Zylo 2026:* las áreas de negocio controlan el 81% del gasto SaaS y TI el 15%. El 36% de las licencias no se usa. El gasto reembolsado subió 267% [verificado: https://zylo.com/news/2026-saas-management-index — 2026-09-16]. En el top 15 de apps reembolsadas aparecen Canva y Slack, **pero no Miro ni Notion** [verificado: https://zylo.com/blog/top-expensed-saas-applications — 2026-09-16].
  - *Torii 2026:* el 61% de las apps descubiertas está fuera del control de TI [verificado: https://www.globenewswire.com/news-release/2026/02/24/3243646/0/en/torii-2026-benchmark-report-ai-isn-t-consolidating-saas-it-s-expanding-shadow-it.html — 2026-09-16].
- **Cómo decide TI** entre un upgrade de plataforma y el pedido de una jefatura: **desconocido**. No se encontraron estudios.

## 4. Posicionamiento, tendencias y evidencia de uso

**Evidencia de co-edición frente a consulta**
- **No hay datos públicos sobre cuántos editan y cuántos solo miran en una reunión.** Miro solo publica techos de concurrencia: ~200 editores por tablero "almost every week" [verificado: https://help.miro.com/hc/en-us/articles/360013912300 — 2026-09-16].
- **Miro (junio 2020):** "between 64% and 67% of Miro boards have been used by teams to work together at the same time", frente a ~50% antes de la pandemia [verificado: https://miro.com/blog/collaboration-trends/ — 2026-09-16]. Es un dato del proveedor, del pico pandémico, y "a la vez" no equivale a "dos o más editando durante una reunión".
- **Microsoft Research (CHI 2021):** "around 25% [of remote meetings] include file multitasking". El chat paralelo es "integral" [verificado: https://www.microsoft.com/en-us/research/blog/chi-2021-making-remote-and-hybrid-meetings-work-in-the-new-future-of-work/ — 2026-09-16].
- **Retros remotas (estudio académico, 2025):** las describe con "lower engagement and trust". Los juegos y el anonimato "demonstrably increased… active participation" [verificado: https://ideas.repec.org/h/spr/lnichp/978-3-031-87880-0_2.html — 2026-09-16]. La participación activa hay que provocarla.
- **Persistencia del tablero entre sprints:** **desconocido**.

**Posicionamiento**
- **Miro:**
  - Se define como "the AI Innovation Workspace… the collaboration layer where people, context, and agents… converge" [verificado: https://www.businesswire.com/news/home/20260519060858/en/ — 2026-09-16].
  - **Miro Engage** (enero 2026) promete pasar "from one-way presentations into active collaboration", con votaciones, participación "from any device without requiring accounts" y síntesis con IA. No menciona Teams [verificado: https://www.businesswire.com/news/home/20260120449270/en/ — 2026-09-16].
- **Mural:** "AI-powered visual workspace" [verificado: https://www.mural.co/ — 2026-09-16].
- **FigJam:** "Make meetings more visual and collaborative" [verificado: https://www.figma.com/figjam/ — 2026-09-16].
- **Zoom:** "AI-first, open work platform… designed to move conversations to completion" [verificado: https://news.zoom.com/zoom-launches-ai-companion-3-0/ — 2026-09-16].
- **Microsoft Facilitator:** "surfacing agendas, tracking progress, and capturing key highlights in real time" [verificado: https://learn.microsoft.com/en-us/microsoftteams/facilitator-teams — 2026-09-16].

**Espacios saturados:** resumen y acciones después de la reunión (Microsoft, Zoom, Google, Slack y los note-takers). El discurso de "AI workspace". La facilitación dentro del propio tablero de terceros (Miro Engage, Mural).

**Espacios aparentemente vacíos:**
- Conectar lo que pasa en el tablero de terceros con lo que se dice en la reunión de Teams.
- Facilitación inclusiva (votar, anonimato, móvil, externos) *dentro de Teams* y sin licencia Copilot.
- Organizaciones sin Copilot, que quedan fuera de Facilitator.

**Tendencias** (orden de magnitud)
- **Microsoft WTI, "infinite workday" (junio 2025).**
  - El 57% de las reuniones es improvisada.
  - El 30% cruza zonas horarias.
  - Las reuniones de más de 65 personas son las que más crecen [verificado: https://www.microsoft.com/en-us/worklab/work-trend-index/breaking-down-infinite-workday — 2026-09-16].
  - Fuente del proveedor, parte con telemetría.
- **Agentes en M365:** se multiplicaron ×15 en un año (WTI, mayo 2026) [verificado: https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization — 2026-09-16].
- **New Future of Work 2025 (Microsoft Research):** los facilitadores con IA aumentaron un 22% el intercambio de información, sin cambiar las decisiones. "AI currently works better for individuals than it does for teams" [verificado: https://www.microsoft.com/en-us/research/wp-content/uploads/2025/12/New-Future-Of-Work-Report-2025.pdf — 2026-09-16].
- **Reducción de reuniones:** Shopify eliminó unas 322.000 horas de reuniones recurrentes en 2023 [verificado: https://www.opb.org/article/2023/02/15/shopify-deleted-322000-hours-of-meetings-should-the-rest-of-us-be-jealous/ — 2026-09-16].
- **Consolidación:**
  - Microsoft integra Whiteboard en Teams.
  - Google deja de tener pizarra propia y se apoya en socios.
  - Torii reporta que la IA *expande* la cantidad de apps en vez de consolidarla.
- **Tamaño del mercado:** software de pizarra colaborativa de "algunos miles de millones de USD, creciendo rápido". La cifra de Mordor Intelligence (~3,8 mil M, ~20% anual) es de un informe comercial con metodología opaca y no conviene citarla como dato [verificado: https://www.mordorintelligence.com/industry-reports/collaborative-whiteboard-software-market — 2026-09-16].

**¿Es un dolor que se siente?**
- **HBR (2022):** unos 1.200 cambios de app al día y "just under four hours each week" dedicadas a reorientarse. Muestra de 137 personas [verificado: https://hbr.org/2022/08/how-much-time-and-energy-do-we-waste-toggling-between-applications — 2026-09-16].
- **Atlassian State of Teams 2025 (encuesta del proveedor):** el 74% de los ejecutivos dice que la falta de comunicación afecta la velocidad y la calidad [verificado: https://atlassianblog.wpengine.com/wp-content/uploads/2025/03/the-state-of-teams-2025.pdf — 2026-09-16].
- **Klaxoon con Rogelberg (2021, del proveedor):** el 44% dice que las reuniones "stifle" la inclusión [verificado: https://www.businesswire.com/news/home/20211220005087/en/ — 2026-09-16].
- **Qué falta:** si el Team Lead vive la colaboración en la reunión como *su* problema o como "así es el trabajo" es **desconocido**. Las encuestas muestran malestar general, no que el Team Lead se sienta dueño del problema.

## Impacto en creencias

Veredictos sobre el **mercado**. Ninguno confirma ni descarta una creencia sobre nuestros usuarios. Qué pasa con el registro lo decide `/review-evidence`.

| Creencia (de overview.md) | Veredicto | Evidencia |
|---|---|---|
| **#2 [opportunity] [value]** En la mayoría de las reuniones del segmento con link a Miro/Mural/FigJam, dos o más participantes editan el artefacto durante la reunión | **No dice nada** | No hay datos públicos sobre co-edición frente a consulta en reuniones (§4). El único dato cercano (Miro 2020, 64–67% de tableros usados "at the same time") es del proveedor, de la pandemia, y no separa editores de lectores. La literatura sobre retros sugiere que la edición activa hay que provocarla, lo que no alcanza para inclinar la balanza. |
| **#6 [opportunity] [viability]** Los upgrades a Max del segmento los inició o justificó un mando medio, no TI | **Apoya débilmente (por analogía)** | Productos PLG: el 70% de los Enterprise nuevos de Figma ya tenía un usuario Professional (resumen del S-1). Según Zylo, las áreas de negocio controlan el 81% del gasto SaaS (proveedor). Pero son productos que se compran desde abajo, no upgrades de un plan M365 que firma TI. No hay evidencia sobre cómo decide TI (§3). Conviene separar "quién origina" de "quién firma". |
| **#1 [product] [value]** Se pega el link porque Teams no resuelve el trabajo en vivo; si lo resolviera, dejarían de salirse | **Contradice parcialmente** | Miro, Mural, FigJam y Lucidspark permiten co-editar dentro del stage de Teams desde 2021 (§1), y aun así se pega el link. "Teams no permite" no alcanza como explicación; las candidatas son la fricción de acceso (admin doble, perfil, app por reunión, móvil solo lectura) o que el artefacto vive afuera por otras razones. **Apoya** la parte nativa: a Whiteboard le falta facilitación (votación, temporizador) que Zoom sí tiene (§2). |
| **#3 [product] [viability]** Quien baja de plan tiene un problema de valor percibido, no de precio | **No dice nada (tangencial)** | Zylo reporta que el 36% de las licencias SaaS no se usa (proveedor), así que pagar por lo que no se usa es común. Eso no distingue entre valor y precio en estas cuentas. |
| **#4 [product] [value]** El Team Lead vive la colaboración en la reunión como un problema propio; el bajo uso refleja que las funciones no sirven | **No dice nada / apoya parcialmente la 2ª mitad** | Si el Team Lead se siente dueño del problema: desconocido (§4). Que las funciones nativas no sirven tiene apoyo como señal: G2 4,0 frente a 4,6, quejas de "limited features", sin votación ni temporizador en la pizarra, y retiro de las apps independientes (§2). |
| **#5 [product] [viability]** Hay disposición a pagar USD 8/usuario/mes por colaboración en vivo, y el Team Lead puede empujarlo ante TI | **Contradice parcialmente (precio) / apoya parcialmente (origen)** | El mercado cobra USD 3–25 solo a quien facilita, y participar es gratis (§3). USD 8 a toda la organización son +36% sobre Business Premium. Teams Premium (USD 10) no vende lienzo, y Microsoft cobra la facilitación con IA vía Copilot (USD 18–30). Sobre el origen: la compra que nace abajo es la norma en PLG, pero la firma es de TI. |
| **#7 [product] [value]** "No encuentro el archivo" es un problema de búsqueda en SharePoint, no de archivos que viven fuera | **No dice nada (tangencial)** | Torii ubica el 61% de las apps fuera de TI y Miro se declara con más de 100 M de usuarios (proveedores): el contenido fuera del tenant es común. No dice nada sobre los tickets de este caso. |

## Qué sigue necesitando research primario

**Datos propios (antes de salir a campo; ya en la agenda del brief, con dos agregados):**
- Cruce entre link externo y edición del artefacto durante la reunión (creencia #2).
- **Nuevo:** penetración de las apps Miro/Mural/FigJam instaladas en tenants del segmento y uso de *Share to Stage* frente a pegar link. Si el stage está disponible y no se usa, el problema es de acceso o descubrimiento, no de capacidad.
- **Nuevo:** penetración de Copilot/Facilitator en el segmento. Define si "capturar acuerdos" ya está resuelto para una parte de las cuentas.

**Encuesta (`/design-survey`: cuántos, cada cuánto, cuánto):**
- Cuántos participantes editan en la última reunión con tablero, y si eso cambia por tipo de reunión (retro o planning frente al resto).
- Minutos perdidos en acceso y cambio de ventana.
- Si conocen o probaron *Share to Stage*.
- Quién paga la herramienta externa (área, tarjeta o TI) y cuántos facilitadores por equipo, para dimensionar el precio por facilitador frente al precio por usuario.
- Frecuencia de participantes externos y en móvil.

**Entrevistas (`/design-interview`: por qué y qué hacen hoy):**
- Por qué pegan el link en vez de usar stage o Whiteboard: desconocimiento, permisos, o el tablero vive allí por la memoria del equipo.
- Qué pasa con el tablero después de la reunión.
- Si viven el problema como propio.
- En las cuentas que subieron a Max: quién originó el pedido, quién firmó y con qué argumento (creencia #6).
- Con TI (tipo Nadia): cómo evalúa un upgrade frente a consolidar herramientas externas.
