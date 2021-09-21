import numpy as np

A= np.array([[1,4,0],
             [0,1,1],
             [2,0,3]])
B= np.array([[5],
             [2],
             [0]])

#encontramos la matriz triangular superior
U=(np.triu(A))
#encontramos la matriz triangular inferior
L=(np.tril(A))
print('matriz triangular inferior')
print(L)
print('matriz triangular superior')
print(U)


D=np.array([[1,0,0],
              [0,1,0],
              [0,0,1]])
DI=np.linalg.inv(D)

sum=L+U
print('Suma de L y U')
print(sum)
print('Matriz de transicion')
T=np.matmul(DI,sum)
print(T)
#encontrar valores propios
VP, vectarCaracteristicas=np.linalg.eig(T)
print('Valores propios de la matriz de transicion')
print(VP)
print('Vectores propios de la matriz de transicion')
print(vectarCaracteristicas)

print('valor maximo de los valores propios')
Max=np.amax(VP)
print(Max)
absMax=abs(Max)
print('Valor Abosluto del Max')

print(absMax)

if(absMax<1):
    print('CONVERGE')
else:
    print('NO CONVERGE')

