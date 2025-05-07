"Prueba de la solución de fuerza bruta para el problema LPS"
import random
import string
import unittest

from src.ejercicios.lps.lps_brute import solve_lps_brute  
from src.ejercicios.lps.lps_dynamic import solve_lps_dp  


class TestBruteRepetition(unittest.TestCase):
    def generate_input(self, num_elements):
        return [
            "".join(random.choices(string.ascii_letters + string.digits, k=3))
            for _ in range(num_elements)
        ]

    def run_scaled_test(self, num_elements, repetitions=3):
        for rep in range(repetitions):
            data = self.generate_input(num_elements)
            expected = solve_lps_dp(
                data
            )  # Reutilizamos la salida de DP como referencia correcta
            result = solve_lps_brute(data)

            for i, (exp, res) in enumerate(zip(expected, result)):
                self.assertIn(
                    exp,
                    res,
                    msg=f"[Iter {rep+1}] Entrada {i}: Esperado '{exp}' en '{res}'",
                )

    def test_pequeno_brute(self):
        """Prueba con 100 elementos."""
        self.run_scaled_test(num_elements=100)

    def test_mediano_brute(self):
        """Prueba con 1000 elementos."""
        self.run_scaled_test(num_elements=1000, repetitions=3)

    def test_grande_brute(self):
        """Prueba con 10000 elementos."""
        self.run_scaled_test(num_elements=10000, repetitions=2)

    def test_extra_grande_brute(self):
        """Prueba con 50000 elementos (puede tardar)."""
        self.run_scaled_test(num_elements=50000, repetitions=1)
