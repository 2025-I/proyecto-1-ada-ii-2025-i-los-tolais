def solve_party_voraz(lines):
    index = 1
    results = []
    num_problems = int(lines[0])

    for _ in range(num_problems):
        m = int(lines[index])
        matrix = [list(map(int, lines[index + i + 1].split())) for i in range(m)]
        values = list(map(int, lines[index + m + 1].split()))
        index += m + 2

        tree = build_tree(matrix)
        invited, total = voraz(tree, values)
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


def voraz(tree, values):
    n = len(values)
    score = [(values[i], i) for i in range(n)]
    score.sort(reverse=True)
    invited = [0] * n
    banned = set()

    for val, i in score:
        if i not in banned:
            invited[i] = 1
            banned.update(tree[i])
            for parent in tree:
                if i in tree[parent]:
                    banned.add(parent)

    total = sum(values[i] for i in range(n) if invited[i])
    return invited, total
