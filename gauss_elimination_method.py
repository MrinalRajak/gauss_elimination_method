

#Gauss elimination method

import numpy as np
A=np.array([[25,5,1],[64,8,1],[144,12,1]],dtype=float)
b=np.array([106.8,177.2,279.2],dtype=float)
n=len(A)

#Triangularization

for k in range(n-1):
    for i in range(k+1,n):
        u=A[i,k]/A[k,k]
        for j in range(k,n):
            A[i,j]=A[i,j]-u*A[k,j]
        b[i]=b[i]-u*b[k]
print("\nTriangularization Matrix A\n: ",A)
print("\nMatrix b: \n",b)

#Determination

x=np.zeros(n)
k=(n-1)
x[k]=b[k]/A[k,k]
while k>=0:
    x[k]=(b[k]-np.dot(A[k,k+1:],x[k+1:]))/A[k,k]
    k=k-1

print("\nsolution for x: \n",x)
