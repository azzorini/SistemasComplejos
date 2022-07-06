import numpy as np
from matplotlib import rc, rcParams
import matplotlib.pyplot as plt

N_TRAYECTORIAS = 6
CONDICIONES_INI = [(-0.1, -0.1), (-0.1, 0.1), (0.4, -0.1), (0.4, 0.15), (1, -0.1), (1, 0.15)]

a = 0.1
b = -0.005
c = 0.033
I_ext = 0

def V_dot(V, w):
    return V*(a-V)*(V-1) - w + I_ext

def w_dot(V, w):
    return b*V - c*w

t_max, N_PASOS = 200, 100000
t = np.linspace(0, t_max, N_PASOS)
dt = t_max/N_PASOS

trayectorias = [np.full((2,N_PASOS), 0.0) for _ in range(N_TRAYECTORIAS)]

for nt in range(len(trayectorias)):
    trayectorias[nt][0][0], trayectorias[nt][1][0] = CONDICIONES_INI[nt]

for i in range(1, N_PASOS):
    for nt in range(len(trayectorias)):
        ult_V, ult_w = trayectorias[nt][0][i-1], trayectorias[nt][1][i-1]
        trayectorias[nt][0][i] = ult_V + V_dot(ult_V, ult_w)*dt
        trayectorias[nt][1][i] = ult_w + w_dot(ult_V, ult_w)*dt

## Estilo ploteo
rc("text", usetex=True)
rc("text.latex", preamble=r"\usepackage[sc]{mathpazo}")
rc("font", size=18)
rcParams['figure.figsize'] = 12, 8

for nt in range(len(trayectorias)):
    plt.plot(trayectorias[nt][0], trayectorias[nt][1], lw=2)

plt.grid()
plt.title(f"$b = {b:.4f}$")
plt.xlabel("$V$")
plt.ylabel(r"$\omega$")
plt.savefig(f"FHN_trayectorias_b_{b:.3e}.png")
plt.cla()

for nt in range(len(trayectorias)):
    plt.plot(t, trayectorias[nt][0], lw=2)

plt.grid()
plt.title(f"$b = {b:.4f}$")
plt.xlabel("$t$")
plt.ylabel("$V$")
plt.savefig(f"FHN_V_t_b_{b:.3e}.png")

#with open(f"FHN_trayectorias_b_{b:.3e}.txt", "w") as f:
#    for i in range(len(t)):
#        f.write(f"{t[i]}")
#        for nt in range(len(trayectorias)):
#            f.write(f"\t{trayectorias[nt][0][i]}\t{trayectorias[nt][1][i]}")
#        f.write("\n")
