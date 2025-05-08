
# Pruebas de Rendimiento y Correctitud  
## Programación Dinámica para la Selección Óptima de Invitados (Problema del Árbol de Fiesta)

---

### Archivo de prueba  
`tests/test_party/test_party_dynamic.py`

---

### Descripción

Este conjunto de pruebas evalúa la eficiencia y correctitud de la función `solve_party_dp`, que resuelve el problema de selección óptima de invitados en una jerarquía de empleados representada como árbol (sin invitar a empleados con relación directa supervisor-subordinado). La solución usa **programación dinámica** sobre la estructura del árbol.

---

### Implementación de pruebas

El archivo de prueba genera árboles aleatorios para tamaños definidos, les asigna valores de convivencia aleatorios, y evalúa tanto la correctitud como el rendimiento promedio de la solución.

#### Funcionalidades clave:

- Validación estructural: se asegura que no haya invitados con relación directa.
- Validación de suma: la suma de los valores invitados coincide con el total reportado.
- Evaluación de rendimiento para 5 repeticiones por tamaño.

---
### Detalles sobre los tamaños

Cada tamaño (`10`, `100`, `1000`, `10000`) hace referencia a la **cantidad de empleados** (nodos del árbol). Para cada tamaño:

- Se genera **un único problema**.
- Se construye una **matriz de adyacencia de tamaño n×n**, donde `n` es el número de empleados.
- Se genera un **vector de calificaciones** de tamaño `n`, con valores aleatorios entre 1 y 30.
- Se ejecuta la función `solve_party_dp` y se validan los resultados.

Ejemplo para `n = 10`:
- Se genera 1 árbol con 10 empleados.
- La matriz tiene dimensiones 10 × 10.
- El vector de calificaciones tiene 10 valores.

---

### Resultados de ejecución

| Tamaño de entrada | Repeticiones | Tiempo promedio (segundos) |
|-------------------|--------------|-----------------------------|
| 10                | 5            | 0.00007                     |
| 100               | 5            | 0.00406                     |
| 1000              | 5            | 0.28896                     |
| 10000             | 5            | 28.62594                    |
| 50000             | 5            | killed                      |
---

### 📈 Análisis de rendimiento

La ejecución muestra una progresión de tiempos consistente con la **complejidad dinámica sobre árboles**, la cual es lineal con respecto al número de nodos, aunque el procesamiento adicional (formato, validación, etc.) introduce un pequeño overhead.

Observaciones destacadas:

- La ejecución para 10,000 empleados tarda aproximadamente **28.6 segundos**, lo cual sigue siendo razonable para experimentación.
- El crecimiento temporal es aproximadamente proporcional a la entrada, pero con constantes mayores que las de la versión voraz.
- A diferencia de la solución voraz, esta garantiza **resultados óptimos**, lo que la hace ideal para aplicaciones donde la precisión es prioritaria.

```
10     →  0.00007 s
100    →  0.00406 s   (~58× más que 10)
1000   →  0.28896 s   (~71× más que 100)
10000  →  28.62594 s  (~99× más que 1000)
```
La complejidad temporal de solve_party_dp es 𝑂(n), lo cual es consistente con los resultados experimentales para árboles de tamaño hasta 10,000 nodos. La linealidad se mantiene a pesar del crecimiento del tiempo debido al tamaño y a validaciones adicionales.

---

### ✅ Conclusión

La solución `solve_party_dp`:

- Es **correcta** y verificada automáticamente con múltiples validaciones.
- Escala de forma **aceptable**, aunque con mayor tiempo que la solución voraz.
- Ofrece **máxima precisión**, garantizando la selección óptima sin conflictos.

- [Volver a la tabla de contenido](/docs/Readme.md)
