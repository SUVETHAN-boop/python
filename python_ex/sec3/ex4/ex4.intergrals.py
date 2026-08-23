             # Definite Intergral and Indefinite indergral 

import sympy as sp

x = sp.Symbol("x")
f = x**2
definit_integral = sp.integrate(f,(x,0,2))
indefinit_integral = sp.integrate(f,x)

print("Definite Inertgral : \n",definit_integral)
print("Indefinite Inertgral : \n",indefinit_integral)
