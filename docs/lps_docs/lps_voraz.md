# Solución Voraz

- [implementacion del algoritmo por solución voraz](../src/ejercicios/lps/lps_voraz.py)
- [Volver a la tabla de contenido](/docs/Readme.md)
## lps_voraz
Este módulo implementa una solución voraz (greedy) para encontrar la subsecuencia palindrómica más larga. Aunque esta aproximación puede ser más rápida en algunos casos, no garantiza encontrar la solución óptima en todos los escenarios, ya que no evalúa todas las posibilidades como lo hacen las soluciones de fuerza bruta o programación dinámica.

### Función Principal:
- **def solve_lps_greedy(lines: list[str]) -> list[str]:** recibe una lista de cadenas **lines** y devuelve una lista de subsecuencias palindrómicas construidas por la heurística, una por cada línea.

### Explicacion del algoritmo:
```
    try:
        n = int(lines[0])
        raws = lines[1 : 1 + n]
    except ValueError:
        raws = lines
```
- Lee un posible encabezado numérico n.

- Si existe, toma las n líneas siguientes como casos; si no, usa todas.

- **Función Auxiliar**
```
    def expand(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # al salir, [left+1:right] es palíndromo
        return s[left + 1 : right]
```
- Función auxiliar expand que, dado un centro (left,right), expande mientras los caracteres a ambos lados coincidan.
- Devuelve la subcadena palindrómica máxima alrededor de ese centro.
```
    out = []
    for raw in raws:
        s = normalize(raw)
        best = ""
```
- Inicializa la lista out.
- Para cada línea raw, normaliza a s y arranca best vacío.
```
        for i in range(len(s)):
            # impar
            p1 = expand(s, i, i)
            if len(p1) > len(best):
                best = p1
            # par
            p2 = expand(s, i, i + 1)
            if len(p2) > len(best):
                best = p2
```
- Recorre cada índice i como posible centro de palíndromo.
    * Palíndromo de longitud impar: llama expand(s, i, i).
    * Palíndromo de longitud par: llama expand(s, i, i+1).
- Si la subcadena obtenida (p1 o p2) es más larga que best, la adopta.
```
        out.append(best)
    return out
```
- Añade la mejor subsecuencia palindrómica encontrada para raw.

- Tras procesar todas, devuelve out.


### Análisis de Complejidad:
- **Tiempo**:
    Sea $n = |s|$ la longitud de la cadena normalizada.

    1. **Recorrer centros**

    * Hay $n$ posibles centros para palíndromos impares y $n$ para pares → O(n) iteraciones.

    2. **Expansión alrededor de un centro**

    * Cada llamada a `expand` avanza dos punteros hasta que dejan de coincidir o se sale de los límites.
    * En el peor caso, recorre toda la cadena → O(n).

    3. **Total por centro**

    * Dos expansiones (impar + par) → $2 \times O(n) = O(n)$.

    4. **Complejidad global**

    $$
        \underbrace{O(n)}_{\substack{\text{centros}}} \times \underbrace{O(n)}_{\substack{\text{expansión}}}
        \;=\;O(n^2)
    $$

- **Espacio**: Solo variables escalares y la salida → **O(1)** adicional (excluyendo la cadena de entrada y la lista de resultados).