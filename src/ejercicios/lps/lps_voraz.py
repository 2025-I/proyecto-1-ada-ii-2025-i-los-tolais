"Solucion de Voraz para el problema de la subsecuencia palindromica más larga (LPS)."
from ...utils.normalize import normalize

def solve_lps_greedy(lines: list[str]) -> list[str]:
    """
    Centro-expand: O(n^2), O(1) espacio. Rápido en la práctica.
    """
    try:
        n = int(lines[0])
        raws = lines[1 : 1 + n]
    except ValueError:
        raws = lines

    def expand(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # al salir, [left+1:right] es palíndromo
        return s[left + 1 : right]

    out = []
    for raw in raws:
        s = normalize(raw)
        best = ""
        for i in range(len(s)):
            # impar
            p1 = expand(s, i, i)
            if len(p1) > len(best):
                best = p1
            # par
            p2 = expand(s, i, i + 1)
            if len(p2) > len(best):
                best = p2
        out.append(best)
    return out
