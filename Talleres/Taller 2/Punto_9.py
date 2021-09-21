from numpy import *
import numpy
import numpy as np

def f(A,x,b):
    return 0.5*np.dot(np.dot(x,A),x)+np.dot(b,x)
def  g(A,x,b):
    return np.dot(A,x)+b
#
def minimize_cg(A,b, x0, jac=None,gtol=1e-5,maxiter=None,disp=False):
    if maxiter is None:
        maxiter = len(x0) * 200
    gfk = np.dot(A, x0) + b
    k = 0
    xk = x0
    warnflag = 0
    pk = -gfk

    gnorm = numpy.amax(numpy.abs(gfk))
    while (gnorm > gtol) and (k < maxiter):
        deltak = numpy.dot(gfk, gfk)
        alpha_k = -np.dot(gfk, pk) / (np.dot(np.dot(pk,A.T ),pk))
        xk = xk + alpha_k * pk
        gfkp1=np.dot(A, xk) + b
        beta_k = max(0, numpy.dot(gfkp1, gfkp1) / deltak)
        pk = -gfkp1 + beta_k * pk
        gfk = gfkp1
        gnorm=numpy.amax(numpy.abs(gfk))#Valor máximo como norma
        k += 1
    if warnflag == 0:
        # msg = _status_message['success']
        if disp:
            print('success')
            print("         Valor de la función Actual: " , xk )
            print("         Iteraciones: %d" % k)
            print("         Valor de la función: " , f(A,xk,b))
            print("         Valor actual de x*: ",-np.dot(np.linalg.inv(A),b))
            print("         Valor de la función actual f(x*): ",f(A,-np.dot(np.linalg.inv(A),b),b))

if __name__ == '__main__':
    x0 = [0, 0]
    A=np.array([[2,-1],[-1,2]])
    b=[1,0]
    g0=g(A,x0,b)
    minimize_cg(A,b,x0,g0,disp=True,maxiter=10000)
