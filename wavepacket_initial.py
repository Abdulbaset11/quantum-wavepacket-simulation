import numpy as np
import matplotlib.pyplot as plt
import time

# Parametrs of the wave function
x = np.linspace(0, 20, 1000)
x00 = 5.0
start_time = time.perf_counter()
t = time.perf_counter() - start_time
x0 = x00 + (0.579) * t
k0 = 5.0
sigma = 1.0

# Wave function
psi = np.exp(-((x - x0) ** 2) / (2 * sigma ** 2)) * np.exp(1j * k0 * x)

# Calculate the delta x
dx = x[1] - x[0]

# Calculate total area under wave funcation
total_area = np.sum(np.abs(psi)**2) * dx

# Parameter A
a = 1/np.sqrt(total_area)

# Normalize Psi
psi_norm = psi * a

# Calculate probabilty
proablity = np.abs(psi_norm)**2








# Ploting Probablity of electron at t = 0
plt.plot(x, proablity)
plt.show()