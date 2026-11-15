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

نحتاج الى تطبيع الدالة الموجية بأخذ تربيع مقدارها ثم حساب المساحة كاملة تحت منحنى مربع المقدار ثم حساب المعامل A الذي معناه اننا اذا ضربناه في مساحة مربع المقدار سنحول الناتج الكلي إلى 1 وهي المساحة التي تمثل تواجد الالكترون حتى يكون الناتج يساوي 100% 

### Total Area
$$
S = \int | \psi |^2 dx
$$

### Parameter A
$$
A = \frac{1}{\sqrt(S)}
$$

### Normaliztion Wave Function
$$
\int |A\psi(x)|^2 dx = 1
$$ 

بالنسبة ل dx فهو اصغر عرض ممكن على المحور فلو كان على المحور نقطتين 1 و 2 وكان هناك 50 نقطة بين 1 و 2 ف العرض dx سيكون 0.02 لأن النقطة التالية هي 1.02