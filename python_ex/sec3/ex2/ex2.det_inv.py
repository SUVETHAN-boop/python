             #Determinats and invers

import numpy as np

m1 = np.array([[11,30],[40,50]]) 

# 1) Determinats 
determinats = np.linalg.det(m1)
print("Determinats matrix : \n",determinats)

# 2) Invers
print("matrix : \n",m1)
invers = np.linalg.inv(m1)
print("Invers matrix : \n",invers)


            #Eiganvalues and Eiganvectors

eiganValue,eiganVector = np.linalg.eig(m1)
print("Eiganvalue : \n",eiganValue)
print("Eiganvectors : \n",eiganVector)

             #Matrix demoposition

U,S,Vt =np.linalg.svd(m1)
print("U : \n",U)
print("Singular value : \n",S)
print("V transpose : \n",Vt)