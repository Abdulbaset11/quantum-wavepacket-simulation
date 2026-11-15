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
\psi(x) = e^{-\frac{(x-x_0)^2}{2\sigma^2}} \cdot e^{ikx}
$$

## Normalization

> We need to normalize the wave function. First, we calculate the squared magnitude of the wave function. Then, we calculate the total area under the curve.

After that, we calculate the factor **A**. When we multiply the wave function by **A**, the total area becomes **1**.

This means the total probability of finding the electron in the full region is **100%**.

---

### Total Area

$$
S = \int |\psi|^2 \, dx
$$

### Factor A

$$
A = \frac{1}{\sqrt{S}}
$$

### Normalized Wave Function

$$
\int |A\psi(x)|^2 \, dx = 1
$$

---

### Step Size (dx)

`dx` is the distance between two neighboring points on the x-axis.

**Example:**

If the distance from `x = 1` to `x = 2` is divided into **50 equal parts**, then:

- `dx = 0.02`
- The next point after `1` is `1.02`.

---