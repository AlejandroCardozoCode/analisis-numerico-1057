import numpy as np
  
#creacion de la matriz
m = np.array([[1, 0.5, 0.33], 
            [0.5, 0.33, 0.25],
            [0.33, 0.25 ,0.2]])
#funcion que nos permite encontrar el nuemro de condicion 
numero_condicion =  np.linalg.cond(m, "fro")
print("Frobenious: " + str(numero_condicion))

numero_condicion =  np.linalg.cond(m, 1)
print("Norma 1: " + str(numero_condicion))

numero_condicion =  np.linalg.cond(m, np.inf)
print("Norma Infinito: " + str(numero_condicion))