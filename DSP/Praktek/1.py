import sympy as sym
from IPython import get_ipython
ipy = get_ipython()
if ipy is not None:
    ipy.run_line_magic('matplotlib', 'inline')
sym.init_printing()

t, sigma, omega = sym.symbols('t sigma omega', real=True)
s = sigma + 1j*omega
x = sym.exp(s*t)

y = x.subs({omega: 10, sigma: -.1})

sym.plot(sym.re(y), (t, 0, 2*sym.pi), ylabel=r'Real{$e^{st}$}')
sym.plot(sym.im(y), (t, 0, 2*sym.pi), ylabel=r'Imajiner{$e^{st}$}');
