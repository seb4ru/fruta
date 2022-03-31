import random

#----SOLICITAR CANTIDAD DE JUGADORES----

def ingreso_de_datos():
    
    # jugadores = número de jugadores
    # lanzamiento_i = dado
    # jugadores_nombres = nombres de los jugadores

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

#----IMPRESIÓN DE RESULTADOS----


for i in range(1, datos_basicos[0]+1):
      print('\n',datos_basicos[2][i-1],' sacó', datos_basicos[1][i-1],'  en el puntaje inicial de dados')

#----ORDEN DE JUEGO----


    # aquí meter un diccionario para el orden de los jugadores

ordenLanzamiento = datos_basicos[1]
ordenLanzamiento.sort(reverse = True)
orden_lanzamiento = {}

print(ordenLanzamiento)


for i in range(0, len(ordenLanzamiento)):
    
    orden_lanzamiento[ordenLanzamiento[i]] = datos_basicos[2][i-1]

print(orden_lanzamiento, '\n')

print('El orden de juego será el siguiente (dado por el puntaje obtenido en el lanzamiento inicial de dados)):', '\n')

x = 1


for i in range(1, datos_basicos[0] + 1):
    
    print('Jugador ', x ,orden_lanzamiento[ordenLanzamiento[i-1]])
    x = x + 1

print('¡AHORA SÍ, EMPECEMOS!')

valorInicial = float(input('Ingrese valor de la apuesta inicial acordado por todos los participantes : '))

print("Jugadores:", datos_basicos[0])
print("Apuesta inicial:", valorInicial)

#----CONDICIONES DEL JUEGO----


#def lanzamientos(jugadores):
#    lanzamiento = [random.randint(1, (6 * 1)) for _ in range(jugadores)]
#    if lanzamiento == 1:
#        print('Pierde turno')
#    elif lanzamiento == 6:

#        decisición = input(
#            'Desea retractarse de su apuesta y pasar al turno siguiente? Y/N')

#        while decisición != 'N':

#            if decisición == 'Y':
#                print('yes')
#            else:
#                print('Decisión inválida')
#        segundoLanzamiento = [random.randint(
#            1, (6 * 1)) for _ in range(jugadores)]


#Juego
#def juego(mesa):
                      



def lanzamientos(jugadores, valorInicial):
    
    mesa = jugadores * valorInicial
    
    print('\nMesa: ', mesa)
    print('Jugador\n', )
    
    lanzamiento = random.randint(1, (6 * 1))
    
    print('Primer Lanzamiento: ', lanzamiento)
    
    for _ in range(jugadores-1):

        if lanzamiento == 1:
            print('Pierde turno')
        elif lanzamiento == 6:
            print('Gano la apuesta mínima')
            mesa = mesa-valorInicial
            print('Mesa: ', mesa)

        else:

            decisición = input('Desea retractarse de su apuesta y pasar al turno siguiente jugador? Y/N: ')
            
            if decisición == 'N':
                nuevaApuesta = input('¿Desea apostar por un número mayor o menor? Y/N: ')
                if nuevaApuesta == 'Y':
                    desicionNuevaApuesta = input('¿Mayor o menor?: ')

                    segundoLanzamiento = random.randint(1, (6 * 1))
                    print(segundoLanzamiento)

                    if desicionNuevaApuesta == 'Mayor':
                        if segundoLanzamiento > lanzamiento:
                            print('El jugador gana, retira lo que aposto')
                            mesa = mesa-valorInicial
                            print('Mesa: ', mesa)
                        else: 
                            print('El jugador pierde, debe colocar lo que aposto')
                            mesa = mesa+valorInicial
                            print('Mesa: ', mesa)
                    elif desicionNuevaApuesta == 'Menor':
                        if segundoLanzamiento < lanzamiento:
                            print('El jugador gana, retira lo que aposto')
                            mesa = mesa-valorInicial
                            print('Mesa: ', mesa)
                        else: 
                            print('El jugador pierde, debe colocar lo que aposto')
                            mesa = mesa+valorInicial
                            print('Mesa: ', mesa)
                    else:
                            print('Tiros iguales, pierde turno')
                            print('Mesa: ', mesa)

            elif decisición == 'Y':
                print('Siguiente jugador')
                lanzamiento = random.randint(1, (6 * 1))
                print('Primer Lanzamiento: ', lanzamiento)                    
            else:
                print('ERROR. Decisión inválida')

lanzamientos(datos_basicos[0], valorInicial)
