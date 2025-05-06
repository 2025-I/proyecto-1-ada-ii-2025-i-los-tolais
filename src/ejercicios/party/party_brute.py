def solve_party_brute(lines):
    index = 1
    results = []
    num_problems = int(lines[0])

    for _ in range(num_problems):
        m = int(lines[index])
        matrix = [list(map(int, lines[index + i + 1].split())) for i in range(m)]
        values = list(map(int, lines[index + m + 1].split()))
        index += m + 2

        tree = build_tree(matrix)
        invited, total = brute_force(tree, values)
        result_line = " ".join(str(i) for i in invited) + f" {total}"
        results.append(result_line)

    return results


def build_tree(matrix):
    tree = {}
    n = len(matrix)
    for i in range(n):
        tree[i] = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                tree[i].append(j)
    return tree


def brute_force(tree, values):
    from itertools import product

    n = len(values)
    max_total = 0
    best_combo = [0] * n

    for combo in product([0, 1], repeat=n):
        valid = True
        for parent in range(n):
            if combo[parent] == 1:
                for child in tree[parent]:
                    if combo[child] == 1:
                        valid = False
                        break
            if not valid:
                break
        if valid:
            total = sum(values[i] for i in range(n) if combo[i] == 1)
            if total > max_total:
                max_total = total
                best_combo = list(combo)

    return best_combo, max_total
