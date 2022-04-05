import random

#----SOLICITAR CANTIDAD DE JUGADORES----

def ingreso_de_datos():
    
    # jugadores = número de jugadores                   0
    # lanzamiento_i = número de dado                    1
    # jugadores_nombres = nombres de los jugadores      2

    jugadores = int(input("Ingrese la cantidad de jugadores:"))
    lanzamiento_i = []

    while(len(lanzamiento_i) < jugadores):
        j = random.randint(1, (30 * 1))
            
        if not(j in lanzamiento_i):            
            lanzamiento_i.append(j)

        jugadores_nombres = []
        contador_while = jugadores
    
    
    while(contador_while != 0):
        
        jugadores_nombres.append(input("A continuación ingresará uno por uno el nombres de cada jugador: "))
        contador_while = contador_while - 1

    return(jugadores, lanzamiento_i, jugadores_nombres)

datos_basicos = ingreso_de_datos()
#print(datos_basicos)       

#----ORDEN DE JUEGO----

ordenLanzamiento = datos_basicos[1]
ordenLanzamiento.sort(reverse = True)
orden_lanzamiento = {}

for i in range(0, len(ordenLanzamiento)):    
    orden_lanzamiento[ordenLanzamiento[i]] = datos_basicos[2][i-1]


valorInicial = float(input('Ingrese valor de la apuesta inicial acordado por todos los participantes : '))
print('\n¡AHORA SÍ, EMPECEMOS!\n El orden de juego será el siguiente (dado por el puntaje obtenido en el lanzamiento inicial de dados)):', '\n')
print('\n')

x = 1

for i in range(1, datos_basicos[0] + 1):
    
    print('Jugador ', x ,orden_lanzamiento[ordenLanzamiento[i-1]], 'con un puntaje inicial de dados :', ordenLanzamiento[i-1])
    x = x + 1

print('\n')
print("Total de jugadores:", datos_basicos[0])
print("Apuesta inicial:", valorInicial)


#----CONDICIONES DEL JUEGO----

mesa = datos_basicos[0] * valorInicial    
print('\nMesa: ', mesa)
    
def lanzamientos():    
    return (random.randint(1, 6)) # Caras del dado
    
#---JUEGO---
contador_porcentual = 0

del ordenLanzamiento
ordenLanzamiento = []
for i in orden_lanzamiento:
    ordenLanzamiento.append(orden_lanzamiento[i])

casino = 0
nueva_mesa = 0
ganancias = 0
ganancias1 = 0

while(mesa > 0):

    jugador_actual = datos_basicos[2][ contador_porcentual % datos_basicos[0]-1]
    print('JUGADOR ACTUAL: ', jugador_actual)
    print(' El valor actual en la mesa es: ', mesa)

    lanzamiento_actual = lanzamientos()

    if not( lanzamiento_actual == 1 or lanzamiento_actual == 6 ):

        print(' Dado obtenido en el primer lanzamiento: ', lanzamiento_actual)
        decisición = input(' ¿Desea retractarse de su apuesta y pasar al turno siguiente jugador? Y/N: ')
        
        if (decisición in ["n","N"]):
        
            nueva_apuesta = input(' ¿Desea apostar por un número mayor o un número menor? MAY/MEN: ')
            
            while(nueva_mesa < valorInicial):

                nueva_mesa = float(input(' \nIngrese el nuevo valor a apostar. Recuerde que no puede ser una cantidad menor a la inicial: '))

            mesa = mesa + nueva_mesa #Aquí se le suma a la mesa el valor que el jugador apostó
            print(' El valor actual en la mesa es: ', mesa)
            segundo_lanzamiento = lanzamientos()            
            
            if (nueva_apuesta == 'MAY'):
        
                    if (segundo_lanzamiento > lanzamiento_actual):
        
                        print(' Dado obtenido en el segundo lanzamiento: ', segundo_lanzamiento)
                        print(' El jugador gana, retira lo que aposto')
                       
                        ganancias1 = mesa * .05
                        casino = casino + ganancias1
                        mesa = mesa-(ganancias1 + nueva_mesa)    
                       
                        print ('Ganancias del casino:' , casino)
                        print(' Nuevo valor en la mesa: ', mesa, '\n')   

                    elif (segundo_lanzamiento < lanzamiento_actual): 
                        
                        print('Dado obtenido en el segundo lanzamiento: ', segundo_lanzamiento)
                        print(' ',jugador_actual, 'pierde su dinero')
                        print(' Nuevo valor en la mesa', mesa, '\n')      
                    
                    else:
                    
                        print('Dado obtenido en el segundo lanzamiento: ', segundo_lanzamiento)
                        print(' ',jugador_actual, 'pierde turno por lanzar dos tiros iguales y pierde su dinero')
                        print(' Nuevo valor en la mesa', mesa, '\n') 
            
            elif (nueva_apuesta == 'MEN'):
            
                    if (segundo_lanzamiento < lanzamiento_actual):

                        print(' Dado obtenido en el segundo lanzamiento: ', segundo_lanzamiento)
                        print(' El jugador gana, retira lo que aposto')
                        
                        ganancias = mesa*0.95
                        casino = casino + ganancias 
                        mesa = mesa - ( casino + nueva_mesa )
                        
                        print ('Las ganancias del casino son:' , casino)
                        print(' Nuevo valor en la mesa: ', mesa, '\n')  
                    
                    elif (segundo_lanzamiento > lanzamiento_actual): 

                        print('Dado obtenido en el segundo lanzamiento: ', segundo_lanzamiento)
                        print(' ',jugador_actual, 'pierde su dinero')
                        print(' Nuevo valor en la mesa', mesa, '\n')     
                    
                    else:
                    
                        print(' Dado obtenido en el segundo lanzamiento: ', segundo_lanzamiento)
                        print(' ',jugador_actual, 'pierde turno por lanzar dos tiros iguales y pierde su dinero')
                        print(' Nuevo valor en la mesa', mesa, '\n') 
        
        elif decisición == 'Y':
        
                print('SIGUIENTE JUGADOR')            
                continue

    elif (lanzamiento_actual == 1):

            print(' Dado obtenido: ', lanzamiento_actual)
            print(' ',jugador_actual, 'pierde turno y da a la mesa el valor de la apuesta inicial')
            mesa = mesa + valorInicial
            print ('Las ganancias del casino son: ', casino)
            print(' Nuevo valor en la mesa', mesa, '\n')

    else:

            print(' Dado obtenido: ', lanzamiento_actual)
            print(' ',jugador_actual, 'pierde turno pero saca de la mesa el equivalente al valor inicial de la apuesta')
            mesa = mesa -((2*valorInicial) + mesa*0.05)
            ganancias2 = mesa - mesa*0.95
            casino = casino+ganancias2
            print(' El nuevo valor en la mesa es: ', mesa, '\n')
            print ('Las ganancias del casino son: ', casino)
                                    
    if (mesa <= 0):
        mesa = 0
        
    print('\n')

    contador_porcentual = contador_porcentual + 1

    # Cierre del cilco while
        


print('LA MESA HA QUEDADO CON $0. JUEGO TERMINADO')
print ('GANANCIAS TOTALES DEL CASINO: ', casino)


#def historial():
#Función que muestra el historial
#....

#historial = print(¿Desea conocer el historial de juego? Y/N): ---Aquí se pregunta si quiere conocer o no el historial---
#    if historial = 'Y':
#        historial()
#    else: