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

Por estas razones, **las pruebas para fuerza bruta se realizaron utilizando matrices de tamaño fijo `15 x 15`**, pero con cantidades variables de matrices generadas para simular la carga creciente (10, 100, 1000, 10000, 50000).

Cada caso se ejecutó con **5 repeticiones por tamaño** y se promediaron los tiempos.

---

## Resultados de ejecución

| Tamaño | Nº de matrices | Dimensión de cada matriz | Repeticiones | Tiempo promedio  |
| Juguete|    10          |       15 × 15            | 5            |   0.37340        |
| Pequeño|    100         |       15 × 15            | 5            |   3.55231        |
| Mediano|    1000        |       15 × 15            | 5            |   36.25317       |
| Grande |    10000       |       10 × 10            | 5            |   11.95405       |
| Extra  |    50000       |       10 × 10            | 5            |   60.90625       |        

---

## Conclusión

El enfoque de fuerza bruta es útil únicamente como **referencia de exactitud** frente a algoritmos más eficientes. Su uso queda limitado a tamaños pequeños (hasta ~15 empleados). Para escalabilidad y uso real, se recomienda emplear programación dinámica o algoritmos voraces.

- [Volver a la tabla de contenido](/docs/Readme.md)
