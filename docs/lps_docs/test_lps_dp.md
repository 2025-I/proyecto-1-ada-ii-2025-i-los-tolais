# Pruebas de Rendimiento y Correctitud  
## Programación Dinámica para la Subsecuencia Palindrómica Más Larga (LPS)

---

###  Archivo de prueba  
`tests/test_lps/test_lps_dp.py`

---

### Descripción

Este conjunto de pruebas evalúa la eficiencia y correctitud de la función `solve_lps_dp`, la cual resuelve el problema de la **subsecuencia palindrómica más larga (LPS)** mediante **programación dinámica**. Las pruebas están diseñadas para validar tanto la exactitud de los resultados como el rendimiento en distintos tamaños de entrada.

---

### Implementación de pruebas

El archivo contiene la clase `TestDPRepetition`, que hereda de `TestRepetition` y usa un generador de datos sintéticos para ejecutar la función sobre múltiples frases.

#### Funciones clave:

- `setUp`: Configura el algoritmo a testear.
- `run_scaled_test(num_elements, repetitions)`: 
  - Genera entradas y salidas esperadas.
  - Ejecuta el algoritmo múltiples veces.
  - Verifica correctitud.
  - Mide tiempo promedio de ejecución.

#### Pruebas implementadas:

```python
def test_juguete_dynamic(self):        # 10 frases
def test_pequeno_dynamic(self):        # 100 frases
def test_mediano_dynamic(self):        # 1000 frases
def test_grande_dynamic(self):         # 10000 frases
def test_extra_grande_dynamic(self):   # 50000 frases
```
---
### Resultados de ejecución

| Tamaño de entrada | Repeticiones | Tiempo promedio (segundos) |
|-------------------|--------------|-----------------------------|
| 10                | 5            | 0.0030                      |
| 100               | 5            | 0.0189                      |
| 1000              | 5            | 0.1884                      |
| 10000             | 5            | 1.8877                      |
| 50000             | 5            | 9.4078                      |

---
### Análisis de rendimiento

El tiempo de ejecución promedio crece de forma **cuadrática** respecto al número de frases analizadas, lo cual es coherente con la **complejidad temporal O(n²)** de la solución por programación dinámica.

Conclusiones:

- La ejecución para 50,000 frases toma cerca de 9.4 segundos, lo cual es aceptable para un entorno experimental.
- La función escala adecuadamente y mantiene tiempos de respuesta manejables hasta volúmenes grandes.
- El crecimiento temporal muestra una progresión consistente:

```
10     →  0.0030 s
100    →  0.0189 s   (~6.3× más que para 10)
1000   →  0.1884 s   (~10× más que para 100)
10000  →  1.8877 s   (~10× más que para 1000)
50000  →  9.4078 s   (~5× más que para 10000)
```

Esto confirma la escalabilidad de la solución y la efectividad del enfoque dinámico.

---

###  Conclusión

La solución `solve_lps_dp` basada en programación dinámica:

-No es la más **veloz** ni la más **lenta**, pero sí es la más **precisa**
- Es **correcta** (verificada con pruebas automatizadas y comparación contra salidas esperadas).
- Es **eficiente** y escalable a grandes volúmenes de entrada.
- Cumple con las exigencias del proyecto en cuanto a rendimiento y exactitud.

- [Volver a la tabla de contenido](/docs/Readme.md)