# solucion fuerza bruta

## party_brute.py

- [implementacion del algoritmo por fuerza bruta](../src/ejercicios/party/party_brute.py)
- [Volver a la tabla de contenido](/docs/Readme.md)

Este módulo implementa una solución por fuerza bruta para resolver el problema de planificación de una fiesta de empleados. El objetivo es maximizar la suma de las calificaciones de convivencia de los empleados invitados, evitando invitar a un supervisor directo juntos

La solución explora todas las posibles combinaciones binarias de asistencia (0 = no invitado, 1 = invitado) y verifica que la combinación sea válida según las relaciones jerárquicas representadas por una matriz de adyacencia.

### Funcion principal:

- **def solve_party_brute(lines: list[str]) -> list[str]:** :
    Recibe una lista de cadenas que representan uno o más problemas de planificación. Devuelve una lista de strings donde cada línea representa una solución válida con la suma máxima de calificaciones.

### Funciones auxiliares: 

- **def build_tree_brute(matrix: list[list[int]]) -> dict[int, list[int]]:** :
    Construye un árbol jerárquico a partir de la matriz de adyacencia (0 = no relación, 1 = supervisión directa).

- **def brute_force(tree, values):**:
    Recibe como parametros tree: Diccionario de jerarquía, tree: Diccionario de jerarquía, values: Lista de calificaciones de convivencia
    y retorna Tupla (best_combo, max_total) que representa la mejor combinación válida de invitados y su suma total.

### Explicacion del algoritmos:

**def solve_party_brute** :

```
    index = 1
    results = []
    num_problems = int(lines[0])

```
- Lee el número de problemas desde la primera línea.
- results = []: lista que almacenará los resultados de cada instancia.

```
    for _ in range(num_problems):
    m = int(lines[index])
    matrix = [list(map(int, lines[index + i + 1].split())) for i in range(m)]
    values = list(map(int, lines[index + m + 1].split()))
    index += m + 2
```
- Extrae la cantidad de empleados (m), la matriz de adyacencia y las calificaciones.
- m es el número de empleados.
- matrix es la matriz de adyacencia (supervisor → subordinado).
- values contiene las calificaciones de convivencia de cada empleado.
- Se avanza index para posicionarse en la siguiente instancia.

```
    tree = build_tree_brute(matrix)
    invited, total = brute_force(tree, values)
```
- Construye un árbol jerárquico a partir de la matriz y aplica la solución de fuerza bruta.

```
    result_line = " ".join(str(i) for i in invited) + f" {total}"
    results.append(result_line)
```
- Formate y almacena la solucion

**def build_tree_brute**:

```
tree = {i: [] for i in range(len(matrix))}
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            tree[i].append(j)
```
- Recorre la matriz y registra las relaciones de supervisión directa.

**def brute_force**:

```
for combo in product([0, 1], repeat=n):
```
- Genera todas las combinaciones posibles de invitados: $2^n$ combinaciones.

```
        valid = True
        for parent in range(n):
            if combo[parent] == 1:
                for child in tree[parent]:
                    if combo[child] == 1:
                        valid = False
                        break
```
- Verifica que no haya invitados que sean supervisor y subordinado a la vez.

```
        if valid:
            total = sum(values[i] for i in range(n) if combo[i] == 1)
            if total > max_total:
                max_total = total
                best_combo = list(combo)
```
- Si la combinación es válida, calcula la suma y actualiza si es la mejor encontrada.

### Análisis de Complejidad

- **Tiempo** 

    - Generación de combinaciones: $2^n$

    - Verificación de validez: $O(n)$ por combinación

    - Cálculo de suma: $O(n)$ por combinación

    - Complejidad Total: $O(n \cdot 2^n)$

- **Espacio**

    Se utiliza:

    - Un árbol de relaciones ($O(n^2)$ en el peor caso si todos supervisan a todos)

    - Combinación actual y mejor combinación ($O(n)$)

    - Complejidad Espacial: $O(n^2)$ en peor caso, usualmente $O(n)$ si jerarquía es un árbol.