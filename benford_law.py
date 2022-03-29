import numpy as np
from matplotlib import rc, rcParams
import matplotlib.pyplot as plt

MAX_INTEGER = 1000000000

# Guarda en las primeras posiciones de array las primeras cifras de los números que se generen
def get_primeras_cifras(array, n_aleatorios = 10000, n_iteraciones = 100):
    for i in range(n_aleatorios):
        n = np.random.randint(MAX_INTEGER)
        for j in range(n_iteraciones):
            array[i*n_iteraciones + j] = int(str(n)[0]) # Guardamos la primera cifra del número

            # Modificamos aleatoriamente el número
            if np.random.choice([True, False]):
                n /= 2
            else:
                n *= 2

# Plotea un histograma usando los datos de array y lo guarda en filename
# devuelve un array con las frecuencias de aparición de cada cifra
def plot_primeras_cifras(array, filename="benford.pdf"):
    ## Estilo ploteo
    rc("text", usetex=True)
    rc("text.latex", preamble=r"\usepackage[sc]{mathpazo}")
    rc("font", size=18)
    rcParams['figure.figsize'] = 12, 8

    plt.xlabel(r"\textnormal{Primera cifra}")
    plt.ylabel(r"\textnormal{Número apariciones}")
    plt.xticks([i+1 for i in range(9)])

    n, bins, patches = plt.hist(array, bins=[0.5 + i for i in range(10)], color="#add8e6", edgecolor="black", linewidth=1)

    plt.savefig(filename, dpi=200)

    return n

def main():
    datafile = "benford.txt" # Fichero donde guardaremos los datos finales

    N_aleatorios = 10000 # Número de aleatorios a generar
    seed = 28021999 # Semilla para los números aleatorios
    np.random.seed(seed)

    N_iteraciones = 100 # Número de iteraciones para cada aleatorio

    primeras_cifras = np.zeros(N_iteraciones*N_aleatorios) # Array con el tamaño necesario para guardarlo todo

    get_primeras_cifras(primeras_cifras, N_aleatorios, N_iteraciones)

    n = plot_primeras_cifras(primeras_cifras)
    C_norm = sum(n)

    with open(datafile, "w") as f:
        for i in range(len(n)):
            f.write(f"{i+1}\t{n[i]/C_norm}\n")

if __name__ == "__main__":
    main()
