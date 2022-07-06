import numpy as np
from matplotlib import rc, rcParams
import matplotlib.pyplot as plt

a = 0.1
c = 0.033
I_ext = 0

samples = 10
V_inf, V_sup = -0.25, 1.25
w_inf, w_sup = -0.2, 0.2
V, w = np.meshgrid(np.linspace(V_inf, V_sup, samples), np.linspace(w_inf, w_sup, samples))

V_nul = np.linspace(V_inf, V_sup, 5000)

nulclina_2 = -V_nul**3 + (a+1)*V_nul**2 - a*V_nul + I_ext

v = -V**3 + (a+1)*V**2 - a*V - w + I_ext

## Estilo ploteo
rc("text", usetex=True)
rc("text.latex", preamble=r"\usepackage[sc]{mathpazo}")
rc("font", size=18)
rcParams['figure.figsize'] = 12, 8

for b in [-0.005, 0.0061, 0.0062, 0.1]:
    nulclina_1 = b/c*V_nul
    
    u = b*V - c*w

    plt.xlim(V_inf, V_sup)
    plt.ylim(w_inf, w_sup)
    plt.title(f"$b = {b:.4f}$")
    plt.xlabel("$V$")
    plt.ylabel(r"$\omega$")
    plt.plot(V_nul, nulclina_1, lw=2)
    plt.plot(V_nul, nulclina_2, lw=2)
    plt.streamplot(V, w, u, v, color="grey", linewidth=1)
    plt.grid()

    plt.savefig(f"FHN_plot_b_{b:.3e}.png")
    plt.cla()
