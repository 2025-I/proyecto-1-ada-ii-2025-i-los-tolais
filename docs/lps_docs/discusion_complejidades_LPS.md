# Informe de Análisis: Comparación de Complejidades en el Problema LPS

![Graficos](/docs/images/ComparacionesComplejidadesLPS.png)

## Introducción
El problema de la Subsecuencia Palindrómica Más Larga (LPS, por sus siglas en inglés) es un desafío clásico en ciencias de la computación. Este informe analiza los resultados teóricos y experimentales de tres enfoques para resolver LPS: Fuerza Bruta, Programación Dinámica y Algoritmos Greedy.

## Análisis de Complejidades

### Complejidad Teórica
1. **Fuerza Bruta**:  
   - Teórica: O(2^n)  
   - Exponencial debido a la evaluación de todas las posibles subsecuencias.

2. **Programación Dinámica**:  
   - Teórica: O(n^2)  
   - Cuadrática por el uso de una tabla de tamaño n×n para almacenar subproblemas.

3. **Algoritmo Greedy**:  
   - Teórica: O(n)  
   - Lineal, asumiendo estrategias óptimas locales (aunque no siempre garantizan solución global óptima para LPS).

### Complejidad Experimental
- **Fuerza Bruta**:  
  - Experimental: O(n^2)  
  - Posible discrepancia debido a optimizaciones no consideradas en el modelo teórico o restricciones en el rango de pruebas.

- **Programación Dinámica**:  
  - Experimental: O(n^2)  
  - Coincide con la teoría, validando su eficiencia en la práctica.

- **Algoritmo Greedy**:  
  - Experimental: O(n)  
  - Confirma su escalabilidad lineal, pero la efectividad en calidad de solución puede variar.

## Discusión de Resultados
- **Consistencia**: La Programación Dinámica muestra coherencia perfecta entre teoría y práctica.  
- **Diferencias**:  
  - Fuerza Bruta exhibe mejor desempeño experimental, sugiriendo que las pruebas no alcanzaron tamaños de entrada suficientes para manifestar su naturaleza exponencial.  
  - Los algoritmos Greedy, aunque rápidos, pueden no ser precisos para LPS, ya que este problema generalmente requiere soluciones exactas.  

## Conclusión
La gráfica subraya la superioridad de la Programación Dinámica para LPS, equilibrando eficiencia y precisión. Mientras que los enfoques Greedy son rápidos, su aplicabilidad depende de si se toleran soluciones subóptimas. La Fuerza Bruta, aunque mejor de lo esperado en pruebas pequeñas, sigue siendo inviable para entradas grandes. Se recomienda validar los algoritmos Greedy en contextos donde la optimalidad no sea crítica.  
