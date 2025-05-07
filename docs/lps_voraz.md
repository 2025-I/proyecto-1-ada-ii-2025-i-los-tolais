## lps_voraz
Este módulo implementa una solución voraz (greedy) para encontrar la subsecuencia palindrómica más larga. Aunque esta aproximación puede ser más rápida en algunos casos, no garantiza encontrar la solución óptima en todos los escenarios, ya que no evalúa todas las posibilidades como lo hacen las soluciones de fuerza bruta o programación dinámica.

### Funciones principales:
- **lps_voraz(s: str) -> int**: Calcula una aproximación de la longitud de la subsecuencia palindrómica más larga utilizando un enfoque voraz.

### Complejidad:
- Tiempo: Depende de la implementación, pero generalmente es más eficiente que la fuerza bruta.
- Espacio: O(1) o O(n), dependiendo de si se utiliza memoria adicional para almacenar resultados intermedios.