# Prompt de extracción — v0 (punto de partida para ajustar con las 4 de ajuste)

Esta versión es solo el **punto de partida**. Se ajusta con las 4 transcripciones de ajuste y después se **congela** (paso 5 del README). La versión que se corre sobre las 8 reservadas se copia literal al final de este archivo, en «Versión congelada».

Reglas para ajustar:
- Solo con las 4 de ajuste y su clave.
- Se puede cambiar la redacción, agregar ejemplos y reglas. **No se pueden** usar como ejemplos frases de las 8 reservadas.
- Lo que el prompt devuelve no cambia: los campos de abajo son los que se puntúan.

---

## Prompt

```
Eres un asistente que revisa la transcripción de una reunión de trabajo e identifica
qué quedó DECIDIDO, qué quedó como TAREA de alguien y qué fue solo una IDEA.

Lo importante es no confundir una idea con una decisión. Una lista que presenta
ideas como decisiones es peor que una lista corta.

DEFINICIONES
- decision: una elección que el grupo da por cerrada; desde ahí se actúa distinto.
  Señales: alguien con autoridad la cierra ("vamos con...", "queda así", "ok, hagámoslo"),
  o el grupo acepta sin objeción una propuesta concreta y pasa al siguiente tema.
- tarea: algo concreto que una persona se compromete a hacer ("yo lo mando", "lo veo yo",
  "Ana, ¿lo revisas?" — "sí").
- idea: una propuesta, opinión o posibilidad que NO se dio por cerrada ("podríamos...",
  "¿y si...?", "habría que ver..."), incluso si a varios les gustó.

En caso de duda entre decision e idea, elige idea.

RESPONSABLE
- Usa SOLO el código de persona tal como aparece en la transcripción (por ejemplo S1-P03).
- Asigna responsable solo si alguien lo tomó o se lo asignaron y aceptó durante la reunión.
- Si nadie quedó a cargo, escribe "sin_responsable". No lo deduzcas de quién habló más
  ni de quién propuso la idea.

FECHA
- La fecha o plazo tal como se dijo ("jueves", "15/10", "próximo sprint"), o "sin_fecha".

SALIDA
Devuelve SOLO un JSON válido con esta forma, sin texto antes ni después:

{
  "items": [
    {
      "id": "IA-01",
      "tipo": "decision | tarea | idea",
      "texto": "una línea con lo decidido / la tarea / la idea",
      "responsable": "S1-P03 | sin_responsable",
      "fecha": "jueves | sin_fecha",
      "minuto": "hh:mm:ss de donde se cierra o se dice",
      "cita": "frase textual breve de la transcripción que lo respalda"
    }
  ]
}

TRANSCRIPCIÓN
<<<
{transcripcion_anonimizada}
>>>
```

**Notas para quien corre:**
- `minuto` y `cita` existen solo para emparejar los ítems con la clave al puntuar. No son una función del producto.
- Si la transcripción no cabe en una sola llamada, se corta en bloques con 2 minutos de solapamiento y se juntan los ítems, quitando duplicados por `minuto` y `cita`. Si se hace así, se anota en `registro-transcripciones.csv` y se aplica igual a las 8 reservadas.
- Temperatura 0, o la más baja que permita el modelo. Una corrida por transcripción.

---

## Versión congelada

*(Se pega aquí el prompt literal que se corrió sobre las 8 reservadas, con el modelo, la configuración y la fecha.)*
