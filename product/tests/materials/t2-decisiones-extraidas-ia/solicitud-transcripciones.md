# Solicitud de transcripciones y consentimiento

## 1. Mensaje al líder (Team Leads de T1 y, si faltan, 2 o 3 del pool de la encuesta)

> **Asunto:** ¿Nos prestas 2 o 3 transcripciones de tu reunión semanal?
>
> Hola [nombre]:
>
> Seguimos con la investigación sobre las decisiones que se pierden después de las reuniones. Ahora queremos ver si una IA puede distinguir en una transcripción qué fue una **decisión**, qué fue una **idea** y qué fue una **tarea**, y quién quedó a cargo de cada cosa. Para medirlo necesitamos reuniones reales y a alguien que sepa qué se decidió de verdad: tú.
>
> **Qué te pedimos:**
> - La transcripción de Teams de **2 o 3 reuniones** de tu serie [nombre de la serie], de más de 5 participantes. Si ya participas en la prueba de cierre, idealmente las mismas reuniones que observamos.
> - **Unos 20 minutos por reunión**, junto a [nombre de la persona observadora], para marcar en una lista qué fue decisión, idea o tarea, con responsable y fecha. No te mostramos lo que sacó la IA, y tampoco necesitas verlo.
>
> **Qué hacemos con la transcripción:**
> - Antes de que salga de tu organización, reemplazamos los nombres de personas, clientes y proyectos por códigos. La versión con nombres no sale del tenant.
> - La usamos solo para esta prueba. No se comparte con tu empresa ni sirve para evaluar a nadie.
> - Si alguna reunión trata temas que no pueden salir del tenant, ni siquiera anonimizados, la saltamos.
>
> Antes de enviarla, el grupo tiene que estar de acuerdo (abajo va un texto corto para leerles).
>
> ¿Te sumas? Responde **"Sí, acepto"** y te explicamos cómo exportarla.

## 2. Texto para el grupo (lo lee el líder al inicio de la reunión, o lo manda por el chat)

> "Esta reunión se transcribe como siempre. Con su acuerdo, voy a compartir la transcripción **con los nombres reemplazados por códigos** para un estudio sobre cómo una IA identifica las decisiones de una reunión. No se usa para nada más. Si alguien prefiere que esta reunión no se comparta, me lo dice por privado y no la mandamos."

**Si alguien se opone, no se comparte la transcripción de esa reunión.** Registrar en `registro-transcripciones.csv` → `consentimiento_grupo = no` y no usarla.

## 3. Exclusiones (fijadas en el diseño)

- Cuentas cuyo compliance no permite sacar transcripciones del tenant, ni anonimizadas (Lucía).
- Reuniones de 5 participantes o menos.
