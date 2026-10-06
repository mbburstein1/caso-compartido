---
date: 2026-09-29
source: real
opportunity: colaboracion-en-vivo-fuera-de-teams
guide: product/interview-guides/2026-09-23-2030-colaboracion-en-vivo-fuera-de-teams.md
n: 10 entrevistas de exploración (25 y 28 de septiembre de 2026)
sources:
  - product/interviews/2026-09-25-1000-tomas-aguirre.md (source: real)
  - product/interviews/2026-09-25-1100-andres-quintero.md (source: real)
  - product/interviews/2026-09-25-1600-lucia-fernandez.md (source: real)
  - product/interviews/2026-09-28-0900-javier-molina.md (source: real)
  - product/interviews/2026-09-28-0930-martina-rojas.md (source: real)
  - product/interviews/2026-09-28-1000-diego-paredes.md (source: real)
  - product/interviews/2026-09-28-1200-sofia-martinez.md (source: real)
  - product/interviews/2026-09-28-1400-paula-benitez.md (source: real)
  - product/interviews/2026-09-28-1500-valeria-castro.md (source: real)
  - product/interviews/2026-09-28-1700-ricardo-salinas.md (source: real)
related: product/insights/2026-09-29-2040-colaboracion-en-vivo-fuera-de-teams.md (encuesta, n=210)
---

# Insights de entrevistas: cómo trabajan y deciden los líderes en reuniones de más de 5

## Corpus

| Entrevistado | Rol · país | Encuesta | Reunión analizada | Mundo |
|---|---|---|---|---|
| Tomás Aguirre | Eng. Manager · AR | R-113 · panel | Retro en Miro (+ refinamiento en Jira) | Pizarra |
| Andrés Quintero | Head Support Ops · CO | R-170 · panel | Escalamientos sobre Excel en SharePoint, pantalla compartida | Sistema de registro |
| Lucía Fernández | Eng. Manager · ES | R-143 · email | Priorización de incidencias en la pizarra de Teams (compliance) | Pizarra nativa |
| Javier Molina | Eng. Manager · ES | R-097 · panel | PI planning en Miro + Slido | Pizarra |
| Martina Rojas | Eng. Manager · CL | R-224 · panel | Planning en Jira + Grafana (+ retro en Miro) | Sistema de registro |
| Diego Paredes | Data Team Lead · PE | R-036 · email | Revisión de métricas en Power BI | Sistema de registro |
| Sofía Martínez | PM Lead · MX | R-151 · panel | Revisión de PRD en Confluence (+ kickoff en Google Doc) | Sistema de registro |
| Paula Benítez | Product Lead · AR | R-153 · email | Review mensual con notas de reunión de Teams | Informativa, no se decide |
| Valeria Castro | Design Lead · CO | R-024 · email | Planning trimestral en FigJam (+ critique en Figma) | Pizarra |
| Ricardo Salinas | Dir. Ing. Plataforma · MX | R-196 · panel | Sync semanal, todo hablado | Sin artefacto |

**Límites.** Diez entrevistas reclutadas del pool de la encuesta, a propósito cargadas hacia quienes contradecían las creencias (4 del grupo "no salen", 3 de "artefacto preexistente + acceso rápido", 3 confirmadores). Las cifras "x/10" son **recurrencia**, no prevalencia. Tomás reconoció haber exagerado en la encuesta ("puse que salgo de Teams en todas las reuniones. No es así"): Q1 puede sobrestimar la frecuencia de salida.

## Recurrencia por entrevistado

| Insight | Tomás | Andrés | Lucía | Javier | Martina | Diego | Sofía | Paula | Valeria | Ricardo | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1. Lo decidido se pierde después | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | **10** |
| 2. El recap de IA no sirve como registro | | | ● | ● | ● | ● | | ● | ● | | **6** |
| 3. Lo nativo rompe la continuidad | ● | | ● | ● | | | ● | ● | | ● | **6** |
| 4. Quien no toca, dicta o calla | ● | ● | ● | ● | ● | ● | ● | | ● | | **8** |
| 5. Converger es informal y opaco | ● | ● | ● | ● | ● | | ● | | ● | ● | **8** |

---

## 1. Lo decidido se pierde entre la reunión y la ejecución, y solo lo sostiene el trabajo manual del líder

Los diez contaron un caso reciente y concreto de una decisión que se ejecutó distinto o no se ejecutó, casi siempre con costo medible (tabla abajo). El mecanismo no es la falta de un lugar donde registrar (todos tienen Jira, correo, Confluence o Slack), sino la **falta de un cierre**: nadie confirma antes de colgar qué se decidió, quién lo hace y para cuándo, y el registro depende de que el líder lo reescriba después, entre 10 y 60 minutos por reunión ("nadie más lo hace": Tomás, Javier, Valeria). El campo que más falla es el responsable: en tres casos cada uno creyó que lo hacía el otro (Andrés, Lucía, Ricardo). Implicación: la oportunidad con más evidencia no es colaborar en vivo sino **cerrar la reunión**: una lista de decisiones con responsable y fecha, confirmada por el grupo antes de colgar y enviada a donde vive el trabajo (el ticket, el PRD, el canal).

| Entrevistado | Qué pasó | Costo |
|---|---|---|
| Tomás | El acuerdo sobre tests de integración nunca pasó a Jira porque la pizarra se perdió | Un mes después nadie recordaba; se rediscutió en otra retro |
| Andrés | Escalamiento de Guayaquil: el líder y él creyeron que lo pasaba el otro | Cliente 4 días sin atención; escaló al gerente comercial |
| Lucía | Incidencia reconstruida de memoria; dos personas creyeron que la llevaba la otra | Una semana sin tocar; el cliente lo notó |
| Javier | La dependencia de la API de geocercas quedó en el recap como "se habló de" | Entrega 2 semanas tarde; se movió una release entera |
| Martina | El porqué de postergar una historia de seguridad quedó en un hilo de Slack | 20 min de rediscusión; la historia pudo entrar dos semanas antes |
| Diego | El correo de acuerdos salió dos días tarde; marketing Chile lo esperaba para pausar | La campaña siguió 3 días; presupuesto gastado de más |
| Sofía | "SPEI queda fuera" se decidió en un comentario que ella marcó resuelto (y se ocultó) | 2 semanas de trabajo rehecho |
| Paula | El recap de IA registró una idea como decisión | ~1 semana de dos desarrolladores |
| Valeria | Captura confusa: una iniciativa descartada quedó cargada en Jira | 1 semana de un diseñador |
| Ricardo | El orden de la migración de Postgres "se habló"; nadie lo escribió | 2 días de arreglo + fin de semana de guardia |

> Evidencia: "Se habló en la sync, cada uno se fue con su versión y nadie lo escribió. Yo pensé que el arquitecto iba a hacer el ADR y él pensó que yo lo iba a mandar por correo" — Ricardo · "Pues ahí uno se da cuenta de que el correo no sirve tanto como uno cree" — Andrés · "Lo que nos falla es cómo se cierra la reunión: que quede claro qué se decidió, que lo sepan todos, incluso los que no hablaron. Eso lo hago medio a mano y a veces se me va" — Sofía

## 2. El recap de IA se usa pero no sirve como registro: no separa decisión de idea, no asigna responsable y no ve el artefacto

Seis de los diez usaron el resumen de Copilot/Teams y los seis tienen una queja concreta; dos armaron una rutina manual para corregirlo (Paula revisa 10 min por reunión, Javier lo reescribe en 30 min) y Martina lo abandonó. Las fallas son de dos tipos: **estructura** (pone todo al mismo nivel: Javier, Martina; no dice quién se comprometió: Lucía; convierte ideas en decisiones: Paula) y **ceguera al artefacto** (no ve los votos del FigJam: Valeria; no sabe qué filtro o gráfico se miraba: Diego; no ve lo decidido en Slack: Martina). Además, el recap se lee como fuente de verdad aunque esté mal: el equipo de México leyó el recap en vez del hilo (Javier) y Paula lo reenvió sin leerlo. Implicación para la IA: el valor no es resumir, que ya existe, sino **extraer decisiones tipificadas (decisión / idea / tarea) con responsable y fecha, apoyadas en el estado del artefacto (votos, filtros, tickets), con confirmación humana antes de publicarse** y escritas de vuelta en el ticket.

> Evidencia: "Marca como decisión cosas que eran solo ideas. Alguien dice 'podríamos pasar el release al 20' y en el resumen aparece 'se decidió pasar el release al 20'" — Paula · "No ve lo que pasó en el FigJam, solo lo que se habló. [...] El resumen decía algo como 'se discutieron prioridades'" — Valeria · "Me resumió la conversación, no las decisiones" — Martina · "Lo que sí me serviría es algo que cierre la reunión con lo decidido y el por qué, y que eso quede en el ticket" — Martina

## 3. La continuidad entre sesiones es lo que retiene a Miro; lo nativo la rompe porque queda atado a una instancia de la reunión

Tomás y Javier usan un único tablero de Miro con un frame por sesión, y lo justifican por la continuidad: revisar los acuerdos anteriores y ver qué se arrastra. En el otro sentido, cinco perdieron un artefacto nativo porque quedó colgado del chat o de la invitación de una reunión puntual: la pizarra desapareció al recrearse la serie (Tomás, 15 min buscando, acuerdos perdidos), al hacer una convocatoria nueva (Lucía, que ahora pega capturas en Confluence), o simplemente "no supe dónde había quedado" (Sofía, Ricardo); a Paula le pasó con las notas de reunión al reprogramar. De los seis que probaron la pizarra de Teams, cinco la abandonaron, y además de la persistencia citan falta de votación (Tomás, Javier, Lucía), falta de plantillas (Tomás, Javier), lentitud con 9 a 14 personas (Tomás, Javier, Sofía, Ricardo) y agrupar a mano (Lucía, Ricardo). La sexta, Lucía, sigue solo porque compliance le prohíbe salir. Implicación: antes de sumar funciones de dibujo, anclar la pizarra y las notas a la **serie, el equipo o el canal**, que sobrevivan a una reprogramación, con un link fijo y acceso a la sesión anterior. Paula muestra que el anclaje a la reunión se valora; el problema es el objeto al que se ancla.

> Evidencia: "Esa continuidad es la razón por la que estamos en Miro. Si tuviera que empezar de cero cada vez, perdería el hilo" — Tomás · "Queda atada al chat de esa reunión, y como la segunda sesión fue una convocatoria nueva, pues ahí no aparecía [...] Desde entonces hago captura de pantalla al terminar y la pego en Confluence" — Lucía · "Lo que me gusta es que quedan pegadas a la reunión [...] Lo único que me molesta es cuando reprogramamos" — Paula

## 4. Quien no puede tocar el artefacto dicta o se queda callado, y su objeción aparece después de la reunión

Ocho de diez describen participantes que no pueden actuar sobre el artefacto, por dos vías. **No logran entrar**: invitados sin licencia (Tomás, 3 de 11 solo miran), otra instancia de Miro en la filial de Francia (Javier, 2 o 3 sin editar en toda la primera hora), cuenta personal de Google (Valeria: Gloria nunca entró), sin permiso en Confluence (Sofía: Karla), pantalla de 13 pulgadas (Lucía). **Pantalla compartida**: solo el que comparte actúa y los demás no pueden señalar (Andrés, Diego, Valeria en el critique, Tomás en Jira, Martina). El resultado es que el líder transcribe al dictado (Tomás, Lucía, Javier, Martina, Andrés) y los errores son del líder: Andrés cerró el ticket de la fila equivocada y al cliente le llegó la notificación de cierre. Los minutos de acceso solo pesan con licencias de pizarra (5 a 10 min en Tomás, Javier y Valeria); con SSO es un minuto (Martina, Diego, Sofía). Implicación, en línea con la encuesta: medir **participantes que pueden actuar** (señalar, marcar, votar), no minutos. En el mundo sistema de registro, un puntero compartido o la posibilidad de marcar una fila o un punto del gráfico desde la reunión resuelve buena parte sin salir de la herramienta.

> Evidencia: "La gente que no entra al tablero no es poca. En casi todas hay alguien mirando desde afuera, y esa gente no opina. Eso me preocupa más que los minutos" — Valeria · "Hace como un mes y medio cerré un ticket que no era [...] Al cliente le llegó la notificación de cierre y el caso seguía abierto" — Andrés · "El de operaciones decía 'el pico de marzo', yo pongo el mouse en marzo, 'no, el otro'" — Diego

## 5. Converger es informal y opaco: se vota contando manos, el líder desempata solo y el desacuerdo de los callados no queda registrado

Tres cuentan manos o reacciones a ojo (Andrés: "a veces se me pasa uno"; Lucía: "no te fías del todo del número"; Ricardo: "nueve contra siete, algo así"). En FigJam, dos votaron dos veces y se perdieron 10 minutos discutiendo si valía (Valeria). Martina no tiene cómo marcar prioridades sin que se vuelva una discusión de 20 minutos. En seis casos el líder terminó decidiendo solo, por tiempo o por empate (Tomás, Andrés, Lucía, Javier, Martina, Sofía), y en tres el desacuerdo apareció después, por privado o en un café (Martina, Sofía, Valeria). Hay un contrapunto: para Paula y Ricardo las reuniones grandes no son para decidir ("con dieciséis personas no se puede decidir nada") y para Javier "la votación no decide". Implicación: la necesidad no es "votar para decidir" sino **capturar posiciones, incluidas las de los que no hablan, como insumo de la decisión del líder**. Eso pide una votación nativa liviana que limite votos, muestre quién votó y deje el resultado pegado a la decisión (se conecta con el insight 1).

> Evidencia: "No hay forma de que cada uno marque su prioridad sin que se transforme en conversación. Hablamos veinte minutos. Al final decidí yo. Y dos devs se quedaron con cara de no" — Martina · "Me la encuentro en un café de la oficina y me dice que no estaba de acuerdo con sacar la reprogramación de citas por WhatsApp [...] Una objeción importante, y yo ni me enteré en la reunión" — Valeria · "Sé que hay gente que arma tableros con votaciones y todo eso con veinte personas. A mí no me parece que eso sea decidir. Es dar la sensación de que todos participaron" — Paula

---

## Señales en contra y matices

- **La herramienta de la reunión no es "su" problema para la mitad.** Diego ("A mí no me falta nada en Teams"; lo ve como disciplina), Ricardo (su problema es la cantidad: 27 h semanales de reuniones), Paula ("no lo necesito"), Martina ("no veo para qué querría otra herramienta") y Sofía ("la herramienta no es el problema"). Pero los cinco sí reconocen el dolor del insight 1.
- **Salir de Teams por colaborar en vivo** describe solo al mundo pizarra (Tomás, Javier, Valeria, la retro de Martina). En el mundo sistema de registro (Andrés, Martina, Diego, Sofía) el artefacto vive ahí y nadie lo movería: "Si hacemos el planning en otro lado después hay que pasarlo a Jira igual. Doble trabajo" (Martina).
- **Compliance** (Lucía): aprobar una herramienta externa lleva meses (seguridad, legal, DPO). Para ese perfil, lo nativo es la única opción: "Necesito que funcione mejor, no que me digan que hay otra cosa fuera".
- **Lo nativo tampoco se conoce**: apps dentro de la reunión (Ricardo: "¿Se puede?"), notas de Loop (Andrés las vio una vez y le gustaron; Diego nunca las usó), la pizarra (Valeria no sabía que existía).
- **Sofía usa un Google Doc** para kickoffs porque comercial no tiene acceso a Confluence: a veces se sale de un sistema por permisos, no por colaboración.

## Contraste con la encuesta (2026-09-29-2040)

Las entrevistas confirman con casos los cuatro primeros insights de la encuesta: la decisión que no sobrevive, los dos mundos, "alguien queda afuera" y la pizarra abandonada por falta de persistencia. Agregan tres cosas que la encuesta no mostraba: el recap falla también por **ceguera al artefacto**; lo que se pierde no es solo el qué sino el **porqué** (Martina); y el **desacuerdo silencioso** aparece después de la reunión.

## Para la próxima ronda

1. ¿Aceptaría el grupo un cierre de 2 minutos para confirmar decisiones? ¿Quién lo conduce si el líder está moderando (Lucía: "escribir y moderar a la vez me cuesta")?
2. ¿Qué haría que una lista de decisiones se lea? El recap que Martina pegó en el ticket nadie lo leyó porque era largo.
3. Referidos que conducen de forma distinta, útiles como contraste: Carla (retros solo habladas, Nubila), Natalia (usa notas de reunión, Tándem), Fernanda (planning sin nada externo, Trazo), Mariana (reuniones sin documento, Ámbar), Gonzalo Ferreyra (vive en Miro, Siembra), Andrés (todo en Teams, Kora), Daniela (tableros, Lumen) y un manager de Veta Colombia que trabaja por Slack.
