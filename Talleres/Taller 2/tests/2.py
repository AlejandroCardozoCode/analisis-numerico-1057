
def Jacobi(mx,mr,n=100,c=0.0001):
        if len (mx) == len (mr): #Si mx y mr tienen la misma longitud, comience la iteración; de lo contrario, la ecuación no tiene solución
            x = [] # Valor inicial iterativo inicializado en una sola fila toda la matriz 0
        for i in range(len(mr)):
            x.append([0])
        cuenta = 0 #Cuenta el número de iteraciones
        while count < n:
            nx = [] # Guardar el conjunto de valores después de una sola iteración
            for i in range(len(x)):
                nxi = mr[i][0]
                for j in range(len(mx[i])):
                    if j!=i:
                        nxi = nxi+(-mx[i][j])*x[j][0]
                        nxi = nxi/mx[i][i]
                        nx.append ([nxi]) # Calculado iterativamente el siguiente valor xi
                        lc = [] # almacena el conjunto de errores entre los resultados de dos iteraciones
                        for i in range(len(x)):
                            lc.append(abs(x[i][0]-nx[i][0]))
                            if max(lc) < c:
                                return nx #Cuando el error cumple con los requisitos, devuelve el resultado del cálculo
                            x = nx
                            count = count + 1
                            return False #Si el resultado de la iteración establecida aún no está satisfecho, la ecuación no tiene solución
                    else:
                        return False
 
mx = [[8,-3,2],[4,11,-1],[6,3,12]]
 
mr = [[20],[33],[36]]
print(Jacobi(mx,mr,100,0.00001))