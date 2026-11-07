# quantum-wavepacket-simulation
Numerical simulation of 1D quantum wave packet dynamics and tunneling using the Time-Dependent Schrödinger Equation.

# 1D Quantum Wave Packet Simulation & Tunneling Dynamics

A computational physics project aimed at modeling, simulating, and visualizing the time evolution of a quantum wave packet governed by the **Time-Dependent Schrödinger Equation (TDSE)** in one dimension.

---

## 🔬 Scientific Motivation & Objective

Analytical solutions to quantum mechanical problems are strictly limited to idealized, highly symmetric potentials (e.g., infinite square wells, free particles, harmonic oscillators). In realistic physical systems—such as electron transport through nanostructures or quantum tunneling across arbitrary energy barriers—numerical computation serves as an indispensable virtual laboratory.

### Core Objectives:
1. **Mathematical Discretization:** Formulate spatial coordinates and quantum differential operators using finite difference schemes.
2. **Dynamic Evolution:** Propagate quantum wave packets through time using numerically stable, unitary integration methods.
3. **Phenomenological Verification:** Quantify quantum tunneling probabilities ($T$) and reflection coefficients ($R$), verifying conservation of probability ($\int |\psi|^2 dx = 1$) and Heisenberg's uncertainty principle.

---

## 📐 Mathematical Framework (Week 1 Baseline)

### 1. The Gaussian Wave Packet ($t = 0$)
The initial state is localized as a Gaussian envelope modulated by a plane wave:

$$\psi(x, 0) = \left( \frac{1}{2\pi \sigma^2} \right)^{1/4} \exp\left( -\frac{(x - x_0)^2}{2\sigma^2} \right) \exp(i k_0 x)$$

* $x_0$: Initial central spatial position.
* $\sigma$: Wave packet spatial width (spatial uncertainty $\Delta x$).
* $k_0$: Central wave number related to initial momentum via de Broglie relation: $p_0 = \hbar k_0$.
* The complex phase $e^{i k_0 x} = \cos(k_0 x) + i \sin(k_0 x)$ defines directional drift velocity.

### 2. Born Probability Density & Normalization
The continuous probability density of finding the particle at position $x$ is:

$$P(x) = |\psi(x)|^2 = \psi^*(x)\psi(x)$$

Subject to the spatial normalization constraint:

$$\int_{-\infty}^{\infty} |\psi(x)|^2 dx \approx \sum_{i} |\psi_i|^2 \Delta x = 1.0$$

---

## 🗺️ Project Roadmap

| Phase | Milestone | Focus Area | Status |
| :--- | :--- | :--- | :--- |
| **Week 1** | **State Representation & Spatial Grid** | Spatial grid discretization ($\Delta x$), complex field representation, normalization, and phase space visualization. | 🔄 Upcoming |
| **Week 2** | **Time Evolution & Free Propagation** | Finite-difference kinetic operator matrix, time step ($\Delta t$), and implementing a unitary time-stepper (Crank-Nicolson / Split-Operator). | ⏳ Planned |
| **Week 3** | **Quantum Barrier & Tunneling Dynamics** | Introducing arbitrary rectangular/delta potentials, scattering dynamics, and computing transmission ($T$) vs. reflection ($R$). | ⏳ Planned |
| **Week 4** | **Wave Packet Dispersion & Analysis** | Quantitative validation of Heisenberg uncertainty relation, wave packet dispersion analysis, and interactive animations. | ⏳ Planned |

---

## 💻 Tech Stack & Requirements

* **Language:** Python 3.10+
* **Core Libraries:**
  * `NumPy`: High-performance vectorized multidimensional array operations.
  * `Matplotlib`: Data plotting and scientific animations.
  * `SciPy`: Sparse matrices and linear system solvers (Crank-Nicolson evolution).

### Installation:
```bash
git clone [https://github.com/Abdulbaset11/quantum-wavepacket-simulation.git](https://github.com/Abdulbaset11/quantum-wavepacket-simulation.git)
cd quantum-wavepacket-simulation
pip install numpy matplotlib scipy
