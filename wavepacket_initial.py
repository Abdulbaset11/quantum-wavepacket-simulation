import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

#Parameters
x = np.linspace(0,20,1000)
dx = x[1] - x[0]
x_0 = 5.0
sigma = 1.0
k_0 = 5.0


psi = np.exp(-(x-x_0)**2 / (2*sigma**2)) * np.exp(1j * k_0 * x)

Total_Area = np.sum(np.abs(psi)**2) * dx
a = 1/np.sqrt(Total_Area)

psi_norm = a * psi
Probabilty = np.abs(psi_norm)**2


plt.plot(x, Probabilty)
plt.show()