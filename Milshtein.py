#!/usr/bin/python

import random as rd
import numpy as np
from datetime import datetime
from matplotlib import rc, rcParams
import matplotlib.pyplot as plt

SEED = 1234

def q_I(rho, landa, mu):
    return landa*rho**2*(1-rho) - mu*rho

def g_I(rho, landa, mu, N):
    return np.sqrt((landa*rho**2*(1-rho)+mu*rho)/N)

def g_I_prime(rho, landa, mu, N):
    return (2*landa*rho - 3*landa*rho**2 + mu)/N/2/g_I(rho, landa, mu, N)

def main():
    rho_0, t_0 = 0.1, .0
    landa, mu = 10.0, 1.0
    N = 1000

    N_pasos = 10000
    h = 1e-3
    sqrt_h = np.sqrt(h)

    arr_rho, arr_t = np.zeros(N_pasos), np.zeros(N_pasos)

    rho, t = rho_0, t_0
    for i in range(N_pasos):
        u_i = rd.gauss(0, 1)
        t += h
        rho += h*q_I(rho, landa, mu) + g_I(rho, landa, mu, N)*sqrt_h*u_i + 0.5*g_I(rho, landa, mu, N)*g_I_prime(rho, landa, mu, N)*h*u_i**2

        arr_t[i], arr_rho[i] = t, rho

    ## Estilo ploteo
    rc("text", usetex=True)
    rc("text.latex", preamble=r"\usepackage[sc]{mathpazo}")
    rc("font", size=18)
    rcParams['figure.figsize'] = 12, 8

    plt.xlim(t_0, t_0 + N_pasos*h)
    plt.ylim(0, 1)

    plt.title(f"$\\lambda = {landa:.2f},\\ \\mu = {mu:.2f}$")
    plt.xlabel("$t$")
    plt.ylabel(r"$\rho$")

    plt.plot(arr_t, arr_rho, lw=2)

    plt.savefig(f"Milshteinv2_{landa:.2f}_{rho_0:.2f}.png")

if __name__ == "__main__":
    rd.seed(SEED)
    main()
