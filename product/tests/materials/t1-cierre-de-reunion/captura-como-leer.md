# Planillas de captura — cómo se llenan y cómo se lee el umbral

Dos archivos:

- **`planilla-captura.csv`** — una fila por decisión. La primera fila es un ejemplo de valores válidos: bórrala al empezar.
- **`planilla-reuniones.csv`** — una fila por reunión (3 por serie, 15 en total). La primera fila es un ejemplo: bórrala al empezar.

## Columnas clave

| Columna | Valores | Quién la llena y cuándo |
|---|---|---|
| `tipo_reunion` | `base` (reunión 1) · `cierre` (reuniones 2 y 3) | Al abrir la fila |
| `origen` | `observada` (la anotó la observadora) · `confirmada` (solo apareció en el cierre) · `ambas`. En la base siempre `observada` | Tras la reunión |
| `decision_texto`, `responsable`, `fecha_compromiso` | Lo que escuchó la observadora (vacío si no se dijo). Si la decisión fue confirmada en el cierre, lo confirmado | Tras la reunión |
| `sin_dueno` | `si` si no tiene responsable | Tras la reunión |
| `estado_lider`, `estado_responsable` | `como_se_decidio` · `distinto` · `tarde` · `no_se_hizo` · `no_se` | Seguimiento a 14 días |
| `estado_final` | Regla del guion §3 (si difieren → `distinto`; sin respuesta o "no sé" de ambos → `sin_dato`) | Tras el seguimiento |
| `perdida` | `si` si `estado_final` ∈ {distinto, tarde, no_se_hizo} · `no` si `como_se_decidio` · `sin_dato` | Tras el seguimiento |
| `procedencia` (reuniones) | `real` si el líder es Team Lead del segmento · `stand-in` si no (no debería ocurrir) | Al abrir la serie |
| `cierre_mas_de_2_min` | `si` si `duracion_cierre_seg` > 120 | Tras la reunión con cierre |

## Cómo se lee el umbral (fijado en el diseño — no se cambia acá)

Excluyendo las filas con `perdida = sin_dato`:

1. **Tasa base** = decisiones con `perdida = si` en reuniones `base` ÷ decisiones de reuniones `base`.
2. **Tasa con cierre** = lo mismo, en reuniones `cierre`, contando **todas** las filas (`observada`, `confirmada` y `ambas`). Una decisión que se conversó y el cierre dejó fuera cuenta igual.
3. **Por serie:** las dos tasas calculadas dentro de cada serie, y si la de cierre es menor que la base.

| Resultado | Condición |
|---|---|
| **Mínimo para leer** | ≥ 30 decisiones en reuniones `cierre` y ≥ 15 en `base`. Si no → `inconclusive` |
| **Pasa** | tasa con cierre ≤ la mitad de la tasa base **y** baja en ≥ 4 de 5 series |
| **Falla** | reducción relativa < 25% **o** baja en ≤ 2 series |
| **Entre medio** | ni pasa ni falla → decisión `change` según la regla del diseño |

Diagnóstico (no cambia el resultado): en reuniones con cierre, % de filas con `origen = observada` (decisiones que el cierre no recogió) y su tasa de pérdida, comparada con la de `ambas`/`confirmada`.

Para la regla de `change` revisar además:
- % de reuniones con cierre donde `cierre_mas_de_2_min = si` (¿más de la mitad?).
- Entre las decisiones perdidas con cierre, cuántas tenían `sin_dueno = si` o el responsable respondió "pensé que lo hacía otro" (notas).
