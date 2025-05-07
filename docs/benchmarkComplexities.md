## Resultados del benchmark
A continuación se presentan tres gráficas obtenidas al medir el tiempo de ejecución medio (en nanosegundos) de nuestros tres algoritmos de LPS (Fuerza Bruta, Programación Dinámica y Greedy) para cadenas de diferentes longitudes $n$.  

- [volver a la tabla de contenido](/docs/Readme.md)

- **Figura 1.** Tiempo medio de ejecución frente a $n$ en escala lineal. 
![Figura 1: lineal](/docs/images/Figure_1.png)
- **Escala lineal (Fig. 1)**:

    * El algoritmo de **Fuerza Bruta** (curva azul) muestra un crecimiento muy acelerado a medida que $n$ aumenta, mientras que **DP** (naranja) y **Greedy** (verde) crecen muchísimo más despacio.

   * Para $n=200$, la fuerza bruta supera los $1\cdot10^7$ ns, mientras que DP está alrededor de $4.8\cdot10^6$ ns y Greedy apenas $3\cdot10^5$ ns.

- **Figura 2.** Tiempo medio de ejecución frente a $n$ en escala logaritmica
---
![Figura 2: log-log](/docs/images/Figure_2.png)
- *Escala logaritmica (Fig. 2):*

    * En un gráfico logarítmico, las funciones polinómicas $n^k$ aparecen como líneas rectas de pendiente $k$.

    * La **pendiente** de la curva “Brute” es aproximadamente **3**, confirmando empíricamente su $O(n^3)$.

    * Las curvas de **DP** y **Greedy** tienen pendiente cercana a **2**, lo que coincide con su complejidad teórica $O(n^2)$.

    * Las líneas de referencia trazadas ($O(n^2)$ en rojo punteado y $O(n^3)$ en morado punteado) se solapan con las mediciones, validando el modelo.