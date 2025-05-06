from faker import Faker
from src.ejercicios.lps.utils import normalize
import random

fake = Faker()

def generate_random_palindrome(min_len: int = 20, max_len: int = 25) -> str:
    """
    Genera un palíndromo aleatorio con una longitud mínima y máxima especificadas.
    """
    half_palindrome_length = random.randint(min_len, max_len) // 2
    half_palindrome = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=half_palindrome_length))
    
    is_even = random.choice([True, False])
    if is_even:
        return half_palindrome + half_palindrome[::-1]  # Palíndromo par
    else:
        return half_palindrome + random.choice('abcdefghijklmnopqrstuvwxyz') + half_palindrome[::-1]  # Palíndromo impar


def generate_test_phrase() -> tuple[str, str]:
    """
    Genera una frase con un palíndromo insertado en una posición aleatoria.
    """
    palindrome = generate_random_palindrome()
    max_phrase_len = random.randint(50, 60)
    
    base_text = fake.text(max_nb_chars=max_phrase_len * 2)[:max_phrase_len - len(palindrome)]

    normalized_text = normalize(base_text)
    insert_position = random.randint(0, len(base_text))
    phrase = normalized_text[:insert_position] + palindrome + normalized_text[insert_position:]
    
    return phrase, palindrome


def generate_list_test_phrase(length: int) -> list[tuple[str, str]]:
    """
    Genera una lista de frases de prueba con palíndromos.
    """
    return [generate_test_phrase() for _ in range(length)]
