
# Pruebas de Rendimiento y Correctitud  
## Algoritmo Voraz para la Fiesta Empresarial

---

### Archivo de prueba  
`tests/test_party/test_party_voraz.py`

---

### Descripción

Este conjunto de pruebas evalúa la eficiencia y correctitud de la función `solve_party_voraz`, la cual resuelve el problema de la **selección óptima de invitados en una jerarquía empresarial** mediante una estrategia **voraz**. Las pruebas están diseñadas para validar la exactitud de los resultados, así como el tiempo de ejecución promedio para diferentes tamaños de entrada.

---

### Implementación de pruebas

El archivo contiene pruebas parametrizadas con `pytest` que se ejecutan 5 veces por cada tamaño de entrada. Para cada repetición:

- Se genera una jerarquía aleatoria (matriz de adyacencia).
- Se generan calificaciones aleatorias entre 1 y 30.
- Se mide el tiempo de ejecución de `solve_party_voraz`.
- Se valida que:
  - No se invite a empleados en relación directa padre-hijo.
  - La suma total de calificaciones sea correcta.

Se imprime el **tiempo promedio por tamaño** tras completar las 5 repeticiones.

---
### Detalles sobre los tamaños
Cada tamaño (`10`, `100`, `1000`, `10000`) hace referencia a la **cantidad de empleados** (nodos del árbol). Para cada tamaño:

- Se genera **un único problema**.
- Se construye una **matriz de adyacencia de tamaño n×n**, donde `n` es el número de empleados.
- Se genera un **vector de calificaciones** de tamaño `n`, con valores aleatorios entre 1 y 30.
- Se ejecuta la función `solve_party_dp` y se validan los resultados.

Ejemplo para `n = 10000`:

 - Se genera 1 árbol con 10000 empleados.
 - La matriz de adyacencia tiene dimensiones 10000 × 10000, lo que representa todas las posibles relaciones padre-hijo.
 - El vector de calificaciones contiene 10000 valores aleatorios.
 - El algoritmo determina a qué empleados invitar para maximizar la suma de calificaciones sin invitar supervisores directos.

La prueba también valida que:

 - No haya relaciones padre-hijo entre los invitados. 
 - La suma reportada coincida con las calificaciones de los invitados.

### Pruebas implementadas:

```python
@pytest.mark.parametrize("size,label", [...])
@pytest.mark.parametrize("repeat", range(5))
def test_party_voraz_scaled(size, label, repeat):
    ...
```

---

### Resultados de ejecución

| Tamaño de entrada  | Repeticiones  | Tiempo promedio (segundos)   |
|------------------- |-------------- |------------------------------|
| 10 (juguete)       | 5             | 0.00008                      |
| 100 (pequeño)      | 5             | 0.00418                      |
| 1000 (mediano)     | 5             | 0.34582                      |
| 10000 (grande)     | 5             | 34.99133                     |
| 50000(extra_grande)| 5             |  killed                      |
---

### 📈 Análisis de rendimiento

El tiempo de ejecución muestra un crecimiento **exponencial** al aumentar el tamaño del problema. A pesar de que el algoritmo voraz es conceptualmente rápido, la implementación actual **no escala bien** para entradas grandes.

Comparación relativa:

```
10      →   0.00008 s
100     →   0.00418 s    (~52× más que 10)
1000    →   0.34582 s    (~82× más que 100)
10000   →  34.99133 s    (~101× más que 1000)
```

Esto sugiere un comportamiento cercano a **O(n²)** o incluso **O(n³)** dependiendo de la estructura del árbol y del recorrido empleado. El tiempo para 10,000 empleados (~35 segundos) ya no es práctico para aplicaciones interactivas o tiempo real.

---

### ✅ Conclusión

La solución `solve_party_voraz`:

- **Es correcta**, pasando todas las validaciones de estructura y sumatoria.
- Tiene **una escalabilidad limitada**, con tiempos de ejecución que crecen rápidamente.
- Es **apropiada para tamaños pequeños o medianos**, pero no recomendable para instancias grandes.

- [Volver a la tabla de contenido](/docs/Readme.md)
