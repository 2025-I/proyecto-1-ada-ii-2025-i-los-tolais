"Prueba de la solución voraz para el problema LPS."
from src.ejercicios.lps.lps_dynamic import solve_lps_dp
from src.ejercicios.lps.lps_voraz import solve_lps_greedy
from tests.test_repetition import TestRepetition


class TestGreedyRepetition(TestRepetition):
    def setUp(self):
        self.setAlgorithm(lambda s: solve_lps_greedy([s])[0])
        self.setReference(lambda s: solve_lps_dp([s])[0])

    def test_juguete_voraz(self):
        """Prueba con 10 elementos (casos de juguete)."""
        self.run_scaled_test(num_elements=10)

    def test_pequeno_voraz(self):
        """Prueba con 100 elementos."""
        self.run_scaled_test(num_elements=100)

    def test_mediano_voraz(self):
        """Prueba con 1000 elementos."""
        self.run_scaled_test(num_elements=1000, repetitions=3)

    def test_grande_voraz(self):
        """Prueba con 10000 elementos."""
        self.run_scaled_test(num_elements=10000, repetitions=2)

    def test_extra_grande_voraz(self):
        """Prueba con 50000 elementos"""
        self.run_scaled_test(num_elements=50000, repetitions=1)
