# Documentación de Implementación

## lps_brute.py
Este módulo implementa una solución de fuerza bruta para encontrar la subsecuencia palindrómica más larga (Longest Palindromic Subsequence, LPS) en una cadena dada. La solución evalúa todas las subsecuencias posibles de la cadena y verifica cuáles son palíndromos, seleccionando la más larga. Aunque es una solución simple, tiene una complejidad computacional alta debido a la exploración exhaustiva de todas las subsecuencias posibles.

### Funciones principales:
- **lps_brute(s: str) -> int**: Calcula la longitud de la subsecuencia palindrómica más larga utilizando fuerza bruta.

### Complejidad:
- Tiempo: O(2^n), donde `n` es la longitud de la cadena.
- Espacio: O(n) debido a la pila de recursión.

---

## lps_dynamic.py
Este módulo implementa una solución basada en programación dinámica para encontrar la subsecuencia palindrómica más larga. Utiliza una tabla bidimensional para almacenar los resultados de subproblemas, evitando cálculos redundantes y mejorando significativamente la eficiencia en comparación con la solución de fuerza bruta.

### Funciones principales:
- **lps_dynamic(s: str) -> int**: Calcula la longitud de la subsecuencia palindrómica más larga utilizando programación dinámica.

### Complejidad:
- Tiempo: O(n^2), donde `n` es la longitud de la cadena.
- Espacio: O(n^2) debido a la tabla utilizada para almacenar los resultados intermedios.

---

## lps_voraz
Este módulo implementa una solución voraz (greedy) para encontrar la subsecuencia palindrómica más larga. Aunque esta aproximación puede ser más rápida en algunos casos, no garantiza encontrar la solución óptima en todos los escenarios, ya que no evalúa todas las posibilidades como lo hacen las soluciones de fuerza bruta o programación dinámica.

### Funciones principales:
- **lps_voraz(s: str) -> int**: Calcula una aproximación de la longitud de la subsecuencia palindrómica más larga utilizando un enfoque voraz.

### Complejidad:
- Tiempo: Depende de la implementación, pero generalmente es más eficiente que la fuerza bruta.
- Espacio: O(1) o O(n), dependiendo de si se utiliza memoria adicional para almacenar resultados intermedios.

---

## Comparación de Métodos
| Método         | Complejidad Temporal | Complejidad Espacial | Precisión |
|----------------|-----------------------|-----------------------|-----------|
| Fuerza Bruta   | O(2^n)               | O(n)                 | Óptima    |
| Programación Dinámica | O(n^2)         | O(n^2)               | Óptima    |
| Voraz          | Depende de la implementación | O(1) o O(n)   | Aproximada |

### Notas:
- La solución de fuerza bruta es útil para comprender el problema, pero no es práctica para cadenas largas.
- La solución de programación dinámica es la más recomendada para obtener resultados óptimos con una complejidad razonable.
- La solución voraz puede ser útil en escenarios donde la velocidad es más importante que la precisión.