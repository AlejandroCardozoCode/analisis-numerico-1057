import sympy as sy 
from sympy import *
import math
from mpmath import mp, mpf
# implementacion de metodo de Newton
def metodoNewton(v, e, funcion):
    
    r = mpf(v - (valorFuncion(funcion,v)/derivada(funcion,v)))
    iteraciones = 0
    while abs(mpf(r - v)) > e:
        iteraciones = iteraciones + 1
        v = r
        r = mpf(v - (valorFuncion(funcion,v)/derivada(funcion,v)))
    print("El numero de iteraciones fue de: " + str(iteraciones))
    return mpf(r)
    
# funcioni que valcula el valor de la funcion
def valorFuncion(funcion,v):
    return funcion.evalf(subs = {x:v}) 

# funcion que calcula la derivada de la funcion 
def derivada(funcion, v):
    deriv = sy.diff(funcion,x)
    return deriv.doit().subs({x:v}).evalf()

#definicion de los parametros y funciones necesarias
x = sy.Symbol('x')
funcion1 = (cos(x))**2 - x ** 2
funcion3 =  x ** 3 - 2*(x**2) + ((4/3)*x) - 8/27 
mp.dps = 0

#impresion del menu de consola
valor = input("Ingrese el valor: ")
print("---------------------------------------")
print("1) (cos(x))**2 - x ** 2")
print ("2) x sin(x) - 1 en [-1,2]")
print("3) x ** 3 - 2*(x**2) + ((4/3)*x) - 8/27")
print ("4) ")
print ("5) x^3 - 2x - 5 = 0")
print("---------------------------------------")
numeroF = int(input("Ingrese la funcion que desea trabajar: "))

#asignacion del valor de la funcion 
funcion = None
if numeroF == 1:
    funcion = funcion1
elif numeroF == 3:
    funcion = funcion3

toleranciaN = None 

#asignacion de la tolerancia
print("---------------------------------------")
print("1) 10^-8")
print("2) 10^-16")
print("3) 10^-32")
print("4) 10^-56")
print("---------------------------------------")
valorTolerancia = int(input("Ingrese el valor de la tolerancia deseada: "))

if valorTolerancia == 1:
    toleranciaN = 1.0e-8 
    mp.dps = 8 
elif valorTolerancia == 2:
    toleranciaN = 1.0e-16  
    mp.dps = 16 
elif valorTolerancia == 3:
    toleranciaN = 1.0e-32  
    mp.dps = 32 
elif valorTolerancia == 4:
    toleranciaN = 1.0e-56  
    mp.dps = 56
else:
    print("Valor de tolerancia no valido")

# ejecucion del codigo 
print(mpf(metodoNewton(mpf(valor), mpf(toleranciaN), funcion)))