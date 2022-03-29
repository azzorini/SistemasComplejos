import numpy as np
from matplotlib import rc, rcParams
import matplotlib.pyplot as plt

# Función que recibe una función f [f(a_n) = a_{n+1}] y un valor inicial
# y devulve un array para las x y otro array para las y de todos los puntos del cobweb
# acepta opcionalmente el número de iteraciones a realizar (por defecto hace 100)
def cobweb_arrays(f, a0, n_iter = 100):
    x, y = np.zeros(n_iter*2 + 1), np.zeros(n_iter*2 + 1)
    x[0], y[0] = a0, 0

    for i in range(n_iter):
        value = f(x[2*i])
        x[2*i+1], y[2*i+1] = x[2*i], value
        x[2*i+2], y[2*i+2] = value, value

    return [x, y]

# Función que recibe una función f [f(a_n) = a_{n+1}], un valor inicial a0
# y opcionalmente el número de iteraciones a realizar, el sampleo del array por defecto que se toma
# que va de 0 a 1.2*a0 y/o el array que se va a usar para mostrar la función
def cobweb_plot(f, a0, n_iter = 100, n_samples = 5000, x = None):
    if type(x).__name__ == "NoneType":
        x = np.linspace(0, 1.2*a0, n_samples)

    cobweb_x, cobweb_y = cobweb_arrays(f, a0, n_iter)

    # Estilo ploteo
    rc("text", usetex=True)
    rc("text.latex", preamble=r"\usepackage[sc]{mathpazo}")
    rc("font", size=18)
    rcParams["figure.figsize"] = 12, 12

    # Plot
    fig, ax = plt.subplots()
    ax.set_xlabel("$a_n$")
    ax.set_ylabel(r"$f\left(a_n\right)$")
    ax.plot(x, x, "#00008b", linewidth=2, linestyle="--")
    ax.plot(x, [f(v) for v in x], "#000000", linewidth=2)
    ax.plot(cobweb_x, cobweb_y, "#8b0000", linewidth=1)

    plt.savefig("cobweb.png", dpi=200)

# Función principal
def main():
    # Definimos la función f(a_n) = a_{n+1} que queremos usar
    def f(an):
        if 0 <= an <= .5:
            return 2*an
        else:
            return 2*an - 1

    a0 = np.pi/4 # Fijamos la condición inicial
    cobweb_plot(f, a0, x = np.linspace(0., 1., 5000))

if __name__ == "__main__":
    main()
