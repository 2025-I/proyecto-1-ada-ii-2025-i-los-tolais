import matplotlib.pyplot as plt
import numpy as np

# Rango de tamaños de entrada
n = np.linspace(1, 100, 100)

# Complejidades teóricas
greedy_theoretical = n**2
dp_theoretical = 2*n
brute_theoretical = 0.3*n*(2**n)

# Complejidades experimentales
greedy_experimental = n**3
dp_experimental = n
brute_experimental = 2**n

# Crear gráfico
plt.figure(figsize=(12, 8))

# Teóricas (líneas punteadas)
plt.plot(n, greedy_theoretical, 'g--', label='Greedy Teórica O(n²)')
plt.plot(n, dp_theoretical, 'b--', label='Dinámica Teórica O(n)')
plt.plot(n, brute_theoretical, 'r--', label='Fuerza Bruta Teórica O(2^n)')

# Experimentales (líneas continuas)
plt.plot(n, greedy_experimental, 'g-', label='Greedy Experimental O(n³)')
plt.plot(n, dp_experimental, 'b-', label='Dinámica Experimental O(n)')
plt.plot(n, brute_experimental, 'r-', label='Fuerza Bruta Experimental O(2^n)')

# Personalización
plt.title('Comparación de Complejidad Teórica vs Experimental')
plt.xlabel('Tamaño de entrada (n)')
plt.ylabel('Tiempo / Operaciones (O)')
plt.legend()
plt.grid(True)
plt.ylim(0, 100)
plt.xlim(0, 100)

plt.show()
