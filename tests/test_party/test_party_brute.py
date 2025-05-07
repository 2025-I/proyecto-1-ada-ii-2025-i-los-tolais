import random

import pytest

from src.ejercicios.party.party_brute import solve_party_brute


def generate_random_tree_matrix(m):
    matrix = [[0] * m for _ in range(m)]
    nodes = list(range(m))
    random.shuffle(nodes)
    for i in range(1, m):
        parent = random.randint(0, i - 1)
        matrix[nodes[parent]][nodes[i]] = 1
    return matrix


def format_matrix_as_lines(matrix):
    return [" ".join(map(str, row)) for row in matrix]


@pytest.mark.parametrize(
    "size,label",
    [
        (10, "juguete"),
        (15, "pequeño"),
        (20, "mediano"),
    ],
)
@pytest.mark.parametrize("repeat", range(1))
def test_party_brute_scaled(size, label, repeat):
    num_problems = 1
    matrix = generate_random_tree_matrix(size)
    values = [random.randint(1, 30) for _ in range(size)]

    lines = [str(num_problems), str(size)]
    lines += format_matrix_as_lines(matrix)
    lines.append(" ".join(map(str, values)))

    outputs = solve_party_brute(lines)
    assert len(outputs) == 1

    parts = list(map(int, outputs[0].split()))
    assert len(parts) == size + 1
    invited = parts[:-1]
    total = parts[-1]

    for parent in range(size):
        for child in range(size):
            if matrix[parent][child] == 1:
                assert not (invited[parent] == 1 and invited[child] == 1)

    expected_total = sum(values[i] for i in range(size) if invited[i] == 1)
    assert total == expected_total
