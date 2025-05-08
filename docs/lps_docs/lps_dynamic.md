# Solucion Programación dinamica.

## lps_dynamic.py
- [implementacion del algoritmo por progamación dinamica](../src/ejercicios/lps/lps_dynamic.py)
- [Volver a la tabla de contenido](/docs/Readme.md)

Este módulo implementa una solución basada en programación dinámica para encontrar la subsecuencia palindrómica más larga. Utiliza una tabla bidimensional para almacenar los resultados de subproblemas, evitando cálculos redundantes y mejorando significativamente la eficiencia en comparación con la solución de fuerza bruta.

### Función Principal:
- **def solve_lps_dp(lines: list[str]) -> list[str]:**: devuelve la lista de las subcadenas palindrómicas continuas más largas, una por cada línea de entrada.

### Explicacion del algoritmo:

```
        try:
            n = int(lines[0])
            raws = lines[1 : 1 + n]
        except ValueError:
            raws = lines
```
- Si la primera línea es un número n, toma las n siguientes como casos.
- Si no, considera todas las líneas.
```
        out = []
        for raw in raws:
            s = normalize(raw)
            m = len(s)
            if m == 0:
                out.append("")
                continue
```
- Normaliza (quita no-alfanuméricos, pasa a minúsculas).
- Si la cadena queda vacía, añade "" y sigue.
```
            P = [[False] * m for _ in range(m)]
            start, max_len = 0, 1
```
- P[i][j] será True si s[i..j] es palíndromo.
- start y max_len registran la subcadena óptima encontrada.

- **Caso Base longitud 1**
```
            for i in range(m):
                P[i][i] = True
```
- Es caso base porque un caracter es palindromo.
- **Caso Base longitud 2**
```
            for i in range(m-1):
                if s[i] == s[i+1]:
                    P[i][i+1] = True
                    start, max_len = i, 2
```
- Marca pares iguales como palíndromos de longitud 2.

- **Subcadenas de longitud ≥ 3**
```
            for length in range(3, m+1):
                for i in range(0, m-length+1):
                    j = i + length - 1
                    if s[i] == s[j] and P[i+1][j-1]:
                        P[i][j] = True
                        if length > max_len:
                            start, max_len = i, length
```
- Recorre todas las longitudes desde 3 hasta m.

- Para cada par (i,j), marca palíndromo si los extremos coinciden y el interior ya era palíndromo.

- **Extraer la subcadena óptima**
```
                    out.append(s[start : start + max_len])
```
- Añade la mejor subcadena encontrada a la lista de resultados.

```
                return out
```
- **Devolver resultados**


### Análisis de Complejidad:
- **Tiempo**: 
    - Sea $n=\lvert s\rvert$ 
    la longitud de la cadena normalizada.
    - Crear `P` cuesta $O(n^2)$ espacio y tiempo.
    - **Casos Base**
        * Longitud 1: bucle único de $n$ iteraciones → $O(n)$.
        * Longitud 2: bucle de $n-1$ iteraciones → $O(n)$.
    - **Rellenar DP para longitudes ≥3**
        * `length` va de 3 a $n$ → $n-2$ valores.
        * Para cada `length`, `i` recorre de 0 a $n-\text{length}$ → en total
    $
         \sum_{\ell=3}^{n}(n-\ell+1)
         \;=\;
         \sum_{k=1}^{n-2}k
         \;=\;\frac{(n-2)(n-1)}{2}
         \;=\;O(n^2)
    $
    - **Extraer resultado**
        Operación de slicing $O(n)$, pero ejecutada una sola vez por cadena → $O(n)$.
        por tanto, el tiempo total es:
        $
        O(n^2)\;+\;O(n)\;+\;O(n^2)\;+\;O(n)
        \;=\;
        O(n^2)
        $


- **Espacio**: $O(n^2)$ debido a la tabla utilizada para almacenar los resultados intermedios (la matriz `P` de tamaño $n\times n$, es decir, **O(n²)**)