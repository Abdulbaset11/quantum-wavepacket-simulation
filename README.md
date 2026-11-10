# The goal

> This project is to visualize a scenario in which an electron, fired from a source, moves toward an energy barrier. The exact position of the electron is unknown; instead, there is a probability of finding it at any given location, which is represented by a wave function.

---

I will begin by drawing a number line to represent this wave function, and subsequently, I will refine the wave function so that it evolves in a way that mirrors the actual motion of the electron.

### The wave equation

$$
\psi(x) = e^{-\frac{(x-x_0)^2}{2\sigma^2}} \cdot e^{ik_0x}
$$

---

Now I will normalize the wave equation to probability density

### Total Area

$$
\text{Total Area} = \int_{-\infty}^{\infty} |\psi(x)|^2 ~ dx
$$


### Parameter A

$$
A = \frac{1}{\sqrt{Total Area}}
$$