import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib.pyplot as plt

def simps(f,a,b,N):
    if N % 2 == 1:
        raise ValueError("N must be an even integer.")
    dx = (b-a)/N
    x = np.linspace(a,b,N+1)
    y = f(x)
    S = dx/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    return S

def plot_with_death_rate(S, I, R, t, divide_by=1, death_rate=0.05):
    # Dibujamos los datos de S(t), I(t) y R(t)
    fig, ax = plt.subplots()
    ax.plot(t, S / divide_by, 'b', alpha=0.5, lw=2, label='Susceptible')
    ax.plot(t, I / divide_by, 'r', alpha=0.5, lw=2, label='Infectado')
    RR = R * (1 - death_rate)
    DD = R - RR
    ax.plot(t, RR / divide_by, 'g', alpha=0.5, lw=2, label='Recuperado con inmunidad')
    ax.plot(t, DD / divide_by, 'k', alpha=0.5, lw=2, label='No recuperado')
    ax.set_xlabel('Tiempo /días')
    ax.set_ylabel(f'Número (dividido por {divide_by:,})')
    legend = ax.legend()
    #fig.show() # descomenta esto si no estás en Jupyter

p1=1.26145125
p2=2.97026060
p3=6.29158016
areaAcumulada = 0
s1 = simps(lambda x : 4+np.cos(x+1),0,p1,100)
s2 = simps(lambda x : (math.e**x) *np.sin(x),0,p1,100)
areaAcumulada = areaAcumulada + s1-s2

s1 = simps(lambda x : 4+np.cos(x+1),p1,p2,100)
s2 = simps(lambda x : (math.e**x) *np.sin(x),p1,p2,100)
areaAcumulada = areaAcumulada + s2-s1

s1 = simps(lambda x : 4+np.cos(x+1),p2,p3,100)
s2 = simps(lambda x : (math.e**x) *np.sin(x),p2,p3,100)
areaAcumulada = areaAcumulada + s1-s2

print("El are es de: {:0.8f}".format(areaAcumulada))

# Integrate the SIR equations over the time grid, t.
ret = odeint(deriv, y0, t, args=(N, beta, gamma))
S, I, R = ret.T
 
plot(S, I, R, t) # Datos sin normalizar
plot(S, I, R, t, divide_by=N) # Datos normalizados
plot_with_death_rate(S, I, R, t, divide_by=N, death_rate=0.05)