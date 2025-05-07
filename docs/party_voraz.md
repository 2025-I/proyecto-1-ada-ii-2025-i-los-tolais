# solucion programacion dinamica 

## party_dynamic.py

- [implementacion del algoritmo programacio dinamica](../src/ejercicios/party/party_dynamic.py)
- [Volver a la tabla de contenido](/docs/Readme.md)

Este módulo implementa una solución por programacion voraz para resolver el problema de planificación de una fiesta de empleados. El objetivo es maximizar la suma de las calificaciones de convivencia de los empleados invitados, evitando invitar a un supervisor directo juntos.

Este análisis explica en detalle el funcionamiento de la solución voraz para resolver el problema de maximizar la calificación de convivencia en una fiesta, bajo la restricción de no invitar a empleados supervisores entre sí.

### Funcion principal:

- **def solve_party_voraz(lines):**
    Recibe una lista de líneas (lines), donde la primera línea contiene el número de casos (num_problems).


### Función Auxiliar:

- **def build_tree_voraz(matrix)***
    Recibe como parámetro una matriz de adyacencia, que representa una relación jerárquica entre empleados en forma de grafo dirigido (usualmente un árbol).

- **def voraz(tree, values):**
    Maximiza el puntaje total de convivencia sin invitar a un empleado y su supervisor directo.


### Explicacion del algoritmos:

**def solve_party_voraz** :

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

**def build_tree_voraz** :

```
    tree = {}
    n = len(matrix)
    for i in range(n):
        tree[i] = []
```
- Se inicializa un diccionario vacío tree donde cada nodo representa un empleado y su lista de subordinados.

```
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                tree[i].append(j)
    return tree
```
- La matriz se recorre para construir las relaciones de supervisión.
- Si matrix[i][j] == 1, significa que el empleado i es supervisor directo de j.

**def voraz** :

```
    n = len(values)
    score = [(values[i], i) for i in range(n)]
    score.sort(reverse=True)
```
- Se construye una lista score con pares (valor, índice) para cada empleado.
- La lista se ordena de mayor a menor según la calificación de convivencia.

```
    invited = [0] * n
    banned = set()
```
- invited[i] = 1 indica que el empleado i fue invitado.
- banned es un conjunto que mantiene a los empleados que no pueden ser invitados (por ser supervisores o supervisados de otros ya invitados).

```
    for val, i in score:
        if i not in banned:
            invited[i] = 1
            banned.update(tree[i])
            for parent in tree:
                if i in tree[parent]:
                    banned.add(parent)
```
- Idea principal: Invitar a los empleados con mayor valor siempre que no violen la restricción de jerarquía.
- Se recorren los empleados de mayor a menor valor, si un empleado no está en banned, se le invita
- Se agregan sus subordinados a banned o se busca en el árbol a los supervisores que lo tienen como hijo y también se banean.

```
    total = sum(values[i] for i in range(n) if invited[i])
    return invited, total
```
- Se calcula el total de calificaciones de los invitados.
- Se retorna: invited: lista binaria indicando los invitados, total: suma de las calificaciones.

### Analicis complejidad:

- **Tiempo** :

    O(n²) en el peor caso, dominado por:

    - La construcción del árbol O(n²)

    - La búsqueda de supervisores (parent loop) en cada paso de selección.

- **Espacil** :

    O(n²), dominada por la matriz de adyacencia y la estructura del árbol.