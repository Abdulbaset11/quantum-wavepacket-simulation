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

Selecting the appropriate resolution involves a critical computational trade-off:
* **Under-sampling (Too few points / Large $\Delta x$):**
  * Violates the Nyquist-Shannon sampling limit relative to the de Broglie wavelength ($\Delta x \not\ll \lambda$).
  * Causes numerical aliasing, geometric distortion, and coarse, jagged representations that miscalculate wave derivatives ($\frac{\partial^2 \psi}{\partial x^2}$).
* **Over-sampling (Too many points / Extremely small $\Delta x$):**
  * Demands excessive processor memory (RAM) and drastically increases execution time.
  * In explicit time-stepping schemes, very small $\Delta x$ requires a punishingly small time-step $\Delta t$ to preserve numerical stability.

**Initial Choice:** We set $N = 1000$ points ($\Delta x \approx 0.02$). This ensures smooth spatial derivatives while maintaining lightweight, real-time performance.