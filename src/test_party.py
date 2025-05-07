from ejercicios.party.party_brute import solve_party_brute
from ejercicios.party.party_dynamic import solve_party_dp
from ejercicios.party.party_voraz import solve_party_voraz


def leer_archivo(path):
    with open(path, encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


if __name__ == "__main__":
    lines = leer_archivo("prueba.txt")

    print("Fuerza bruta:")
    for r in solve_party_brute(lines):
        print(r)

    print("\nProgramación dinámica:")
    for r in solve_party_dp(lines):
        print(r)

    print("\nVoraz:")
    for r in solve_party_voraz(lines):
        print(r)
