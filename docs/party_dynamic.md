# solucion programacion dinamica 

## party_dynamic.py

- [implementacion del algoritmo programacio dinamica](../src/ejercicios/party/party_dynamic.py)
- [Volver a la tabla de contenido](/docs/Readme.md)

Este módulo implementa una solución por programacion dinamica para resolver el problema de planificación de una fiesta de empleados. El objetivo es maximizar la suma de las calificaciones de convivencia de los empleados invitados, evitando invitar a un supervisor directo juntos

Este enfoque usa programación dinámica sobre árboles. La jerarquía organizacional se representa como un árbol, y se aplica un recorrido DFS para computar la mejor combinación posible de invitados en subárboles.

### Funcion principal:

- **def solve_party_dp(lines):**
    Recibe una lista de líneas (lines), donde la primera línea contiene el número de casos (num_problems).


### Función Auxiliar:

- **def recover_selected(tree, dp, node, parent_included, invited):***
    Se recupera la decisión óptima para el nodo actual, El booleano parent_included indica si el padre fue invitado.

- **def build_tree_dp(matrix):**

- **def tree_dp(tree, values, root):**


### Explicacion del algoritmos:

**def solve_party_dp** :

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
        tree, root = build_tree_dp(matrix)
        dp = tree_dp(tree, values, root)
        invited = [0] * m
        recover_selected(tree, dp, root, False, invited)
        total = max(dp[root][0], dp[root][1])
        results.append(" ".join(map(str, invited)) + f" {total}")

```

- build_tree_dp(matrix): transforma la matriz en una estructura de árbol y determina la raíz.
- tree_dp(...): realiza programación dinámica en el árbol, obteniendo los valores óptimos con y sin invitar cada nodo.
- recover_selected(...): reconstruye la lista de empleados invitados.
- total: elige el máximo entre invitar o no invitar a la raíz.
- El resultado se guarda como: cadena binaria de invitados + suma total.

**def build_tree_dp** :

```
    n = len(matrix)
    children = {i: [] for i in range(n)}
    indegree = [0] * n
```
- children[i] será la lista de subordinados del nodo i, indegree[i] cuenta cuántos supervisores tiene el nodo i.

```
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                children[i].append(j)
                indegree[j] += 1
```
- Se construye el árbol jerárquico desde la matriz de adyacencia. i → j significa que i es supervisor de j.

```
    root = indegree.index(0)
    return children, root
```
- El nodo raíz es aquel que no tiene supervisores (indegree == 0).
- Se retorna el árbol y la raíz identificada.

**def tree_dp** :

```
    dp = {}
```
- dp[u] = (sin_invitar, con_invitar)
- dp[u][0]: mejor resultado si u no es invitado.
- dp[u][1]: mejor resultado si u sí es invitado.

```
    def dfs(u):
        include = values[u]
        exclude = 0
```
- nclude: si se invita a u, se empieza sumando su valor
- exclude: si no se invita a u, se acumularán los mejores resultados de los hijos.

```
        for v in tree[u]:
            dfs(v)
            exclude += max(dp[v][0], dp[v][1])
            include += dp[v][0]
```
- Si u no es invitado, se puede tomar lo mejor de cada hijo (v), Si u es invitado, ningún hijo puede serlo → solo se suma dp[v][0].

**def recover_selected** :

```
    if parent_included:
        invited[node] = 0
        for child in tree[node]:
            recover_selected(tree, dp, child, False, invited)
```
- Si el padre fue invitado, el nodo actual no puede serlo.

```
    else:
        if include > exclude:
            invited[node] = 1
            for child in tree[node]:
                recover_selected(tree, dp, child, True, invited)
        else:
            invited[node] = 0
            for child in tree[node]:
                recover_selected(tree, dp, child, False, invited)
```
- Si el padre no fue invitado, se elige entre invitar o no al nodo actual, según cuál produce mayor puntuación. Se propaga el estado a los hijos.

### Analisis complejidad:

- **Tiempo**: O(n), donde n es el número de empleados.

    - Cada nodo se visita una vez.

    - Por cada nodo, se procesan sus hijos, lo cual es proporcional al número total de aristas.

- **Espacio**:

    - Diccionario dp → O(n)

    - ista de invitados → O(n)

    - Pila de recursión DFS → O(h), donde h es la altura del árbol.