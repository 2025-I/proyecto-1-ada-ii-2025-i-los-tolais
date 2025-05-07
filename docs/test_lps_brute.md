# Informe de Pruebas – Fuerza Bruta para LPS (`solve_lps_brute`)

## Descripción

Este conjunto de pruebas evalúa la **correctitud** y el **rendimiento** del algoritmo de **fuerza bruta** `solve_lps_brute`, encargado de encontrar la subsecuencia palindrómica más larga en una lista de cadenas. Para verificar la precisión de los resultados, se compara contra la solución basada en **programación dinámica** (`solve_lps_dp`), la cual se considera como referencia confiable.

Las pruebas se ejecutan en distintos tamaños de entrada y repiten 5 veces cada escenario para calcular el tiempo promedio de ejecución.

---

##  Archivo de prueba

```python
tests/test_lps/test_lps_brute.py
```

---

## Funciones evaluadas

- `solve_lps_brute(inputs: List[str]) -> List[str]`: Implementación por fuerza bruta del problema LPS.
- `solve_lps_dp(inputs: List[str]) -> List[str]`: Usado como referencia de validación.

---

## Correctitud

Todas las pruebas pasaron exitosamente, indicando que `solve_lps_brute` entrega resultados válidos que **contienen** la subsecuencia palindrómica esperada, de acuerdo con los resultados obtenidos por el algoritmo dinámico.

---

## Resultados de ejecución

Las siguientes pruebas fueron ejecutadas con 5 repeticiones por tamaño de entrada. El tiempo promedio de ejecución (en segundos) fue el siguiente:

| Tamaño de entrada | Repeticiones | Tiempo promedio (segundos)  |
|-------------------|--------------|-----------------------------|
| 10                | 5            | 0.0061                      |
| 100               | 5            | 0.0540                      |
| 1000              | 5            | 0.5475                      |
| 10000             | 5            | 5.4753                      |
| 50000             | 5            | 27.4807                     |
---

## Análisis de desempeño

El algoritmo de fuerza bruta presenta una **escalabilidad pobre**, con un crecimiento del tiempo de ejecución cercano a **O(n³)** por cada entrada. Esto se debe a que evalúa todas las subsecuencias posibles para identificar cuál es palíndroma y de mayor longitud, lo que es computacionalmente costoso.

Por ejemplo:

- Al aumentar el tamaño de entrada de 1000 a 10000 (x10), el tiempo se multiplica por aproximadamente **10**.
- De 10000 a 50000 (x5), el tiempo se multiplica por un factor cercano a **5**, indicando un comportamiento **casi cúbico**, aunque los efectos del cache y procesamiento paralelo pueden suavizar ligeramente este crecimiento.

Este algoritmo es adecuado únicamente para entradas pequeñas o para propósitos comparativos (como validación).

---

##  Conclusión
- Es la solución más **lenta** de todas, pues su tiempo de ejecución crece **O(n³)**
- Correctitud confirmada frente a una solución de referencia.
- Requiere **muchos recursos computacionales** para listas grandes.
- Ideal para validación, no para producción o entrada de gran escala.
