import numpy as np
import matplotlib.pyplot as plt

# Parametrs of the wave function
x = np.linspace(-10, 10, 1000)
x0 = -5.0
k0 = 5.0
sigma = 1.0

# Wave function
psi = np.exp(-((x - x0) ** 2) / 2 * sigma ** 2) * np.exp(1j * k0 * x)


plt.plot(x, np.real(psi))
plt.show()