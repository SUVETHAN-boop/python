             #to perform Singular value Demposition and Reconstruct matrix

import numpy as np

m1 = np.array([[3,4,5],[6,8,9],[4,6,9]])

#svd
U,S,Vt = np.linalg.svd(m1)
print("Singular matrix : \n",S)
print("U : \n",U)
print(" V Transpose : \n",Vt)

#Reconstrut 
sigma = np.zeros((3,3))
np.fill_diagonal(sigma,S)
reconstructed = U @ sigma @ Vt
print("Sigma diagonal matrix : \n",sigma)
print("Reconstruct matrix : \n",reconstructed)