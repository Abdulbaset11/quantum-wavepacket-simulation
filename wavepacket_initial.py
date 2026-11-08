import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1000)

x0 = -5.0     
k0 = 5.0      
sigma = 1.0   

psi = np.exp(-((x - x0) ** 2) / (2 * sigma ** 2)) * np.exp(1j * k0 * x)