# FFT Convolution
## Convolution
According to the definition of convolution

$$
\begin{aligned}
    h(x) & = \frac{1}{\sqrt{2\pi}}\int (f \circ g) \dd y\\
    & = \frac{1}{\sqrt{2\pi}}\int f(x-y) g(y) \dd y
\end{aligned}
$$

in which

$$
f(x) = \frac{1}{\sqrt{2\pi}}\int \hat{f}(k) e^{\ii kx} \dd k\\
g(x) = \frac{1}{\sqrt{2\pi}}\int \hat{g}(w) e^{\ii wx} \dd w
$$


Thus,

$$
\begin{aligned}
    h(x) & = \frac{1}{\sqrt{2\pi}}\int f(x-y) g(y) \dd y\\
    & = \frac{1}{\sqrt{2\pi}}\int g(y)  \left(\frac{1}{\sqrt{2\pi}}\int \hat{f}(w) e^{\ii w(x-y)} \dd w \right) \dd y\\
    & = \frac{1}{2\pi}\int \int g(y)   \hat{f}(w) e^{\ii w(x-y)} \dd w  \dd y\\
    & = \frac{1}{\sqrt{2\pi}}\int \hat{f}(w) \left(\frac{1}{\sqrt{2\pi}}\int g(y) e^{-\ii wy}\dd y\right)    e^{\ii wx} \dd w  \\
    & = \frac{1}{\sqrt{2\pi}}\int \hat{f}(w)\hat{g}(w)    e^{\ii wx} \dd w  
\end{aligned}
$$

## Non uniform Discrete fourier transform
Seems to have accuracy problem. See template over [here](/notebooks/background/numerical_methods/FFT/convolution.ipynb#convolution-with-stretched-coordinate). [^5j9F29dT]

### Non uniform space and uniform wavenumber
Given data $x_i, i = 0, 1, 2, \dots N-1$ then the non-unform Discrete fourier transform is,

$$
X_k = \sum_{n=0}^{N-1} x_n e^{-\ii 2\pi p_n f_k} \dd p_n,\\
x_n = \sum_{k=0}^{N-1} X_k e^{\ii 2\pi p_n f_k}\dd f_k,
$$

in which $p_n$ are sample points and $f_k$ are frequency. 

In our case, given $N$ data, we have uniform frequency $f_k = [0, 1, \dots, N-1]$ and non-uniform sample point $p_n = \zeta_n \in [0, 1]$.


## Higher dimension FFT convolution

Higher dimensional convolution can be performed by first convolving with a 1-D Gaussian in the x direction, and then convolving with another 1-D Gaussian in the y direction. (The Gaussian is in fact the only completely circularly symmetric operator which can be decomposed in such a way.) [^Gaussian_Smoothing]

[^Gaussian_Smoothing]: https://homepages.inf.ed.ac.uk/rbf/HIPR2/gsmooth.htm

For our concerned problem, we need to calculate,

$$
\begin{align}
    \hat{C}^\dag(\boldsymbol{x}^\top) &= \left\langle \exp{\left(-\frac{\|\boldsymbol{x} - \boldsymbol{x}^\top\|_2}{2\sigma^2}\right)}, C^\dag(\boldsymbol{x})\right\rangle\\
    & = \int C^\dag(\boldsymbol{x})  \exp{\left(-\frac{\|\boldsymbol{x} - \boldsymbol{x}^\top\|_2}{2\sigma^2}\right)} \dd \boldsymbol{x}.
\end{align}
$$


Let 

$$
f(\boldsymbol{x}, \boldsymbol{y}, \boldsymbol{\zeta}) = C^\dag(\boldsymbol{x}, \boldsymbol{y}, \boldsymbol{\zeta}),
$$ 

and 

$$
g(\boldsymbol{x}, \boldsymbol{y}, \boldsymbol{\zeta}) = \underbrace{\exp{\left(-\frac{\|\boldsymbol{x}\|_2}{2\sigma^2}\right)} \exp{\left(-\frac{\|\boldsymbol{y}\|_2}{2\sigma^2}\right)}}_{\mathcal{F}^{-1}(\hat{G}_x(i)\hat{G}_y(j))} \; \underbrace{\exp{\left(-\frac{\|\boldsymbol{\zeta} \|_2}{2\sigma^2}\right)}}_{g_z(\zeta)}
$$


Then, we have

$$
\begin{aligned}
    h(x', y', \zeta') 
    & = \iiint f(x, y, \zeta) g(x-x', y-y', \zeta - \zeta') \dd x \dd y\dd \zeta \\
    & = \iint\left(\int \hat{f}(i, j, \zeta) g_z(\zeta - \zeta') \dd \zeta \right)\hat{G}_x(i)\hat{G}_y(j) e^{\ii ix}e^{\ii jy} \dd i \dd j \

\end{aligned}
$$

In Discrete version,



## Reference
1. [FFT Convolution](https://www.analog.com/media/en/technical-documentation/dsp-book/dsp_book_ch18.pdf)
[^5j9F29dT]: <https://en.wikipedia.org/wiki/Non-uniform_discrete_Fourier_transform>