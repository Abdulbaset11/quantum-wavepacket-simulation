import numpy as np
import matplotlib.pyplot as plt

# Step 1: Spatial Grid Construction
x = np.linspace(-10, 10, 1000)

# Step 2: Wave Packet Definition
# Parameters for the wave packet
x0 = -5.0     # Initial position
k0 = 5.0      # Central wave number
sigma = 1.0   # Width of the wave packet

# Define the wave packet function
psi = np.exp(-((x - x0) ** 2) / (2 * sigma ** 2)) * np.exp(1j * k0 * x)

