# Set de entrada — 12 transcripciones (4 de ajuste y 8 reservadas)

## De dónde salen

1. **Primero:** reuniones de T1 (base y con cierre) de las 5 series. Son las que tienen persona observadora y, en las reuniones con cierre, lista confirmada, que sirven para armar la clave.
2. **Si faltan:** 2 o 3 líderes más del pool de la encuesta (grupo 2 del insight 2026-09-29-2040), con la misma solicitud. Estas no tienen persona observadora: la reemplaza alguien del equipo que lea la transcripción completa **antes** de armar la clave con el líder (ver `clave-respuesta.md`). Se marca `con_observadora = no`.

Requisitos por transcripción: reunión real de más de 5 participantes, líder Team Lead del segmento, exportación de la transcripción de Teams (.vtt o .docx) con hablante y marca de tiempo, y consentimiento del grupo.

Si se puede, que haya reuniones de los dos tipos: pizarra y sistema de registro, igual que en T1.

## Anonimización (dentro del tenant, antes de que la transcripción salga)

- **Personas:** se reemplazan por un código estable **por serie**: `S1-P01`, `S1-P02`… El mismo nombre siempre recibe el mismo código, también cuando se menciona en el habla («que lo vea **Martín**» → «que lo vea **S1-P03**»), y lo mismo con apodos y nombres de pila. La tabla de equivalencias queda en el tenant del líder y nunca sale.
- **Clientes, proyectos, productos internos:** `CLIENTE-A`, `PROYECTO-B`, etc.
- **Correos, teléfonos, montos y números de ticket:** se reemplazan por `[CORREO]`, `[TEL]`, `[MONTO]` y `[TICKET-1]`.
- **Las fechas y los días se mantienen** («el jueves», «para el 15»): sin ellos no se puede evaluar la fecha.
- La clave se arma **con los mismos códigos**, para que el responsable se pueda comparar directo.

Revisión: una segunda persona busca nombres que quedaron sin reemplazar antes de la exportación. Se anota `anonimizada_revisada = si`.

## Separación en ajuste y reservadas

Se hace **antes** de cualquier lectura de las transcripciones con el prompt en mente:

1. Se ordenan las 12 por `id_transcripcion`.
2. Se sortean (por ejemplo, con `random.sample` y una semilla anotada en `registro-transcripciones.csv`) **4 de ajuste**, con una condición: que no queden 2 de ajuste de la misma serie si se puede evitar.
3. Las otras 8 quedan `reservada`. Esas 8 se guardan en una carpeta aparte, y quien ajusta el prompt no las abre.

## Registro

`registro-transcripciones.csv`: una fila por transcripción. La primera fila es un ejemplo de valores válidos: bórrala al empezar. Al final del archivo van dos filas `#PROMPT` y `#SORTEO`, que registran la versión congelada del prompt y la semilla.
