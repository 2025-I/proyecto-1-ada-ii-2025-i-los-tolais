import pytest
from ejercicios.lps.lps_dynamic import solve_lps_dp

# Casos de prueba robustos

def test_single_characters():
    # Caso con una sola letra: la subcadena palíndroma más larga será la letra misma
    lines = ["3", "a", "b", "c"]
    expected = ["a", "b", "c"]
    result = solve_lps_dp(lines)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_palindrome_at_the_end():
    # Caso donde el palíndromo está al final
    lines = ["1", "abccba"]
    expected = ["abccba"]
    result = solve_lps_dp(lines)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_palindrome_in_the_middle():
    # Caso donde el palíndromo está en el medio de la cadena
    lines = ["1", "xabccba"]
    expected = ["abccba"]
    result = solve_lps_dp(lines)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_large_input():
    # Caso con una cadena grande
    lines = ["1", "a" * 1000 + "b" + "a" * 1000]  # 'a'... 'b' ... 'a' es el palíndromo más largo
    expected = ["a" * 1000 + "b" + "a" * 1000]
    result = solve_lps_dp(lines)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_large_palindrome():
    # Caso con una cadena palindrómica de tamaño muy grande
    lines = ["1", "a" * 50000]  # Toda la cadena es un palíndromo
    expected = ["a" * 50000]
    result = solve_lps_dp(lines)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_non_alphabetical_characters():
    # Caso con caracteres no alfabéticos
    lines = ["1", "abc123cba"]
    expected = ["abc123cba"]
    result = solve_lps_dp(lines)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_case_with_spaces():
    # Caso con espacios dentro de la cadena
    lines = ["1", "a b c b a"]
    expected = ["a b c b a"]
    result = solve_lps_dp(lines)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_case_with_special_characters():
    # Caso con caracteres especiales
    lines = ["1", "a!b@c#c@b!a"]
    expected = ["a!b@c#c@b!a"]
    result = solve_lps_dp(lines)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_multiple_palindromes():
    # Caso con múltiples palíndromos
    lines = ["1", "abcdcbba"]
    expected = ["cbcdc"]  # 'cbcdc' es el palíndromo más largo
    result = solve_lps_dp(lines)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_empty_input():
    # Caso con una entrada vacía
    lines = ["1", ""]
    expected = [""]
    result = solve_lps_dp(lines)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_case_with_mixed_case_and_normalization():
    # Caso con mezcla de mayúsculas y minúsculas y normalización
    lines = ["1", "MaDam"]
    expected = ["madam"]  # Después de la normalización 'MaDam' debe ser 'madam'
    result = solve_lps_dp(lines)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_multiple_empty_lines():
    # Caso con varias cadenas vacías
    lines = ["3", "", "", ""]
    expected = ["", "", ""]
    result = solve_lps_dp(lines)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_longest_palindrome_at_start():
    # Caso con el palíndromo más largo al principio
    lines = ["1", "abccba123abccba"]
    expected = ["abccba123abccba"]
    result = solve_lps_dp(lines)
    assert result == expected, f"Expected {expected}, but got {result}"

if __name__ == "__main__":
    pytest.main()
