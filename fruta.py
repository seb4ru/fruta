

# Aura León, Denis Arango, Camilo Avedaño, Jostin Abril, Sebastian Gómez


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
    
    print("****************************************************************************************")
    
    while(contador_while != 0):
        
        nombre = input("A continuación ingresará uno por uno el nombres de cada jugador: ")
        if not(len(nombre) != 6):
            jugadores_nombres.append(nombre)
            contador_while = contador_while - 1
        else:
            print("El nickname debe tener 6 caracteres")

    return(jugadores, lanzamiento_i, jugadores_nombres)
    
    print("****************************************************************************************")

datos_basicos = ingreso_de_datos()
#print(datos_basicos)       

#----ORDEN DE JUEGO----

ordenLanzamiento = datos_basicos[1]
ordenLanzamiento.sort(reverse = True)
orden_lanzamiento = {}

for i in range(0, len(ordenLanzamiento)):    
    orden_lanzamiento[ordenLanzamiento[i]] = datos_basicos[2][i-1]

print("****************************************************************************************")
valorInicial = float(input('Ingrese valor de la apuesta inicial acordado por todos los participantes : '))

print("\n*****************************¡AHORA SÍ, EMPECEMOS!**************************************")
print('\nEl orden de juego será el siguiente (dado por el puntaje obtenido en el lanzamiento inicial de dados)):', '\n')

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

# esto no me acuerdo para que es pero funciona

jugador_actual = 0
primer_lanzamiento = 0
segundo_lanzamiento = 0
casino = 0
nueva_mesa = 0
ganancias = 0
ronda_juego = 1
desición = ''
nueva_apuesta = 0


# creando listas para el historial

ronda_juegoLista = []
jugador_actualLista = []
primer_lanzamientoLista = []
desiciónLista = []
segundo_lanzamientoLista = []
gananciasLista = []
casinoLista = []
nueva_apuestaLista = []
mesaLista = []




# historial

while(mesa > 0):

    jugador_actual = datos_basicos[2][ contador_porcentual % datos_basicos[0]-1]

    print("\n-----------------------------------------------------------------------------")
    print('JUGADOR ACTUAL: ', jugador_actual, '\n')
    print(' El valor actual en la mesa es: ', mesa)

    primer_lanzamiento = lanzamientos()

    # lo que sucede sí el jugador saca un número entre 2-5

    if not( primer_lanzamiento == 1 or primer_lanzamiento == 6 ):

        print('\n', 'Dado obtenido en el primer lanzamiento: ', primer_lanzamiento)
        desición = input(' ¿Desea retractarse de su apuesta y pasar al turno siguiente jugador? Y/N: ')

        # el jugador decide si quiere o no saltar turno

        while(not (desición in ['n', 'N', 'y', 'Y'])):
            desición = input(' ¿Desea retractarse de su apuesta y pasar al turno siguiente jugador? Y/N: ')    

        # lo que sucede si el jugador decide NO saltar turno

        if (desición in ["n","N"]):
        
            nueva_apuesta = input(' ¿Desea apostar por un número mayor o un número menor? MAY/MEN: ')
            

            while(not (nueva_apuesta in ['may', 'MAY', 'men', 'MEN'])):
                nueva_apuesta = input(' ¿Desea apostar por un número mayor o un número menor? MAY/MEN: ')

            # bucle por si el jugador apuesta un valor menor al valor inicial

            while(nueva_mesa < valorInicial):
                
                nueva_mesa = float(input('\n Ingrese el nuevo valor a apostar. Recuerde que no puede ser una cantidad menor a la inicial: '))
            
            print('\n')

            mesa = mesa + nueva_mesa # Aquí se le suma a la mesa el valor que el jugador apostó
            print(' El valor actual en la mesa es: ', mesa)
            segundo_lanzamiento = lanzamientos()
            
            # si el jugador apuesta por un número de dado mayor al actual

            if (nueva_apuesta in ['MAY','may']):
    
                # si el jugador gana la apuesta

                if (segundo_lanzamiento > primer_lanzamiento):
    
                    print(' Dado obtenido en el segundo lanzamiento: ', segundo_lanzamiento)
                    print(' El jugador gana, retira lo que aposto')
                    
                    ganancias = mesa * .05
                    casino = casino + ganancias
                    mesa = mesa-(ganancias + (2*nueva_mesa))    
                    
                    print (' Ganancias del casino:' , casino)
                    print(' Nuevo valor en la mesa: ', mesa, '\n')   

                # si el jugador pierde la apuesta

                elif (segundo_lanzamiento < primer_lanzamiento): 
                    
                    print('Dado obtenido en el segundo lanzamiento: ', segundo_lanzamiento)
                    print(' ',jugador_actual, 'pierde su dinero')
                    print(' Nuevo valor en la mesa', mesa, '\n')      

                # si el jugador saca el mismo número en el dado
            
                else:
                
                    print('Dado obtenido en el segundo lanzamiento: ', segundo_lanzamiento)
                    print(' ',jugador_actual, 'pierde turno por lanzar dos tiros iguales y pierde su dinero')
                    print(' Nuevo valor en la mesa', mesa, '\n') 

            # si el jugador apuesta por un número de dado menor al actual

            elif (nueva_apuesta in ['men', 'MEN']):

                    # si el jugador gana la apuesta
                    
                    if (segundo_lanzamiento < primer_lanzamiento):

                        print(' Dado obtenido en el segundo lanzamiento: ', segundo_lanzamiento)
                        print(' El jugador gana, retira lo que aposto')
                        
                        ganancias = mesa*0.05
                        casino = casino + ganancias 
                        mesa = mesa - ( casino + (2*nueva_mesa))
                        
                        print (' Las ganancias del casino son:' , casino)
                        print(' Nuevo valor en la mesa: ', mesa, '\n')  
                    
                    # si el jugador pierde la apuesta

                    elif (segundo_lanzamiento > primer_lanzamiento): 

                        print('Dado obtenido en el segundo lanzamiento: ', segundo_lanzamiento)
                        print(' ',jugador_actual, 'pierde su dinero')
                        print(' Nuevo valor en la mesa', mesa, '\n')     

                    # si el jugador saca el mismo número en el dado

                    else:
                    
                        print(' Dado obtenido en el segundo lanzamiento: ', segundo_lanzamiento)
                        print(' ',jugador_actual, 'pierde turno por lanzar dos tiros iguales y pierde su dinero')
                        print(' Nuevo valor en la mesa', mesa, '\n') 
        
        elif (desición in ['y', 'Y']):
        
            print("siguiente jugador")
                
            

    # lo que sucede sí el jugador saca 1 en el dado

    elif (primer_lanzamiento == 1):

            print(' Dado obtenido: ', primer_lanzamiento)
            print('',jugador_actual, 'pierde turno y da a la mesa el valor de la apuesta inicial')
            mesa = mesa + valorInicial
            print (' Las ganancias del casino son: ', casino)
            print(' Nuevo valor en la mesa', mesa, '\n')


    # lo que sucede sí el jugador saca 6 en el dado

    else:

            print(' Dado obtenido: ', primer_lanzamiento)
            print('',jugador_actual, 'pierde turno pero saca de la mesa el equivalente al valor inicial de la apuesta')
            ganancias = mesa * .05
            mesa = mesa -((2*valorInicial) + mesa * .05)
            casino = casino+ganancias
            print (' Las ganancias del casino son: ', casino)
            print(' El nuevo valor en la mesa es: ', mesa, '\n')

    ronda_juegoLista.append(ronda_juego)
    jugador_actualLista.append(jugador_actual)
    primer_lanzamientoLista.append(primer_lanzamiento)
    desiciónLista.append(desición)
    segundo_lanzamientoLista.append(segundo_lanzamiento)
    gananciasLista.append(round(ganancias,1))
    casinoLista.append(round(casino ,1))
    nueva_apuestaLista.append(nueva_apuesta)
    mesaLista.append(round(mesa, 1))

    
    nueva_apuesta = ''
    segundo_lanzamiento = 0
    

        
    print('\n')

    ronda_juego = ronda_juego + 1
    contador_porcentual = contador_porcentual+ 1

    # Cierre del cilco while

def genhistorial():

    print("| Ronda | Jugador | Primer lanzamiento | Desición | Segundo lanzamiento | Ganancias casino(en la ronda) | Ganancias casino | valor en la mesa |")  
      
    for i in range(1, ronda_juego):
        print("-----------------------------------------------------------------------------------------------------------------------------------")
        print('   ',ronda_juegoLista[i-1], '    ', jugador_actualLista[i-1], '        ', primer_lanzamientoLista[i-1], '              ', desiciónLista[i-1], '              ', segundo_lanzamientoLista[i-1], '                     ', gananciasLista[i-1], '                        ', casinoLista[i-1], '          ', mesaLista[i-1])

print('LA MESA HA QUEDADO CON $0. JUEGO TERMINADO')

imprimir = input("¿Desea ver el historial de la partida? y/n")
    
if (imprimir in ['y', 'Y']):
    print('\n')
    print("Si en la columna desición no hay nada es porque el jugador sacó el dado 1 o 6 ")
    print('\n')
    genhistorial()




