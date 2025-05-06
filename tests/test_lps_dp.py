import pytest
from ejercicios.lps.lps_dynamic import solve_lps_dp

# Casos de prueba más sencillos

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

def test_small_palindrome():
    # Caso con un palíndromo pequeño
    lines = ["1", "racecar"]
    expected = ["racecar"]
    result = solve_lps_dp(lines)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_case_with_spaces():
    lines = ["1", "a b c b a"]
    expected = ["abcba"]
    result = solve_lps_dp(lines)
    assert result == expected

def test_case_with_special_characters():
    lines = ["1", "a!b@c#c@b!a"]
    expected = ["abccba"]
    result = solve_lps_dp(lines)
    assert result == expected

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

if __name__ == "__main__":
    pytest.main()
