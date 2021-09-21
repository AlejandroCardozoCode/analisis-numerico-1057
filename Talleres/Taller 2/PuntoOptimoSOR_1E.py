import numpy as np
 #Creamos la matriz A de coeficientes
A = [[1,-8, -2], [1, 1, 5], [3, -1, 1]]
# Creamos el vector de términos independientes

b = [1, 4, -2]
# Valores iniciales
tol = 0.00001  # valor de la tolerancia establecida
error = 100000000000000000000000  # valor inicial de la norma
kmax = 100  # número máximo de iteraciones
n = len(A)  # determina tamaño de A
x = np.zeros(n)  # vector x inicial de ceros
x1 = np.copy(x)  # vector auxiliar de x
k = 1  # contador inicial de iteraciones
error1 = [0]
lambd = 1.4

while k < kmax and error > tol:
    print("iteración: ", k)
    for i in range(n):
        sumatoria = 0
        for j in range(n):
            if i != j:
                sumatoria += (A[i][j] * x[j])
        x[i] = (lambd * ((b[i] - sumatoria) / A[i][i])) + (1 - lambd) * x[i]
        if(i==1):
            print("Valor w", i, x[i])

    error = np.linalg.norm(x - x1)  # cálculo de la norma vectorial
    error1.append(error)  # se genera el vector error para ser graficado
    x1 = np.copy(x)  # actualiza vector solución iteración anterior

    #print("  error: ", error1[k])
    print()

    k += 1