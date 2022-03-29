import numpy as np
import matplotlib.pyplot as plt

samples = 10
x, y = np.meshgrid(np.linspace(-5, 5, samples), np.linspace(-5, 5, samples))

u = -y/np.sqrt(x**2 + y**2)
v = x/np.sqrt(x**2 + y**2)

plt.streamplot(x, y, u, v, minlength = 1.0)
#plt.quiver(x, y, u, v)

plt.show()
