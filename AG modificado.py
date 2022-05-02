import random

class AG:
    #######################################################################
    #######################################################################
    #######################################################################
    #PARAMETROS DEL PROBLEMA 8 X 3
    #J = [0,1,2,3,4,5,6,7] #Vector de clientes
    #n = len(J) #Numero de clientes

    #I = [0,1,2] #Vector de servicios
    #m = len(I) # Numero de servicios

    #######################################################################
    #######################################################################
    #######################################################################

    #modelo = [1,1,1,1,1,1,1,1] #Objetivo a alcanzar
    
    #print("\n\nModelo: %s\n"%(modelo)) #Mostrar el modelo, con un poco de espaciado
    
    def __init__(self):
        self.largo = 8 #La longitud del material genetico de cada individuo
        self.num = 10 #La cantidad de individuos que habra en la poblacion
        self.pressure = 3 #Cuantos individuos se seleccionan para reproduccion. Necesariamente mayor que 2
        self.mutation_chance = 0.2 #La probabilidad de que un individuo mute
        self.iteraciones = 300

        self.min = 0
        self.max = 2

        self.cap = [160,90,70] #Capacidad de los servicios Q

        self.c = [[10,11,12,13,14,15,16,17]
            ,[22,24,26,28,30,32,34,36],
            [60,64,68,72,76,80,84,88]] # Matriz de costos


        self.req =  [[48,47,46,45,44,43,42,41],
            [38,37,36,35,34,33,32,31],
            [28,27,26,25,24,23,22,21]] # Matriz de solicitudes de los clientes

    def individual(self,min, max):
        """
            Crea un individual
        """
        return[random.randint(min, max) for i in range(self.largo)]
    
    def crearPoblacion(self):
        """
            Crea una poblacion nueva de individuos
        """
        return [self.individual(self.min,self.max) for i in range(self.num)]
    
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

        self.cap = [160,90,70]

        return fitness
    
    def selection_and_reproduction(self,population):
        """
            Puntua todos los elementos de la poblacion (population) y se queda con los mejores
            guardandolos dentro de 'selected'.
            Despues mezcla el material genetico de los elegidos para crear nuevos individuos y
            llenar la poblacion (guardando tambien una copia de los individuos seleccionados sin
            modificar).
    
            Por ultimo muta a los individuos.
    
        """
        print("calculando fitness")
        puntuados = [ (self.calcularFitness(i), i) for i in population] #Calcula el fitness de cada individuo, y lo guarda en pares ordenados de la forma (5 , [1,2,1,1,4,1,8,9,4,1])
        puntuados = [i[1] for i in sorted(puntuados)] #Ordena los pares ordenados y se queda solo con el array de valores
        population = puntuados
    
    
    
        selected =  puntuados[(len(puntuados)-self.pressure):] #Esta linea selecciona los 'n' individuos del final, donde n viene dado por 'pressure'
    
    
    
        #Se mezcla el material genetico para crear nuevos individuos
        for i in range(len(population)-self.pressure):
            punto = random.randint(1,self.largo-1) #Se elige un punto para hacer el intercambio
            padre = random.sample(selected, 2) #Se eligen dos padres
            
            population[i][:punto] = padre[0][:punto] #Se mezcla el material genetico de los padres en cada nuevo individuo
            population[i][punto:] = padre[1][punto:]
    
        return population #El array 'population' tiene ahora una nueva poblacion de individuos, que se devuelven
    
    def mutation(self,population):
        """
            Se mutan los individuos al azar. Sin la mutacion de nuevos genes nunca podria
            alcanzarse la solucion.
        """
        for i in range(len(population)-self.pressure):
            if random.random() <= self.mutation_chance: #Cada individuo de la poblacion (menos los padres) tienen una probabilidad de mutar
                punto = random.randint(0,self.largo-1) #Se elgie un punto al azar
                nuevo_valor = random.randint(self.min,self.max) #y un nuevo valor para este punto
    
                #Es importante mirar que el nuevo valor no sea igual al viejo
                while nuevo_valor == population[i][punto]:
                    nuevo_valor = random.randint(self.min,self.max)
    
                #Se aplica la mutacion
                population[i][punto] = nuevo_valor
    
        return population
      

algoritmo = AG()
population = algoritmo.crearPoblacion()#Inicializar una poblacion
print("Poblacion Inicial:\n%s"%(population)) #Se muestra la poblacion inicial
  
  
#Se evoluciona la poblacion
for i in range(algoritmo.iteraciones):
    population = algoritmo.selection_and_reproduction(population)
    population = algoritmo.mutation(population)
  
  
print("\nPoblacion Final:\n%s"%(population)) #Se muestra la poblacion evolucionada
factibles = [ (algoritmo.calcularFitness(i), i) for i in population] #Calcula el fitness de cada individuo, y lo guarda en pares ordenados de la forma (5 , [1,2,1,1,4,1,8,9,4,1])
print("Factibles: ",factibles)
print("\n\n")
input("Esperando")