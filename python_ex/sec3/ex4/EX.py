             # Simple Integral

import sympy as sp

x = sp.Symbol("x")
f = sp.exp(-x)

#definit integral
definit_integral = sp.integrate(f,(x,0,sp.oo))
print("Definit Integral : \n",definit_integral)

#indifint integral
indefint_integral = sp.integrate(f,x)
print("Indefinit Integral : \n",indefint_integral)