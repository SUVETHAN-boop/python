             #Derivatives and Partial Derivatives

import sympy as sp 

# 1)derivatives
x = sp.Symbol("x")
f = x**2
derivatives = sp.diff(f,x)
print("Derivatives : \n",derivatives)

# 2)partial derivatives
x, y =sp.symbols('x y')
f = x**2 + y**2
deri_x = sp.diff(f,x)
deri_y = sp.diff(f,y)

print("Partial Derivatives : \n",deri_x," + ",deri_y)