import time

from src.ejercicios.lps.lps_dynamic import solve_lps_dp
from src.ejercicios.lps.lps_voraz import solve_lps_greedy
from src.utils.generators import generate_list_test_phrase
from src.utils.repetition import TestRepetition


class TestGreedyRepetition(TestRepetition):
    def setUp(self):
        self.setAlgorithm(lambda s: solve_lps_greedy([s])[0])
        self.setReference(lambda s: solve_lps_dp([s])[0])

    def run_scaled_test(self, num_elements: int, repetitions: int = 5):
        total_time = 0.0

        for rep in range(repetitions):
            list_test_data = generate_list_test_phrase(num_elements)
            inputs = [phrase for phrase, _ in list_test_data]
            expected_outputs = [self._reference(phrase) for phrase in inputs]

            start_time = time.time()
            actual_outputs = [self._algorithm(phrase) for phrase in inputs]
            elapsed_time = time.time() - start_time

            for actual, expected in zip(actual_outputs, expected_outputs):
                self.assertEqual(actual, expected)

            total_time += elapsed_time

        average_time = total_time / repetitions
        print(
            f"\nTiempo promedio ({num_elements} elementos, voraz): {average_time:.5f} segundos"
        )

    def test_juguete_voraz(self):
        """Prueba con 10 elementos (casos de juguete)."""
        self.run_scaled_test(num_elements=10, repetitions=5)

    def test_pequeno_voraz(self):
        """Prueba con 100 elementos."""
        self.run_scaled_test(num_elements=100, repetitions=5)

    def test_mediano_voraz(self):
        """Prueba con 1000 elementos."""
        self.run_scaled_test(num_elements=1000, repetitions=5)

    def test_grande_voraz(self):
        """Prueba con 10000 elementos."""
        self.run_scaled_test(num_elements=10000, repetitions=5)

    def test_extra_grande_voraz(self):
        """Prueba con 50000 elementos."""
        self.run_scaled_test(num_elements=50000, repetitions=5)
