             #EX 1) implement matrix - vector multiplication
import numpy as np

A = np.array([[1,2,3],[4,5,6],[7,8,9]])
V = np.array([1,2,-4])
result = np.dot(A,V)
print("Array X vector : \n", result)

             #EX 2) Explore special matrix

I = np.eye(3)
print("Array X Identity matrix : \n",np.dot(A,I))

Z = np.zeros((3,3))
print("Array X Zero matrix : \n",np.dot(A,Z))

D = np.diag([1,2,3])
print("Array X Diagonal matrix : \n",np.dot(A,D))