# Puntaje — cómo se llena y cómo se lee el umbral

## Cómo se llena `planilla-puntaje.csv`

Una fila por ítem, por transcripción y por sistema (`ia` o `copilot`). La primera fila es un ejemplo: bórrala al empezar.

1. **Una fila por cada ítem que devolvió el sistema.** Se busca en la clave el ítem que corresponde. Si se encuentra, va su `id_item_clave` y su `tipo_clave`. Si no, ambos quedan vacíos.
2. **Una fila por cada decisión o tarea de la clave que el sistema no tiene** (no se emparejó con ningún ítem): `id_item_sistema` vacío, `tipo_sistema` vacío, y `id_item_clave`, `tipo_clave` y `responsable_clave` llenos. Estas filas son las de «agregar».
3. Los ítems de la clave con `tipo_final = excluido` no cuentan. Si el sistema devolvió un ítem que empareja con uno excluido, se anota `tipo_clave = excluido` y el script lo ignora.

### Regla de emparejamiento

- Un ítem del sistema empareja con un ítem de la clave cuando se refieren **a lo mismo**: la misma elección o el mismo compromiso, aunque esté redactado distinto. Para decidir se usan `minuto` y `cita`.
- **Uno a uno.** Si el sistema parte un ítem de la clave en dos, uno empareja y el otro queda sin emparejar. Si junta dos ítems de la clave en uno, empareja con uno solo y el otro va como fila «agregar».
- **El tipo no se mira para emparejar.** Una decisión de la clave que el sistema puso como idea empareja igual, y queda registrado `tipo_sistema = idea`, `tipo_clave = decision`.
- Quien puntúa **no es quien ajustó el prompt**. Los casos dudosos se resuelven con una segunda persona y se anotan en `notas`.
- Cuando hay comparación con Copilot, se puntúan las dos salidas **sin que se vea cuál es cuál** (se renombran como «salida 1» y «salida 2» antes de puntuar), con la misma regla.

### Cómo se lee la salida de Copilot (regla fijada antes de puntuar)

El recap o Facilitator no clasifica en decisión, idea y tarea. Se toma así:
- `tipo_sistema = decision`: los ítems que aparecen bajo un título de decisiones o acuerdos. Si no hay un título así, los ítems de las notas redactados como algo ya decidido («se decidió», «se acordó», «el equipo va a…»).
- `tipo_sistema = tarea`: las tareas de seguimiento («follow-up tasks» o «acciones»).
- El resto de las notas no se puntúa.
- `responsable_sistema`: la persona que el recap nombra, convertida a su código. Si no nombra a nadie, `sin_responsable`.

### Responsable y fecha

- `responsable_sistema` y `responsable_clave`: códigos o `sin_responsable`. El script los compara.
- `fecha_correcta`: `si` si la fecha del sistema es la de la clave (o ambas son `sin_fecha`), `no` si es otra, `na` si la fecha de la clave quedó `excluida` o si no hay emparejamiento.

## Métricas (las calcula `calcular-puntaje.py`, solo con las filas `reservada`)

| Métrica | Fórmula |
|---|---|
| **Precisión de decisión** | filas con `tipo_sistema = decision` y `tipo_clave = decision` ÷ filas con `tipo_sistema = decision` y `tipo_clave` ≠ `excluido` (incluye las que no emparejaron) |
| **Cobertura de decisión** | decisiones de la clave emparejadas con `tipo_sistema = decision` ÷ todas las decisiones de la clave (emparejadas o «agregar») |
| **Responsable correcto** | entre las decisiones encontradas (numerador de la cobertura), las que tienen `responsable_sistema = responsable_clave` |
| **Correcciones por reunión** | por transcripción, suma de: «agregar» (una decisión o tarea de la clave que falta) + «quitar» (un ítem marcado como decisión o tarea que en la clave es idea o no está) + «retipificar» (marcado como decisión cuando era tarea, o al revés, o una decisión o tarea de la clave marcada como idea) + «corregir» (tipo bien, pero responsable o fecha mal; cuenta 1 por ítem aunque estén mal las dos cosas). Se reporta la **mediana** de las 8. |

Las ideas que el sistema marcó como idea y no están en la clave no suman correcciones: no entran a la lista que se confirma.

## Cómo se lee el umbral (fijado en el diseño, no se cambia acá)

Sobre las 8 reservadas, sistema `ia`:

| Resultado | Condición |
|---|---|
| **Pasa** | precisión ≥ 90% **y** cobertura ≥ 80% **y** responsable correcto ≥ 80% **y** mediana de correcciones ≤ 2 |
| **Falla** | precisión < 75% **o** cobertura < 60% |
| **Falla por comparación** | hay salida de Copilot y la precisión de `ia` **no supera** la de `copilot` (aunque cumpla todo lo demás) |
| **Entre medio** | ni pasa ni falla → `change` según la regla del diseño. Si pasa en todo menos responsable correcto, también es `change` |

Si no se llega a 8 reservadas válidas, no se lee el resultado: se vuelve a `/design-solution-tests`.

Diagnóstico (no cambia el resultado): las mismas métricas sobre las 4 de ajuste. Si en ajuste son mucho mejores que en las reservadas, el prompt quedó sobreajustado.

## Cálculo

```
python3 calcular-puntaje.py planilla-puntaje.csv
```
