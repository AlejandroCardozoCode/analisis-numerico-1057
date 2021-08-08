import sympy as sy 
from sympy import *
import math

# implementacion de metodo de Newton
def metodoNewton(v, e, funcion):
    
    r = float(v - (valorFuncion(funcion,v)/derivada(funcion,v)))
    iteracions = 0
    while abs(float(r - v)) > e:
        i = i + 1
        v = r
        r = float(v - (valorFuncion(funcion,v)/derivada(funcion,v)))
    print("El numeor de iteraciones fue de: " + str(iteraciones))
    return r
    
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

#impresion del menu de consola
tolerancia = input("Ingrese el valor de la toleracia: ")
valor = input("Ingrese el valor: ")
print("1) (cos(x))**2 - x ** 2")
print("3) x ** 3 - 2*(x**2) + ((4/3)*x) - 8/27")
numeroF = int(input("Ingrese la funcion que desea trabajar: "))

#asignacion del valor de la funcion 
funcion = None
if numeroF == 1:
    funcion = funcion1
elif numeroF == 3:
    funcion = funcion3

# ejecucion del codigo 
print(metodoNewton(float(valor), float(tolerancia), funcion))