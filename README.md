# The Goal

> The goal of this project is to imagine an electron moving from a source toward a potential barrier. We do not know the exact position of the electron, so we will plot its probability density using a Gaussian function and a phase function. Then, we will use the Schrödinger equation to simulate how the electron changes with time as it reaches the potential barrier. We want to see what happens to the wave during and after it hits the barrier.

---

### Gaussian Function

$$
G(x) = e^{-\frac{(x-x_0)^2}{2\sigma^2}}
$$

### Phase Function

$$
f(x) = e^{ikx}
$$

$$
e^{ikx} = \cos(kx) + i\sin(kx)
$$

### Parameters

- $k_0$
- $\sigma$
- $x_0$

### Wave Function
$$
\psi(x) = e^{-\frac{(x-x_0)^2}{2\sigma^2}} \cdot f(x) = e^{ikx}
$$
