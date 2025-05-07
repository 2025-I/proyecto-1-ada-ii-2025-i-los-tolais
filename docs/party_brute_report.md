# Informe de pruebas de eficiencia: Fuerza Bruta (`solve_party_brute`)

## Descripción

Este informe presenta los resultados de las pruebas de eficiencia realizadas al algoritmo de **fuerza bruta** para resolver el problema de invitación óptima a una fiesta corporativa.

A diferencia de los enfoques de programación dinámica y voraz, el algoritmo de fuerza bruta explora todas las combinaciones posibles de empleados invitados, lo que implica una **complejidad exponencial** en relación al número de empleados. Debido a esto, **no es viable utilizar matrices de gran tamaño** en las pruebas, como se hace con los otros enfoques.

---

## Limitaciones del enfoque de fuerza bruta

### 1. Complejidad computacional
- El número de combinaciones posibles para `n` empleados es \(2^n\).
- Para `n = 50,000`, esto supera por mucho las capacidades de cualquier sistema computacional actual.
- Incluso con `n = 30`, el algoritmo puede tardar varios minutos u horas.

### 2. Uso de memoria
- Una matriz de adyacencia de tamaño `50000 x 50000` implica 2.5 mil millones de elementos.
- Esto consume decenas de gigabytes de RAM, provocando fallos por falta de memoria.

### 3. Tiempo de ejecución
- Pruebas experimentales muestran que incluso `n = 20` puede tardar varios segundos.
- Con `n >= 25`, es posible que no termine en tiempos razonables.

Por estas razones, **las pruebas para fuerza bruta se realizaron utilizando matrices de tamaño fijo `20 x 20`**, pero con cantidades variables de matrices generadas para simular la carga creciente (10, 100, 1000, 10000, 50000).

Cada caso se ejecutó con **5 repeticiones por tamaño** y se promediaron los tiempos.

---

## Resultados de ejecución

| Tamaño | Nº de matrices | Dimensión de cada matriz | Repeticiones | Tiempo promedio |
| Juguete|    10          |       20 × 20            | 5            |   0.00017       |
| Juguete|    100         |       20 × 20            | 5            |   0.00018       |
| Juguete|    1000        |       20 × 20            | 5            |   0.00018       |
| Juguete|    10000       |       20 × 20            | 5            |   0.00018       |
| Juguete|    50000       |       20 × 20            | 5            |   0.00017       |        

> **Nota**: El tiempo es por ejecución de `solve_party_brute` sobre una única matriz de 15 × 15.

---

## Conclusión

El enfoque de fuerza bruta es útil únicamente como **referencia de exactitud** frente a algoritmos más eficientes. Su uso queda limitado a tamaños pequeños (hasta ~20 empleados). Para escalabilidad y uso real, se recomienda emplear programación dinámica o algoritmos voraces.