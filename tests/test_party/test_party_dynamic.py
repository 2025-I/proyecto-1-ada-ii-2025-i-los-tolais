import pytest
import random
from src.ejercicios.party.party_dynamic import solve_party_dp

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

@pytest.mark.parametrize("size,label", [
    (10, "juguete"),
    (100, "pequeño"),
    (1000, "mediano"),
    (10000, "grande"),
    #(50000, "extra_grande"),
])
@pytest.mark.parametrize("repeat", range(1))
def test_party_dp_scaled(size, label, repeat):
    num_problems = 1
    matrix = generate_random_tree_matrix(size)
    values = [random.randint(1, 30) for _ in range(size)]

    lines = [str(num_problems), str(size)]
    lines += format_matrix_as_lines(matrix)
    lines.append(" ".join(map(str, values)))

    outputs = solve_party_dp(lines)
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
