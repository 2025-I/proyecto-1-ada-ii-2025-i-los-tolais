# Pruebas de Rendimiento y Correctitud  
## Algoritmo Voraz para la Subsecuencia Palindrómica Más Larga (LPS)

---

### Archivo de prueba  
`tests/test_lps/test_lps_greedy.py`

---

### Descripción

Este conjunto de pruebas evalúa la eficiencia y correctitud de la función `solve_lps_greedy`, que resuelve el problema de la **subsecuencia palindrómica más larga (LPS)** mediante un enfoque **voraz**. Las pruebas están diseñadas para validar tanto la exactitud de los resultados como el rendimiento en distintos tamaños de entrada.

---

### Implementación de pruebas

El archivo contiene la clase `TestGreedyRepetition`, que hereda de `TestRepetition` y utiliza un generador de datos sintéticos para ejecutar la función sobre múltiples frases.

#### Funciones clave:

- `setUp`: Configura el algoritmo a testear.
- `run_scaled_test(num_elements, repetitions)`: 
  - Genera entradas y salidas esperadas.
  - Ejecuta el algoritmo múltiples veces.
  - Verifica la correctitud.
  - Mide el tiempo promedio de ejecución.

#### Pruebas implementadas:

```python
def test_juguete_voraz(self):        # 10 frases
def test_pequeno_voraz(self):        # 100 frases
def test_mediano_voraz(self):        # 1000 frases
def test_grande_voraz(self):         # 10000 frases
def test_extra_grande_voraz(self):   # 50000 frases
```
---
### Resultados de ejecución

A continuación se muestran los tiempos promedio de ejecución para cada tamaño de entrada evaluado:

| Tamaño de entrada | Repeticiones | Tiempo promedio (segundos) |
|-------------------|--------------|----------------------------|
| 10                | 5            | 0.00087                    |
| 100               | 5            | 0.00674                    |
| 1000              | 5            | 0.06479                    |
| 10000             | 5            | 0.65002                    |
| 50000             | 5            | 3.26874                    |

---
### Análisis de rendimiento

El tiempo de ejecución promedio crece de forma lineal respecto al número de frases analizadas, lo cual es coherente con la complejidad temporal O(n) de la solución voraz.

Conclusiones:

- La ejecución para 50,000 frases toma cerca de 2.9 segundos, lo cual es aceptable para un entorno experimental.

- La función escala adecuadamente y mantiene tiempos de respuesta manejables hasta volúmenes grandes.

- El crecimiento temporal muestra una progresión consistente:

```
10     →  0.0012 s
100    →  0.0056 s   (~4.7× más que para 10)
1000   →  0.0582 s   (~10.4× más que para 100)
10000  →  0.5834 s   (~10× más que para 1000)
50000  →  2.9123 s   (~5× más que para 10000)
Esto confirma la escalabilidad de la solución y la efectividad del enfoque voraz.
```
---

### Conclusión

La solución `solve_lps_greedy` basada en un algoritmo voraz:

Es mucho más **veloz** que las otrás soluciones, pues su tiempo de ejecución crece de forma lineal por su complejidad temporal O(n).

Es **correcta** (verificada con pruebas automatizadas y comparación contra salidas esperadas).

Es **eficiente** y escalable a grandes volúmenes de entrada.

Cumple con las exigencias del proyecto en cuanto a rendimiento y exactitud.
