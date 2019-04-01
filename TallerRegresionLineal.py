import statistics as stats
import numpy as np


def media(lista):
    u = stats.mean(lista)
    return u


def normalizacion(x, u, maxi, mini):  # <--- Funcion que normaliza los datos.
    normalizacion = (x - u) / (maxi - mini)
    return normalizacion


file = open("ex1data2.txt", 'r')  # <--- abrimos el archivo y lo leemos.
datos = file.readlines()  # <--- leemos  el archivo y readlines() devuelve una lista que contiene las líneas.

lista = []
listOperacion = []
lista60 = []
lista40 = []
auxi = []
valores = []
norma = []
cont = 1

for i in range(len(datos)):  # <-- añadimos los datos del archivo en una lista, desaparecemos '\n' con .strip y
    lista.append(datos[i].strip().split(","))  # convertimos cada linea en una lista con split().
file.close()  # <-- Cerramos el archivo usando .close()

for i in lista:  # <--- contamos la cantidad de datos dentro de lista.
    r = cont
    # print(r, i)
    cont += 1

#np.random.shuffle(lista)  # <--- revolvemos las listas dentro de lista usando .shuffle()

tam = int((cont - 1) * 0.80)  # <-- Tomamos el equivalente al 60% de los datos

for j in range(0, tam):  # <--- guarda el 60% de los datos en lista60
    lista60.append(lista[j])

for m in range(len(lista[0])):
    for n in range(len(lista60)):
        listOperacion.append(float(lista60[n][m])) # <-- se incertan uno por uno los valores dentro de listOperacion.


auxi = np.array(listOperacion).reshape(len(lista[0]), tam) #<-- crea una matriz en base a la listOperacion

for i in range(len(lista[0])):
    minimo = min(auxi[i]) #<-- Valor minimo de la fila i
    maximo = max(auxi[i]) #<-- Valor maximo de la fila i
    medi = media(auxi[i]) #<-- Valor de la media de la fila i
    valores.append([medi, minimo, maximo])  # <-- Guarda los valores de la Media, el valor Minimo y el Maximo.

for i in range(len(lista[0])):
    for j in range(len(lista60)):
        x = auxi[i][j]
        u = valores[i][0]
        mini = valores[i][1]
        maxi = valores[i][2]
        norma.append(x) #< -- Datos no normalizados
        #norma.append(normalizacion(x, u, maxi, mini))

for i in range(len(lista60)):
    norma.insert(0, 1)  # <--- insertamos x0 que es igual a 1

listNorma = np.array(norma).reshape(4, len(lista60)) #construye una lista de 4 filas por el numero de columnas de la lista60.

f = open("60.txt", "w")

for i in listNorma:
    f.write(str(i) + '\n')
f.close()

# ------------------------GRADIENTE---------------------------------#
x = listNorma  # <----- 60%  #

delta = [0, 0, 0]

for N in range(10000):
    print("------------------------------------------")
    print(delta)
    print("------------------------------------------")
    alfa = 0.0000000001
    m = 37
    listaSumatoria = []

    for i in range(3):
        sumatoria = 0
        for j in range(37):
            h = delta[0] * x[0][j] + delta[1] * x[1][j] + delta[2] * x[2][j]
            y = x[3][j]
            sumatoria = sumatoria + (h - y) * x[i][j]

        listaSumatoria.append(sumatoria)

    # print(delta)
    # print("------------")
    for p in range(3):
        tempo = delta[p] - alfa * (1 / m) * listaSumatoria[p]
        delta[p] = tempo

# --------------------------FIN-----------------------------------#
"""
listOperacion = []
auxi = []
listNorma = []
norma = []
hs = []
cont = 0

for i in range(28, 47):
    lista40.append(lista[i])

for m in range(len(lista40[0])):
    for n in range(len(lista40)):
        listOperacion.append(float(lista40[n][m]))

auxi = np.array(listOperacion).reshape(len(lista40[0]), 19)

for i in range(len(auxi)):
    for j in range(len(auxi[0])):
        x = auxi[i][j]
        u = valores[i][0]
        mini = valores[i][1]
        maxi = valores[i][2]
        norma.append(x)  #< -- Datos no normalizados
        #norma.append(normalizacion(x, u, maxi, mini))

for i in range(19):
    norma.insert(0, 1)

listNorma = np.array(norma).reshape(4, 19)

f = open("40.txt", "w")

for i in listNorma:
    f.write(str(i) + '\n')

f.close()

x = listNorma
for j in range(len(lista40)):
    h = delta[0] * x[0][j] + delta[1] * x[1][j] + delta[2] * x[2][j]
    hs.append(h)

sumaError = 0
for j in range(len(lista40)):
    sumaError = sumaError + (abs((x[3][j] - hs[j]) / x[3][j]))
n = len(lista40)

MAPE = (sumaError / n) * 100

print("H: ", delta)
print("MAPE: ", MAPE, "%")
"""