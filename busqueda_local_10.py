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



# almacena la mejor solución hasta ahora
def storeBest(sol,z):
    zub = int(z)
    for j in range(0,n):
        solbest[j] = sol[j]
    
    print("StoreBest =",solbest)
    print("zub =",zub)

def LocalSearch_opt10(c,isOriginal):
    #c es una matriz
    #isOriginal es una booleana

    #int z=0,zorg
    #int i, isol, j
    z = 0 
    capleft = [cap[i] for i in range (0,m)]
    print("capleft=",capleft)


    for j in range(0,n):
        capleft[sol[j]] -= req[sol[j]][j]
        z += c[sol[j]][j]
    
    #zorg=z

    #l0
    l0(capleft,isOriginal,z)
    
def l0(capleft,isOriginal,z):
    for j in range (0,n):
        isol = sol[j]
        for i in range(0,m):
            if (i == isol):
                continue #regresa el control al ciclo
            
            #print("Antes")
            #print("c[i][j]=",c[i][j])
            #print("c[isol][j]=",c[isol][j])
            #print("capleft[i]=",capleft[i])
            #print("req[i][j]=", req[i][j])
            if (c[i][j] < c[isol][j] and capleft[i] >= req[i][j]): #remove from isol and assign to i
                sol[j] = i
                capleft[i] -= req[i][j]
                capleft[isol] += req[isol][j]
                z -= (c[isol][j] - c[i][j])
                
                if(isOriginal and z<zub):
                    storeBest(sol,z)
                    print("[1-0 opt] new zub:",zub)
                #goto l0
                l0(capleft,isOriginal,z)

    print("Valor Z=",z)
    print("Solucion =",sol)
    print("Mejor solucion =",solbest)
    print("Matriz de costos =",c)
    print("Matriz de solicitudes =",req)
    print("Capacidad de los servicios =",cap)


LocalSearch_opt10(c,True)

print("Fin del programa.....")