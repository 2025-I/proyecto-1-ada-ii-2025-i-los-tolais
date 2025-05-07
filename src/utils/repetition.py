"Repetición de pruebas para el algoritmo de la subsecuencia palindrómica más larga (LPS)."

import time
import unittest
from typing import Callable

from .generators import generate_list_test_phrase


class TestRepetition(unittest.TestCase):
    """
    Clase para repetir pruebas de rendimiento y validez de un algoritmo
    que encuentra la subsecuencia palindrómica más larga.
    """

    def setAlgorithm(self, algorithm: Callable[[str], str]):
        """
        Define el algoritmo a probar.
        """
        self._algorithm = algorithm

    def setReference(self, reference: Callable[[str], str]):
        """
        Define el algoritmo de referencia (correcto, aunque no necesariamente eficiente).
        """
        self._reference = reference

    def run_n_repetitions(self, num_tests: int, repetitions: int = 5):
        """
        Ejecuta múltiples repeticiones del conjunto de pruebas y
        calcula el tiempo promedio de ejecución.
        """
        average_time: float = 0

        for _ in range(repetitions):
            list_phrase: list[tuple[str, str]] = generate_list_test_phrase(num_tests)
            start: float = time.time()
            self.run_multiple_tests(num_tests, list_phrase)
            end: float = time.time()
            average_time += end - start

        if repetitions > 1:
            print(
                f"Tiempo promedio de ejecución para tamaño {num_tests}: {average_time / repetitions:.4f} segundos"
            )

    def run_multiple_tests(self, num_tests: int, list_phrase: list[tuple[str, str]]):
        """
        Ejecuta un conjunto de pruebas sobre frases generadas aleatoriamente,
        comparando el resultado con el algoritmo de referencia.
        """
        for i in range(num_tests):
            phrase, _ = list_phrase[i]
            expected = self._reference(phrase)
            result = self._algorithm(phrase)
            self.assertEqual(
                result,
                expected,
                msg=f"Falló en la prueba #{i+1}:\nEsperado: {expected}\nResultado: {result}",
            )

    def run_scaled_test(self, num_elements: int, repetitions: int = 5):
        """
        Ejecuta las pruebas escaladas con una cantidad específica de elementos y repeticiones.
        """
        self.run_n_repetitions(num_tests=num_elements, repetitions=repetitions)
