from ...utils.normalize import normalize


def solve_lps_brute(lines: list[str]) -> list[str]:

    def is_pal(x: str) -> bool:
        return x == x[::-1]

    try:
        n = int(lines[0])
        raws = lines[1 : 1 + n]
    except ValueError:
        raws = lines

    out = []
    for raw in raws:
        s = normalize(raw)
        best = ""
        n = len(s)
        # Genera todos los pares (i,j)
        for i in range(n):
            for j in range(i, n):
                sub = s[i : j + 1]
                if is_pal(sub) and len(sub) > len(best):
                    best = sub
        out.append(best)
    return out
