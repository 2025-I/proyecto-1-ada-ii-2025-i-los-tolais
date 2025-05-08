import tkinter as tk
from tkinter import filedialog, messagebox, ttk
#from ejercicios.lps.lps_dynamic import solve_lps_dp
from src.ejercicios.lps.lps_dynamic import solve_lps_dp
from src.ejercicios.party.party_dynamic import solve_party_dp
from src.ejercicios.lps.lps_voraz import solve_lps_greedy
from src.ejercicios.lps.lps_brute import solve_lps_brute
from src.ejercicios.party.party_brute import solve_party_brute
from src.ejercicios.party.party_voraz import solve_party_voraz

def get_algorithm(name):
    """
    Devuelve la función correspondiente según el nombre del algoritmo seleccionado.
    """
    algorithms = {
        "LPS (Programación Dinámica)": solve_lps_dp,
        "LPS (Solución de Fuerza Bruta)": solve_lps_brute,
        "LPS (Solución Voraz)": solve_lps_greedy,
        "Party (Programación Dinámica)": solve_party_dp,
        "Party (Solución de Fuerza Bruta)": solve_party_brute,
        "Party (Solución Voraz)": solve_party_voraz
    }
    return algorithms.get(name, None)


def run_algorithm():
    filepath = file_path_var.get()
    algorithm_name = algo_var.get()

    if not filepath:
        messagebox.showwarning("Archivo no seleccionado", "Por favor selecciona un archivo de entrada.")
        return

    try:
        with open(filepath, encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip()]
    except Exception as e:
        messagebox.showerror("Error de lectura", f"No se pudo leer el archivo:\n{e}")
        return

    algorithm = get_algorithm(algorithm_name)
    if not algorithm:
        messagebox.showwarning("Algoritmo no seleccionado", "Selecciona un algoritmo válido.")
        return

    try:
        result = algorithm(lines)
    except Exception as e:
        messagebox.showerror("Error al procesar", f"Hubo un error ejecutando el algoritmo:\n{e}")
        return

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, "\n".join(result))



def select_file():
    filepath = filedialog.askopenfilename(
        title="Selecciona el archivo de entrada",
        filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
    )
    if filepath:
        file_path_var.set(filepath)


# Crear ventana principal
root = tk.Tk()
root.title("Proyecto ADA II - Procesamiento de Algoritmos")

# Variables
file_path_var = tk.StringVar()
algo_var = tk.StringVar()

# Layout
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky="nsew")

ttk.Label(frame, text="Archivo de entrada:").grid(row=0, column=0, sticky="w")
ttk.Entry(frame, textvariable=file_path_var, width=60).grid(row=0, column=1, padx=5)
ttk.Button(frame, text="Seleccionar...", command=select_file).grid(row=0, column=2)

ttk.Label(frame, text="Algoritmo:").grid(row=1, column=0, sticky="w", pady=10)
algo_menu = ttk.Combobox(frame, textvariable=algo_var, state="readonly", width=40)
algo_menu["values"] = [
    "LPS (Programación Dinámica)",
    "LPS (Solución de Fuerza Bruta)",
    "LPS (Solución Voraz)",
    "Party (Programación Dinámica)",
    "Party (Solución de Fuerza Bruta)",
    "Party (Solución Voraz)"
]
algo_menu.grid(row=1, column=1, columnspan=2, sticky="w")

ttk.Button(frame, text="Ejecutar", command=run_algorithm).grid(row=2, column=0, columnspan=3, pady=10)

output_text = tk.Text(root, height=20, wrap="word")
output_text.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")

# Expandir ventana con el contenido
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

# Iniciar GUI
root.mainloop()
