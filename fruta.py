from code import interact
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
        print('\n')
        contador_while = contador_while - 1

    return(jugadores, lanzamiento_i, jugadores_nombres)

datos_basicos = ingreso_de_datos()
print(datos_basicos)       

#----ORDEN DE JUEGO----


    # aquí meter un diccionario para el orden de los jugadores

ordenLanzamiento = datos_basicos[1]
ordenLanzamiento.sort(reverse = True)
orden_lanzamiento = {}

for i in range(0, len(ordenLanzamiento)):
    
    orden_lanzamiento[ordenLanzamiento[i]] = datos_basicos[2][i-1]

print(orden_lanzamiento, '\n')

valorInicial = float(input('Ingrese valor de la apuesta inicial acordado por todos los participantes : '))

print('\n¡AHORA SÍ, EMPECEMOS!\n')
print('El orden de juego será el siguiente (dado por el puntaje obtenido en el lanzamiento inicial de dados)):', '\n')
print('\n')

x = 1

for i in range(1, datos_basicos[0] + 1):
    
    print('Jugador ', x ,orden_lanzamiento[ordenLanzamiento[i-1]], 'con un puntaje inicial de dados :', ordenLanzamiento[i-1])
    x = x + 1

print('\n')
print("Total de jugadores:", datos_basicos[0])
print("Apuesta inicial:", valorInicial)

#----IMPRESIÓN DE RESULTADOS----


#----CONDICIONES DEL JUEGO----


mesa = datos_basicos[0] * valorInicial
    
print('\nMesa: ', mesa)
print('Jugador\n', )
    

    
def lanzamientos():
    
    return (random.randint(1, 6)) # Caras del dado
    


contador_porcentual = 0


print(orden_lanzamiento)

del ordenLanzamiento

ordenLanzamiento = []

for i in orden_lanzamiento:
    ordenLanzamiento.append(orden_lanzamiento[i])


print(ordenLanzamiento,'\n')



while(mesa != 0):

    jugador_actual = datos_basicos[2][ contador_porcentual % datos_basicos[0]-1]
    print('Jugador actual: ', jugador_actual)
    print(' El valor actual en la mesa es: ', mesa)

    lanzamiento_actual = lanzamientos()

    if not( lanzamiento_actual == 1 or lanzamiento_actual == 6 ):
        
        print(' Dado obtenido: ', lanzamiento_actual)
    
    elif (lanzamiento_actual == 1):
        
        print(' Dado obtenido: ', lanzamiento_actual)
        print(' ',jugador_actual, 'pierde turno y da a la mesa el valor de la apuesta inicial')
        
        mesa = mesa + valorInicial
        print(' Nuevo valor en la mesa', mesa, '\n')
    
    else:

        print(' Dado obtenido: ', lanzamiento_actual)
        print(' ',jugador_actual, 'pierde turno pero saca de la mesa el equivalente al valor inicial de la apuesta')

        mesa = mesa -(valorInicial + mesa*0.05)
        print(' El nuevo valor en la mesa es: ', mesa, '\n')
    
    # este input es para que el código en el momento se pare para ver los datos obtenidos o algo así, luego se quita y se modifica o algo gdygkl
    input(" pasar al siguiente jugador")
    print('\n')

    contador_porcentual = contador_porcentual + 1




































