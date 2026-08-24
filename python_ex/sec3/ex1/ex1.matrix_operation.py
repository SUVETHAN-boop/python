             #Matrix operation
import numpy as np

m1 = np.array([[1,2], [4,5]])
m2 = np.array([[7,8],[10,11]])

# 1)Addition and Subraction  
print("ADD : \n",m1 + m2)
print("SUB : \n",m1 - m2)


# 2)Scalar maultipile
c  = 2 * m1
print("Scalar mult : \n",c)

# 3)matrix multiple
matrix_mult = np.dot(m1,m2)
print("multiple matrix : \n",matrix_mult)


             #Spical matrix

# 1) Identity matrix(I)
I = np.eye(3)
print("Identity matrix : \n",I)

# 2) Zeros matrix(0)
zero = np.zeros((2,3))
print("Zeros matrix : \n",zero)

# 3) Diagonal matrix
D = np.diag([1,2,3])
print("Diagonal matrix : \n",D)