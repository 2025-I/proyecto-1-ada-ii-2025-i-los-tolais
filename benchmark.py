import time
import random
import string
import numpy as np
import matplotlib.pyplot as plt

from src.ejercicios.lps.lps_brute    import solve_lps_brute
from src.ejercicios.lps.lps_dynamic       import solve_lps_dp
from src.ejercicios.lps.lps_voraz   import solve_lps_greedy

def random_string(n):
    return ''.join(random.choices(string.ascii_lowercase, k=n))

def measure(fn, lines, reps=5):
    times = []
    for _ in range(reps):
        start = time.perf_counter_ns()          # nanosegundos, alta resolución :contentReference[oaicite:4]{index=4}⁠
        fn(lines)
        times.append(time.perf_counter_ns() - start)
    return sum(times) / len(times)

SIZES = [10, 50, 100, 200]
data = {'brute':[], 'dp':[], 'greedy':[]}

for n in SIZES:
    lines = [random_string(n)]
    data['brute'].append((n, measure(solve_lps_brute, lines)))
    data['dp'].append(   (n, measure(solve_lps_dp,    lines)))
    data['greedy'].append((n, measure(solve_lps_greedy,lines)))

n_b, t_b = zip(*data['brute'])
n_d, t_d = zip(*data['dp'])
n_g, t_g = zip(*data['greedy'])

# Lineal
plt.figure()
plt.plot(n_b, t_b, 'o-', label='Brute O(n³)')
plt.plot(n_d, t_d, 's-', label='DP O(n²)')
plt.plot(n_g, t_g, '^-', label='Greedy O(n²)')
plt.xlabel('n (longitud de cadena)')
plt.ylabel('Tiempo medio (ns)')
plt.legend()
plt.grid(True)
plt.savefig('complexity_linear.png', dpi=150)

# Log‑Log
plt.figure()
plt.loglog(n_b, t_b, 'o-', label='Brute')      # default base 10 :contentReference[oaicite:5]{index=5}⁠
plt.loglog(n_d, t_d, 's-', label='DP')
plt.loglog(n_g, t_g, '^-', label='Greedy')
# curvas de referencia
n = np.array(SIZES)
plt.loglog(n, t_d[0]*(n/n[0])**2, '--', label=r'$O(n^2)$ ref')  # pendiente ≈2 :contentReference[oaicite:6]{index=6}⁠
plt.loglog(n, t_b[0]*(n/n[0])**3, '--', label=r'$O(n^3)$ ref')  # pendiente ≈3
plt.xlabel('n (log escala)')
plt.ylabel('Tiempo (log escala)')
plt.legend()
plt.grid(True, which="both", ls="--")
plt.savefig('complexity_loglog.png', dpi=150)
plt.show()
