import sys
import numpy as np
import random
import math

#limit = sys.getrecursionlimit()
sys.setrecursionlimit(999999)

print("Iniciando...")

#PARAMETROS DEL PROBLEMA 8 X 3
J = [0,1,2,3,4,5,6,7] #Vector de clientes
n = len(J) #Numero de clientes

I = [0,1,2] #Vector de servicios
m = len(I) # Numero de servicios

cap = [160,90,70] #Capacidad de los servicios Q
# FIN DE LOS PARAMETROS

INT_MAX = sys.maxsize


c = [[10,11,12,13,14,15,16,17]
    ,[22,24,26,28,30,32,34,36],
    [60,64,68,72,76,80,84,88]] # Matriz de costos


req = np.array( [[48,47,46,45,44,43,42,41],
        [38,37,36,35,34,33,32,31],
        [28,27,26,25,24,23,22,21]]) # Matriz de solicitudes de los clientes


#Definiendo una solucion inicial

sol = [-1,-1,-1,-1,-1,-1,-1,-1] #Para cada cliente, su servidor



def greedy():
    req2 = np.transpose(req)

    cap_resta = cap

    bandera_sol = 0

    i = 0
    while(i < len(req2)):
        print("i  ",i)
        vec = np.array(req2[i])
        print(vec)

        maximum = np.max(vec)
        maximum = int(np.where(vec == maximum)[0])
        print(maximum)
        #print(req2)
        if(cap_resta[maximum]>=vec[maximum]):
            cap_resta[maximum] = cap_resta[maximum] - vec[maximum]
            sol[i] = maximum
            req2[i][maximum]=0

            print(sol)
            print(cap)
            i = i + 1
        else:
            req2[:,maximum] = 0
        
        print(req2)
            #bandera_sol =  bandera_sol + 1
        

    print("sol---",sol)
                
print("Iniciado heuristica")

greedy()

print("Terminando heuristica ....")
