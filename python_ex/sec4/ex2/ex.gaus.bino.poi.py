import matplotlib.pyplot as plt
from scipy.stats import norm,binom,poisson,uniform
import numpy as np 

#gassuian distribution
x = np.linspace(-4,4,100)
plt.plot(x,norm.pdf(x,loc = 0,scale = 1),label ="Gassuian (u=0,s=1)")

#binomial distribution
n,p = 10,0.5
x = np.arange(0,n+1)
plt.bar(x,binom.pmf(x,n,p), alpha = 0.7,label = "binomial (n=10,p=0.5)")

#poissom distribution
lam = 3
x = np.arange(0,10)
plt.bar(x,poisson.pmf(x,lam), alpha = 0.7,label = "poisson (lam =3)" )


plt.title("probability distribution")
plt.legend()
plt.show()