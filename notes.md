# Research Notes & Implementation Log

## Step 1: Spatial Grid Construction & Discretization (The Computational Stage)

### 1. Conceptual Objective
Before propagating or solving any differential wave equation, we must establish the physical space—the "computational stage"—where quantum events will unfold. 

Analytically, continuous space contains an infinite number of spatial coordinates. However, digital processors operate on discrete numerical structures. Therefore, we discretize a continuous one-dimensional number line into a finite lattice of sample points.

---

### 2. Domain Boundaries
We define a bounded domain spanning a total spatial width of $L = 20$ units:
* **Lower Bound ($x_{\min}$):** $-10$
* **Upper Bound ($x_{\max}$):** $+10$

$$\text{Domain Length: } L = x_{\max} - x_{\min} = 10 - (-10) = 20$$

This domain size provides adequate space on both sides of the wave packet, preventing premature boundary collision or unwanted boundary reflection effects during early propagation.

---

### 3. Discretization Trade-off (Grid Resolution $\Delta x$)
To represent the continuous function $\psi(x)$ numerically, the 20-unit domain is divided into $N$ discrete nodes separated by a constant spatial step size:

$$\Delta x = \frac{x_{\max} - x_{\min}}{N - 1}$$

**Initial Choice:** We set $N = 1000$ points ($\Delta x \approx 0.02$). This ensures smooth spatial derivatives while maintaining lightweight, real-time performance.

## Step 2: Initial Wave Packet Formulation ($\psi(x, 0)$)

### 1. Physical Parameters
* **$x_0 = -5.0$ (Center Position):** Sets the initial expected position $\langle x \rangle$ on the left side of the domain.
* **$\sigma = 1.0$ (Spatial Width):** Controls spatial uncertainty ($\Delta x$); determines how localized or spread out the particle is.
* **$k_0 = 5.0$ (Wave Number):** Controls central momentum ($\langle p \rangle = \hbar k_0$); positive sign dictates rightward motion.

---

### 2. Analytical Expression
The wave packet is constructed as a localized Gaussian envelope modulated by a plane wave phase:

$$\psi(x, 0) = \exp\left( -\frac{(x - x_0)^2}{2\sigma^2} \right) \cdot \exp(i k_0 x)$$

* **Gaussian Envelope:** Confines the particle within a localized region so it does not extend infinitely.
* **Complex Phase Factor ($e^{i k_0 x}$):** Encodes kinetic energy and propagation direction using Euler's formula ($\cos(k_0 x) + i \sin(k_0 x)$).