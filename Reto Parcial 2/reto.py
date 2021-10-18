from scipy import interpolate
import matplotlib.pyplot as plt
import pandas as pd
import random

# definicion de arreglos globales
hora_inter = []
temp_inter = []
hora_inter_2 = []
temp_inter_2 = []

# inicializacion de los arreglos
hora = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
        14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
hora_30 = hora.copy()
temperatura_inicial = []
temperatura_30 = []


# calcular valores por interpolacion
def inter(hora_v, temperatura):
    interpolacion_hora_temp = interpolate.interp1d(hora_v, temperatura)

    i = hora_v[0]
    for x in range(0, len(hora)*2 + 1):
        hora_inter.append(i)
        temp_inter.append(interpolacion_hora_temp(i))
        i = i + 0.5

# calcular valores por interpolacion cuadratica


def inter_cuadratica(hora_v, temperatura):
    interpolacion_hora_temp_2 = interpolate.interp1d(
        hora_v, temperatura, kind="cubic")
    i = hora_v[0]
    for x in range(0, len(hora)*2 + 1):
        hora_inter_2.append(i)
        temp_inter_2.append(interpolacion_hora_temp_2(i))
        i = i + 0.5

# esta funcion se encarga de tomar los datos de la tempreratura del excel en un dia juliano en especifico


def cargar_excel():
    excel = pd.read_excel(
        "D:\Carpetas Windows\documentos\GitHub\Analisis Numerico\Reto Parcial 2\Base_datos.xls", sheet_name='Aiuaba')

    excel = excel.loc[excel["Dia Juliano"] == 92]
    excel = excel[["Temp. Interna (ºC)"]]
    return excel.to_numpy()


# impresion de graficas de los datos
def imprimir_resultados():
    plt.plot(hora, temperatura_inicial, '+-r',
             linewidth=2, label="Datos Originales")
    plt.scatter(hora, temperatura_inicial, s=120, c='#FF0000', marker="+")
    plt.plot(hora_inter, temp_inter, '.-g',
             linewidth=1, label="Interpolacion Lineal")
    plt.plot(hora_inter_2, temp_inter_2, '.-b',
             linewidth=1, label="Interpolacion cuadratica")
    plt.xlabel('Hora del dia')
    plt.ylabel('Temperatura interna (c)')
    plt.legend()
    plt.show()


# asignacion del arreglo de los datos obtenidos por el excel
arreglo = cargar_excel()
for x in arreglo:
    temperatura_inicial.append(x.item())

temperatura_30 = temperatura_inicial.copy()

# eliminacion de los datos 30%
datos_eliminar_num = (int)(len(temperatura_inicial) * 0.30)
for i in range(0, datos_eliminar_num):
    posicion = random.randrange(1, len(temperatura_30)-1)
    temperatura_30.pop(posicion)
    hora_30.pop(posicion)


# calculo de la interpolaciones
inter(hora_30, temperatura_30)
inter_cuadratica(hora_30, temperatura_30)

# impresion de los datos ya calculados
imprimir_resultados()
