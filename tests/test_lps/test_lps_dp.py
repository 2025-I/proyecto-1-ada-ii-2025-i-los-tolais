"Prueba de la solución de programación dinámica para el problema de la subsecuencia palindromica más larga (LPS)."

from src.ejercicios.lps.lps_dynamic import solve_lps_dp
from src.utils.generators import generate_list_test_phrase
from src.utils.repetition import TestRepetition


class TestDPRepetition(TestRepetition):
    def setUp(self):
        # solve_lps_dp espera una lista y devuelve una lista, pero para usar TestRepetition
        # con entradas individuales, adaptamos para que devuelva solo el primer resultado.
        self.setAlgorithm(lambda s: solve_lps_dp([s])[0])

    def run_scaled_test(self, num_elements: int, repetitions: int = 5):
        for rep in range(repetitions):
            list_test_data = generate_list_test_phrase(num_elements)
            inputs = [phrase for phrase, _ in list_test_data]
            expected_outputs = [expected for _, expected in list_test_data]
            results = solve_lps_dp(inputs)

            for i, (res, exp) in enumerate(zip(results, expected_outputs)):
                self.assertIn(
                    exp,
                    res,
                    msg=f"[Iter {rep+1}] Entrada {i}: Esperado '{exp}' en '{res}'",
                )

    def test_juguete_dynamic(self):
        """Prueba básica de 10 elementos (verificación de correctitud)."""
        self.run_scaled_test(num_elements=10)

    def test_pequeno_dynamic(self):
        """Prueba con 100 elementos."""
        self.run_scaled_test(num_elements=100)

    def test_mediano_dynamic(self):
        """Prueba con 1000 elementos."""
        self.run_scaled_test(num_elements=1000, repetitions=3)

    def test_grande_dynamic(self):
        """Prueba con 10000 elementos."""
        self.run_scaled_test(num_elements=10000, repetitions=2)

    def test_extra_grande_dynamic(self):
        """Prueba con 50000 elementos (puede tardar)."""
        self.run_scaled_test(num_elements=50000, repetitions=1)
