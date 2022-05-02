import numpy as np

#Creando heurística constructiva para resolver el problema de la mochila

#Definiendo variables del problema de la mochila

c = [3,4,8,3,6,4,10,4,10,9] #Costos de los productos que entran a la mochila
v = [6,4,3,3,3,5,9,8,5,10] #Volumen por costo de producto

b = 26 #Capacidad limite de la mochila

'''Definiendo el indice de sensibilidad

Es el criterio que establece que productos deden meterse a la mochila, dando prioridad en este caso al costo'''

D = np.array([c,v]).transpose()
print(D)

#orddenando la matriz D con bas ene el criterio de costo
D = tuple(D) #Transformando el arreglo a tupla para poder ordenarlo
D = np.array(sorted(D, key=lambda x: x[0],reverse=True))#Orden decreciente
print(D)

#Declarando asignaciones
x = np.zeros((len(c)),dtype=int)

#Indice que alamacena el numero de productos a agregar
k = -1
volumen = np.matmul(np.array(D[:,1].transpose()), x)
#print(volumen)

while(b > volumen):
    #print(volumen)
    k = k + 1

    #Agregando el produdcto más caro
    x[k] = 1

    costo = np.matmul(D[:,0],x)
    volumen = np.matmul(np.array(D[:,1].transpose()), x)

    if k == 10:#Caso ideal, pero no se necesitaria optimizar
        print("Se han agregado todos los productos")

#Eliminando el ultimo elemento, ya que sobrepasa la capacidad de la mochila
x[k] = 0
#Recalculando costo y volumen
costo = np.matmul(D[:,0],x)
volumen = np.matmul(np.array(D[:,1].transpose()), x)

print("Solucion: ",x)
print("Volumen: ",volumen)
print("Costo: ",costo)

