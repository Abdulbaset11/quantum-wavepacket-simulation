import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-10, 10, 1000)
x0 = -4.0
sigma = 0.5
k0 = 5
psi = np.exp(-(x - x0)**2 / (2 * sigma**2)) * np.exp(1j * k0 * x)
# 1. Calculate the spatial step (dx)
dx = x[1] - x[0]

# 2. Calculate the current total probability (Area under |psi|^2)
total_probability = np.sum(np.abs(psi)**2) * dx

# 3. Normalize psi so that the total probability equals 1
psi = psi / np.sqrt(total_probability)

# Check the normalized probability (should print 1.0)
print("Normalized total probability:", np.sum(np.abs(psi)**2) * dx)
# Create a figure window
plt.figure(figsize=(10, 5))

# Plot Real part, Imaginary part, and Probability density
plt.plot(x, psi.real, label="Real Part (Re[psi])", color="blue", alpha=0.6)
plt.plot(x, psi.imag, label="Imaginary Part (Im[psi])", color="orange", alpha=0.4, linestyle="--")
plt.plot(x, np.abs(psi)**2, label="Probability Density (|psi|^2)", color="black", linewidth=2)

# Graph styling (labels in English)
plt.title("Initial Wave Packet at t = 0", fontsize=14)
plt.xlabel("Position (x)", fontsize=12)
plt.ylabel("Amplitude", fontsize=12)
plt.xlim(-10, 10)
plt.grid(True, alpha=0.3)
plt.legend(loc="upper right")

# Display the window
plt.show()