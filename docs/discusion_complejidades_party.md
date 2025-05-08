# Informe de Análisis: Comparación de Complejidades en el Problema de Selección de Invitados para Fiesta Empresarial

![Graficos](/docs/images/ComparacionesComplejidadesParty.png)
## Introducción
El problema de selección de invitados para una fiesta empresarial es un desafío de optimización en estructuras jerárquicas. Debemos maximizar la suma de calificaciones de convivencia de los empleados invitados, con la restricción de que ningún invitado puede ser supervisor directo de otro. Este informe analiza tres enfoques para resolver este problema: Fuerza Bruta, Programación Dinámica y Algoritmos Greedy.

## Análisis de Complejidades

### Complejidad Teórica

#### Fuerza Bruta
- **Teórica**: O(2^n)
- **Explicación**: Exponencial, ya que evalúa todos los posibles subconjuntos de empleados

#### Programación Dinámica
- **Teórica**: O(n)
- **Explicación**: Lineal, aprovechando la estructura de árbol y almacenamiento de subproblemas

#### Algoritmo Greedy
- **Teórica**: O(n)
- **Explicación**: Lineal, utilizando heurísticas locales para selección de nodos

### Complejidad Experimental

#### Fuerza Bruta:

**Experimental**: O(2^n)
Coincide con la teoría, confirmando su naturaleza exponencial

#### Programación Dinámica:

**Experimental**: O(n)
Valida la eficiencia lineal teórica en la práctica

#### Algoritmo Greedy:

**Experimental**: O(n³)
Muestra peor desempeño que lo teórico, posiblemente por implementación subóptima

## Discusión de Resultados

### Consistencia entre Teoría y Práctica
- **Programación Dinámica**: Coherencia perfecta (O(n) teórico vs O(n) experimental)
- **Fuerza Bruta**: Comportamiento exponencial confirmado

### Diferencias Notables
- **Algoritmo Greedy**:
  - **Teoría**: O(n)
  - **Práctica**: O(n³)
  - **Causas posibles**:
    1. Múltiples pasadas sobre los datos
    2. Verificación costosa de restricciones
    3. Heurísticas no óptimas

## Conclusión y Recomendaciones

### Conclusiones Clave
1. **Programación Dinámica** es la solución óptima (eficiente y garantizada)
2. **Algoritmos Greedy** pueden degradarse en la práctica
3. **Fuerza Bruta** solo aplicable a instancias pequeñas
