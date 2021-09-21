import numpy as np
# Método de Gauss-Jordan
# Solución a Sistemas de Ecuaciones
# de la forma A.X=B
import struct

import numpy as np

# INGRESO
A = np.array([[1, -8,  -2],
              [1, 1, 5],
              [3, -1, 1]])

B = np.array([[1],
              [4],
              [-2]])

# PROCEDIMIENTO
casicero = 1e-15  # Considerar como 0

# Evitar truncamiento en operaciones
A = np.array(A, dtype=float)

# Matriz aumentada
AB = np.concatenate((A, B), axis=1)
AB0 = np.copy(AB)

# Pivoteo parcial por filas
tamano = np.shape(AB)
n = tamano[0]
m = tamano[1]

contadorOperaciones = 0

# Para cada fila en AB
for i in range(0, n - 1, 1):
    # columna desde diagonal i en adelante
    columna = abs(AB[i:, i])
    dondemax = np.argmax(columna)

    # dondemax no está en diagonal
    if (dondemax != 0):
        # intercambia filas
        temporal = np.copy(AB[i, :])
        AB[i, :] = AB[dondemax + i, :]
        AB[dondemax + i, :] = temporal
        contadorOperaciones += 3

AB1 = np.copy(AB)

# eliminacion hacia adelante
for i in range(0, n - 1, 1):
    pivote = AB[i, i]
    adelante = i + 1
    for k in range(adelante, n, 1):
        factor = AB[k, i] / pivote
        AB[k, :] = AB[k, :] - AB[i, :] * factor
        contadorOperaciones += 3
AB2 = np.copy(AB)

# elimina hacia atras
ultfila = n - 1
ultcolumna = m - 1
for i in range(ultfila, 0 - 1, -1):
    pivote = AB[i, i]
    atras = i - 1
    for k in range(atras, 0 - 1, -1):
        factor = AB[k, i] / pivote
        AB[k, :] = AB[k, :] - AB[i, :] * factor
        contadorOperaciones += 3
    # diagonal a unos
    AB[i, :] = AB[i, :] / AB[i, i]
X = np.copy(AB[:, ultcolumna])
X = np.transpose([X])

print('solución de X: ')
print(X)
print('------------------- ')
aux=np.copy(X)

resulExact = np.array([[-61/49],
              [-4/7],
              [57/49]])

resta=np.subtract(resulExact,aux)
errorAdelante=np.linalg.norm(resta)
print('Error hacia adelante : ', errorAdelante)

multiMatri=np.matmul(A,aux)
resta2=np.subtract(B,multiMatri)
errorAtras=np.linalg.norm(resta2)
print("Error hacia atras: ", errorAtras)

#Numero de condicion proceso
# creacion de la matriz
m = np.copy(AB)
# funcion que nos permite encontrar el nuemro de condicion
numero_condicion = np.linalg.cond(m)
print("Numero de condicion: " + str(numero_condicion))
