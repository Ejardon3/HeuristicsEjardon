import sys


print("Iniciando...")

#PARAMETROS DEL PROBLEMA 8 X 3
J = [0,1,2,3,4,5,6,7] #Vector de clientes
n = len(J) #Numero de clientes

I = [0,1,2] #Vector de servicios
m = len(I) # Numero de servicios

cap = [160,90,70] #Capacidad de los servicios Q
# FIN DE LOS PARAMETROS

INT_MAX = sys.maxsize

zub = INT_MAX

c = [[10,11,12,13,14,15,16,17]
    ,[22,24,26,28,30,32,34,36],
    [60,64,68,72,76,80,84,88]] # Matriz de costos


req =  [[48,47,46,45,44,43,42,41],
        [38,37,36,35,34,33,32,31],
        [28,27,26,25,24,23,22,21]] # Matriz de solicitudes de los clientes


#Definiendo una solucion inicial
sol = [2,2,2,2,2,2,2,2] #Para cada cliente, su servidor
solbest = [2,2,2,2,2,2,2,2] #Mejor solución para cada cliente, su servidor

