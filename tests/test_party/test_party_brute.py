import random
import time

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
    "num_problems,label",
    [
        (10, "juguete"),
        (100, "pequeño"),
        (1000, "mediano"),
        (10000, "grande"),
        (50000, "extra_grande"),
    ],
)
def test_party_fixed_size_scaled(num_problems, label):
    size = 10 # Tamaño fijo de cada problema
    repeticiones = 5

    # Cálculo del tiempo promedio para cada tamaño
    promedio_tiempos = 0  # Para acumular el tiempo total para este tamaño de problema

    for _ in range(repeticiones):
        rep_avg_time = 0  # Tiempo promedio por repetición
        tiempos_individuales = []  # Lista para almacenar tiempos de cada iteración

        for _ in range(num_problems):
            matrix = generate_random_tree_matrix(size)
            values = [random.randint(1, 30) for _ in range(size)]

            lines = [str(1), str(size)]
            lines += format_matrix_as_lines(matrix)
            lines.append(" ".join(map(str, values)))

            start = time.perf_counter()
            outputs = solve_party_brute(lines)
            end = time.perf_counter()

            time_taken = end - start
            tiempos_individuales.append(
                time_taken
            )  # Almacenamos el tiempo de esta iteración
            rep_avg_time += (
                time_taken  # Acumulamos el tiempo total para esta repetición
            )

            # Verificaciones
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
        # Calcular el tiempo promedio para esta repetición
        promedio_tiempos += rep_avg_time

    # Calcular el promedio general para este tamaño después de todas las repeticiones
    promedio_general = promedio_tiempos / repeticiones
    print(
        f"Tiempo promedio ({label}, {num_problems} matrices {size}x{size}, {repeticiones} repeticiones): {promedio_general:.5f} segundos"
    )
