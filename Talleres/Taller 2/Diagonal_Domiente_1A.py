import numpy as np
def es_diagonal_dominante(x):
    abs_x=np.abs(x)
    return np.all(2*np.diag(abs_x)>=np.sum(abs_x,axis=1))
A = np.array([[1,8,2],
             [1,1,5],
             [3,-1,1]])
print(es_diagonal_dominante(A))
