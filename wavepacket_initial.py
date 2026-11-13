import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

# Reduced Planck constant (J.s)
hbar = 1.054571817e-34
# Electron mass (kg)
m_e = 9.1093837139e-31
# Parameters
x = np.linspace(0, 20, 1000, endpoint=False)
x00 = 5.0
k0 = 5.0
sigma = 1.0
C = (hbar / (2 * m_e)) * 1000

# Start the timer
start_time = time.perf_counter()

# Calculate the initial time
t = time.perf_counter() - start_time

# Calculate the initial position
x0 = x00 + (0.579) * t


# Wave function
psi = np.exp(-((x - x0) ** 2) / (2 * sigma ** 2)) * np.exp(1j * k0 * x)

# Calculate the delta x
dx = x[1] - x[0]

# Calculate total area under probability density
total_area = np.sum(np.abs(psi)**2) * dx

# Parameter A
a = 1/np.sqrt(total_area)

# Normalize Psi
psi_norm = psi * a

# Calculate wave numbers
k = 2 * np.pi * np.fft.fftfreq(len(x), d=dx)

# Fourier transform of the initial wave function
psi_k_initial = np.fft.fft(psi_norm)

# Calculate probability density
proablity = np.abs(psi_norm)**2

# Create the initial plot
line, = plt.plot(x, proablity)


# Update the wave packet with time
def update(frame):

    # Calculate simulation time in femtoseconds
    t = min(time.perf_counter() - start_time, 15.0)

    # Time evolution from Schrodinger equation
    psi_k_t = psi_k_initial * np.exp(-1j * C * k**2 * t)

    # Convert back to position space
    psi_t = np.fft.ifft(psi_k_t)

    # Calculate probability density
    proablity = np.abs(psi_t)**2

    # Update the plot
    line.set_ydata(proablity)



# Animate the probability density
animation = FuncAnimation(
    plt.gcf(), update, interval=20
)

# Show the animation
plt.show()
