import time

from src.ejercicios.lps.lps_brute import solve_lps_brute
from src.ejercicios.lps.lps_dynamic import solve_lps_dp
from src.utils.generators import generate_list_test_phrase
from src.utils.repetition import TestRepetition


class TestBruteRepetition(TestRepetition):
    def setUp(self):
        # Establece el algoritmo de prueba como fuerza bruta
        self.setAlgorithm(lambda s: solve_lps_brute([s])[0])

    def run_scaled_test(self, num_elements: int, repetitions: int = 5):
        """
        Ejecuta pruebas escaladas para una cantidad dada de elementos
        y repite varias veces para calcular el tiempo promedio.
        """
        total_time = 0.0

        for rep in range(repetitions):
            list_test_data = generate_list_test_phrase(num_elements)
            inputs = [phrase for phrase, _ in list_test_data]
            expected_outputs = solve_lps_dp(inputs)  # Se toma como referencia

            start = time.time()
            results = solve_lps_brute(inputs)
            end = time.time()

            total_time += end - start

            for i, (res, exp) in enumerate(zip(results, expected_outputs)):
                self.assertIn(
                    exp,
                    res,
                    msg=f"[Iter {rep + 1}] Entrada {i}: Esperado '{exp}' en '{res}'",
                )

        average_time = total_time / repetitions
        print(
            f"Tiempo promedio de ejecución para tamaño {num_elements}: {average_time:.4f} segundos"
        )

    def test_pequeno_brute(self):
        """Prueba con 100 elementos."""
        self.run_scaled_test(num_elements=100, repetitions=5)

    def test_juguete_brute(self):
        """Prueba básica con 10 elementos."""
        self.run_scaled_test(num_elements=10, repetitions=5)

    def test_mediano_brute(self):
        """Prueba con 1000 elementos."""
        self.run_scaled_test(num_elements=1000, repetitions=5)

    def test_grande_brute(self):
        """Prueba con 10000 elementos."""
        self.run_scaled_test(num_elements=10000, repetitions=5)

    def test_extra_grande_brute(self):
        """Prueba con 50000 elementos (puede tardar)."""
        self.run_scaled_test(num_elements=50000, repetitions=5)
