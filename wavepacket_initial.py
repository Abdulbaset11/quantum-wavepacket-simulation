
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time


# Parameters
x = np.linspace(0, 20, 1000)
x00 = 5.0
k0 = 5.0
sigma = 1.0

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

# Calculate probability density
proablity = np.abs(psi_norm)**2

# Create the initial plot
line, = plt.plot(x, proablity)


# Update the wave packet with time
def update(frame):

    # Calculate the new time
    t = time.perf_counter() - start_time

    # Calculate the new position
    x0 = x00 + (0.579) * t

    # Calculate the new wave function
    psi = np.exp(-((x - x0) ** 2) / (2 * sigma ** 2)) * np.exp(1j * k0 * x)

    # Normalize the new wave function
    psi_norm = psi * a

    # Calculate the new probability density
    proablity = np.abs(psi_norm)**2

    # Update the existing plot
    line.set_ydata(proablity)


# Animate the probability density
animation = FuncAnimation(
    plt.gcf(), update, interval=20
)

# Show the animation
plt.show()
