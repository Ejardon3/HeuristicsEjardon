
from math import cos
import random
import numpy as np

class Hormiga():
    def __init__(self):
        self.cap =[28512,18144,10692,9072,7128,6804,5346,4536,3564,3402]  #Capacidad de los servicios Q

        self.c = [
    [0.450,0.450,37.5,37.5,34.6,34.6,40.4,40.4,25,25,28.6,28.6,40.1,40.1,37.6,37.6,39.3,39.3,36.9,36.9,33.1,33.1,31.7,31.7,43.3,43.3,17.2,17.2,37.6,37.6,12.7,12.7],
    [35.1,35.1,24.8,24.8,14.9,14.9,0.4,0.4,13.4,13.4,16.4,16.4,6.8,6.8,23.5,23.5,24.7,24.7,22.6,22.6,5.5,5.5,32.9,32.9,30.2,30.2,18.4,18.4,23.3,23.3,27,27],
    [24.9,24.9,18,18,16,16,11.7,11.7,5.1,5.1,9.9,9.9,17.3,17.3,23.2,23.2,18.2,18.2,16,16,10.2,10.2,32.5,32.5,23.5,23.5,7.9,7.9,22.9,22.9,15.8,15.8],
    [34,34,17.7,17.7,8.6,8.6,5.2,5.2,8.6,8.6,9.7,9.7,8.3,8.3,24.3,24.3,20.8,20.8,18.7,18.7,0.550,0.550,33.7,33.7,26.3,26.3,17.1,17.1,23.8,23.8,24.5,24.5],
    [31.1,31.1,41.7,41.7,35.7,35.7,30.4,30.4,33.6,33.6,33.4,33.4,38.3,38.3,9.5,9.5,41.7,41.7,39.5,39.5,31,31,0.170,0.170,47.1,47.1,24,24,12.8,12.8,34.9,34.9],
    [42.7,42.7,7.7,7.7,15.9,15.9,30.6,30.6,19.5,19.5,14.7,14.7,30.5,30.5,43.9,43.9,6,6,7.9,7.9,26.6,26.6,47.2,47.2,0.35,0.35,25.4,25.4,43.6,43.6,34.5,34.5],
    [16.3,16.3,18.3,18.3,19.6,19.6,16.9,16.9,9.5,9.5,13.5,13.5,23.2,23.2,21.2,21.2,22.1,22.1,19.6,19.6,17.5,17.5,24,24,27.2,27.2,2.1,2.1,21,21,9.1,9.1],
    [18.9,18.9,19.4,19.4,17.2,17.2,15.1,15.1,7.2,7.2,11.1,11.1,21.4,21.4,20.8,20.8,19.7,19.7,17.3,17.3,15.7,15.7,23.6,23.6,24.9,24.9,1.6,1.6,20.6,20.6,12.5,12.5],
    [31.9,31.9,37.6,37.6,27.3,27.3,22,22,25.2,25.2,29.3,29.3,25.7,25.7,5.4,5.4,37.9,37.9,35.4,35.4,22.6,22.6,13.7,13.7,43.1,43.1,20,20,1.2,1.2,29.6,29.6],
    [12.7,12.7,27.9,27.9,25.7,25.7,25.8,25.8,15.7,15.7,19.6,19.6,31.3,31.3,32.1,32.1,28.2,28.2,25.7,25.7,27.5,27.5,24.2,24.2,33.3,33.3,9.4,9.4,31.8,31.8,1.6,1.6]
    ] # Matriz de costos, el costo es la distancia en kilometros # Matriz de costos

        self.req =  [
    [16407,16408,4124,4124,4052,4053,3374,3374,3260,3261,2134,2135,1901,1902,1842,1842,1722,1722,1376,1376,1322,1323,1061,1061,642,643,312,313,271,272,249,249],
    [16407,16408,4124,4124,4052,4053,3374,3374,3260,3261,2134,2135,1901,1902,1842,1842,1722,1722,1376,1376,1322,1323,1061,1061,642,643,312,313,271,272,249,249],
    [16407,16408,4124,4124,4052,4053,3374,3374,3260,3261,2134,2135,1901,1902,1842,1842,1722,1722,1376,1376,1322,1323,1061,1061,642,643,312,313,271,272,249,249],
    [16407,16408,4124,4124,4052,4053,3374,3374,3260,3261,2134,2135,1901,1902,1842,1842,1722,1722,1376,1376,1322,1323,1061,1061,642,643,312,313,271,272,249,249],
    [16407,16408,4124,4124,4052,4053,3374,3374,3260,3261,2134,2135,1901,1902,1842,1842,1722,1722,1376,1376,1322,1323,1061,1061,642,643,312,313,271,272,249,249],
    [16407,16408,4124,4124,4052,4053,3374,3374,3260,3261,2134,2135,1901,1902,1842,1842,1722,1722,1376,1376,1322,1323,1061,1061,642,643,312,313,271,272,249,249],
    [16407,16408,4124,4124,4052,4053,3374,3374,3260,3261,2134,2135,1901,1902,1842,1842,1722,1722,1376,1376,1322,1323,1061,1061,642,643,312,313,271,272,249,249],
    [16407,16408,4124,4124,4052,4053,3374,3374,3260,3261,2134,2135,1901,1902,1842,1842,1722,1722,1376,1376,1322,1323,1061,1061,642,643,312,313,271,272,249,249],
    [16407,16408,4124,4124,4052,4053,3374,3374,3260,3261,2134,2135,1901,1902,1842,1842,1722,1722,1376,1376,1322,1323,1061,1061,642,643,312,313,271,272,249,249],
    [16407,16408,4124,4124,4052,4053,3374,3374,3260,3261,2134,2135,1901,1902,1842,1842,1722,1722,1376,1376,1322,1323,1061,1061,642,643,312,313,271,272,249,249]
    ] # Matriz de solicitudes de los clientes

        self.alpha = 0

        self.p = 0.01 #Taza de evaporacion de los caminos de la hormiga

        self.J =  [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31] #Vector de clientes (Municipios que acuden a los modudlos)

        self.I = [0,1,2,3,4,5,6,7,8,9] #Vector de servicios

        self.caminos =[]
        self.caminos_recorridos =[]
        self.costos =[]
        self.visibilidades = []
        self.t = []
        self.probabilidades = []
        self.solucion = [0,1,0,0,2,2,3,3,4,4,5,5,5,6,6,7,7,8,8,9,9,0,0,0,1,1,1,2,2,2,2,2]

    def generaArreglosIniciales(self):
        
        print (".............INICIALIZANDO VARIABLES...........")

        for j in range(len(self.J)):#Vector clientes
            cliente =  []
            clientes_visitados = []
            costo = []
            visibilidad = []
            t_aux = []

            for i in range(len(self.I)):#Vector servicios
                cliente.append(i)
                clientes_visitados.append(-1)
                costo.append(self.req[i][j])
                aux_visibilidad = 1/self.req[i][j]
                visibilidad.append(aux_visibilidad)
                t_aux.append(0.1)

            self.caminos.append(cliente)
            self.caminos_recorridos.append(clientes_visitados)
            self.visibilidades.append(visibilidad)
            self.costos.append(costo)
            self.t.append(t_aux)
            self.probabilidades.append([])

        print("Caminos--",self.caminos)
        print("Visibilidades--",self.visibilidades)
        print("Costo--",self.costos)
        print("Tau--",self.t)
        print("Probabilidades--",self.probabilidades)

        print (".............FIN DE LA INICIALIZACION DE VARIABLES.............")

    def calculaProbabilidades(self):
        
        for j in range(len(self.J)):#Vector clientes
            numerador = []
            for i in range(len(self.I)): #Vector servicios
                numerador.append(self.visibilidades[j][i] * self.t[j][i])
            
            numerador_sum = sum(numerador)
            #print("Numeradores---",numerador)
            #print("Suma numerador---",numerador_sum)

            #Calculando probabilidades
            probabilidad = []
            for i in range(len(numerador)): #Vector ded numeradores
                probabilidad.append(numerador[i]/numerador_sum)
            
            self.probabilidades[j] = probabilidad

        #print("............Actualizando probabilidades............")
        #print(self.probabilidades)
        #print("............Fin de actualización............")

    def calcularFitness(self,individual):
        cap_res = self.cap
        """
            Calcula el fitness de un individuo concreto.
        """
        
        #print("CAP---",self.cap)
        fitness = 0
        #for i in range(len(individual)):
        #    if individual[i] == modelo[i]:
        #        fitness += 1

        for i in range(len(individual)):
            cap_res[individual[i]] = cap_res[individual[i]] - self.req[individual[i]][i]
            #print(cap_res)
            if(cap_res[individual[i]]>0):
                fitness = fitness + 1
                #print (fitness)

        self.cap = [28512,18144,10692,9072,7128,6804,5346,4536,3564,3402] 

        return fitness

    def recorreHormiga(self):
        solucion = [0 for i in range(len(self.J))]
        for j in range(len(self.J)):#Vector clientes
            #for i in range(len(self.I)): #Vector servicios
            aleatorio = random.uniform (0, 1)#Valor entre 0 y 1 porque está normalizado el valor
            #|----P1----|---------P2----------|---P3---|
            #Verificando en cual division de la recta cae el numero aleatorio
            #print("Probabilidades------",self.probabilidades)
            intervalo = self.buscaIntervalo(aleatorio,self.probabilidades[j])
            self.calculaProbabilidades() #Vuelve a calcular la matriz de probabilidades
            #self.probabilidades[j].pop(0)
            
            #Guardando la asignacion con base en la probabilidad calulada

            solucion[j] = intervalo

            #print("aleatorio---",aleatorio)
            #print("XXXXXX||||",intervalo)
        
        #print("aaaaaaaaaaaaaaaaaaaaaaa///",solucion)
        #Calculando el costo de la solucion creda por la hormiga
        costo_solucion = self.calcularFitness(solucion)
        #costo_solucion = 7777777777
        return solucion,costo_solucion 

    def buscaIntervalo(self,aleatorio,arreglo):
        #########################################
        ###Arreglando los intervalos del arreglo de entrada
        #print("Arreglo  de entrada--",arreglo)
        arreglo.insert(0,0.0)
        arreglo.pop()

        for i in range(1,len(arreglo)):
            arreglo[i] = arreglo[i] + arreglo[i-1]
        arreglo.append(1.0)
        #########################################
        ###Terminando de arreglar el arreglo
        #print("Nuevo arreglo--",arreglo)
        

        #print("arreglo////",arreglo)
        posicion = -1
        for i in range(len(arreglo)-1):
            if(arreglo[i] <= aleatorio and aleatorio<= arreglo[i+1]):
                posicion = i
                break
        return posicion                                         

    def actualizaFeromonas(self,vec_soluciones,costos):
        #print("Inicio")
        #print(vec_soluciones)
        #print(costos)
        #Marcando los caminos recorridos
        
        vec_caminos_recorridos = []

        for soluciones in vec_soluciones:
            caminos_recorridos = []
            for j in range(len(self.J)):#Vector clientes
                servicios = []
                for i in range(len(self.I)): #Vector servicios
                    #print("Soluciones j",soluciones[j] )
                    #print("self.caminos[j][i]",self.caminos[j][i] )
                    if(soluciones[j]==self.caminos[j][i]):
                        servicios.append(1)
                    else:
                        servicios.append(0)
                caminos_recorridos.append(servicios)
            vec_caminos_recorridos.append(caminos_recorridos)

        #print("-------------------Caminos recorridos-----------------")
        #print(vec_caminos_recorridos)
        #print("-------------------Caminos recorridos-----------------")

        #CALCULANDO NUMERADOR DE LA ECUACION
        numeradores = []
        for j in range(len(self.J)):#Vector clientes
            vec = []
            for i in range(len(self.I)): #Vector servicios
                aux1 = (1 - self.p) * self.t[j][i]
                vec.append(aux1)
            numeradores.append(vec)

        #CALCULANDO APORTE DE FEROMONAS
        matriz_aporte = []

        hormiga = 0
        for camino in vec_caminos_recorridos:
            aux_hormiga = []
            for i in range(len(camino)):
                vec_aporte = []
                for j in range(len(camino[i])):
                    if(camino[i][j]==0):
                        vec_aporte.append(0)
                    else:
                        aportacion = 1/costos[hormiga]
                        vec_aporte.append(aportacion)
                aux_hormiga.append(vec_aporte)
            matriz_aporte.append(aux_hormiga)
            hormiga +=1

        #Inicializando el nuevo Tao
        nuevo_tao = []
        for i in range(len(self.J)):
            aux = []
            for j in range(len(self.I)):
                aux.append(numeradores[i][j])
            nuevo_tao.append(aux)

        #print("nuevo taooo",nuevo_tao)

        #Calculando el nuevo Tao
        for hormiga in range(len(matriz_aporte)):
            #print("Hormiga///",matriz_aporte[hormiga])
            for i in range(len(matriz_aporte[hormiga])):
                for j in range(len(matriz_aporte[hormiga][i])):
                    nuevo_tao[i][j]=nuevo_tao[i][j]+matriz_aporte[hormiga][i][j]
        
        self.t = nuevo_tao

        '''print("nuevo taooo",nuevo_tao)

        print("")
        print("")
        print("Numeradores---",numeradores)
        print("Aportaciones----",matriz_aporte)
        print("Costos----",costos)'''






hormigas = Hormiga()
hormigas.generaArreglosIniciales()
hormigas.calculaProbabilidades()

num_hormigas = 5
iteraciones =  200
for i in range(iteraciones):
    L = []#Arreglo que guara el costo del camino total de cada hormiga
    soluciones = []
    for m in range(num_hormigas):
        print("")
        cad =  "Hormiga " + str(m+1)+ " incia su camino"
        print(cad)
        
        solucion,costo = hormigas.recorreHormiga()
        

        print("Solución entregada por la hormiga:",solucion)
        print("Costo de la solución entregada por la hormiga:",costo)
        print("")
        L.append(costo)
        soluciones.append(solucion)

    soluciones_fitness = [ (hormigas.calcularFitness(i), i) for i in soluciones]
    print("VECTOR DE SOLUCIONES", soluciones_fitness)

    #Actualizando feromonas
    hormigas.actualizaFeromonas(soluciones,L)
    
