# T2 · decisiones-extraidas-ia — material de la prueba técnica

Prueba: `product/tests/2026-10-06-2100-decisiones-que-no-sobreviven-la-reunion.md`, T2 (`technical-test`, creencia 12, parte de **precisión**).
Responsable de correrla: **tecnología**.

## Qué hay en esta carpeta

| Archivo | Para qué |
|---|---|
| `solicitud-transcripciones.md` | Mensaje a los líderes para pedir las transcripciones y texto de consentimiento del grupo |
| `set-de-entrada.md` + `registro-transcripciones.csv` | Cómo juntar, anonimizar y separar las 12 transcripciones (4 de ajuste y 8 reservadas) |
| `clave-respuesta.md` + `clave-respuesta.csv` | Cómo arman la clave el líder y la persona observadora, una fila por ítem |
| `prompt-extraccion.md` | El prompt de extracción y su formato de salida |
| `planilla-puntaje.csv` + `puntaje-como-leer.md` | Puntaje por ítem, cómo se emparejan los ítems y cómo se lee el umbral |
| `calcular-puntaje.py` | Calcula las cuatro métricas y el resultado contra el umbral a partir de las dos planillas |

## Orden de la corrida (no se altera)

1. **Juntar** las 12 transcripciones con consentimiento (`solicitud-transcripciones.md`) y **anonimizarlas** dentro del tenant (`set-de-entrada.md`).
2. **Separar** 4 de ajuste y 8 reservadas con la regla de `set-de-entrada.md`, **antes** de que nadie lea las transcripciones con el prompt en mente.
3. **Armar la clave de las 12** (`clave-respuesta.md`). La clave se cierra antes de correr el prompt y nadie que la arme ve la salida de la IA.
4. **Ajustar el prompt** solo con las 4 de ajuste, con su clave. Se puede iterar todo lo necesario.
5. **Congelar el prompt:** se anota en `registro-transcripciones.csv` la versión (copia literal o hash), el modelo y la configuración. Desde ahí no se toca.
6. **Correr a ciegas** el prompt congelado sobre las 8 reservadas, **una corrida por transcripción**. No se repite para quedarse con la mejor. Si la cuenta tiene Copilot, se exporta el recap o Facilitator de esas mismas 8 reuniones.
7. **Puntuar** con `planilla-puntaje.csv` y `puntaje-como-leer.md`, y **calcular** con `calcular-puntaje.py`.

Si una de las 8 reservadas se mira mientras se ajusta el prompt, deja de servir como reservada: se reemplaza por una transcripción nueva y se anota en `notas`.

**Fuera a propósito** (lo fija el diseño): interfaz, integración con Teams, publicación, lectura del artefacto (votos, tickets) y flujo de confirmación.
