import random

#----SOLICITAR CANTIDAD DE JUGADORES----

def ingreso_de_datos():
    jugadores = int(input("Ingrese la cantidad de jugadores:"))
    lanzamiento_i = [random.randint(1, (30 * 1)) for _ in range(jugadores)]
    return(jugadores, lanzamiento_i)

datos_basicos = ingreso_de_datos()
print(datos_basicos[0])
print(datos_basicos[1])
print(datos_basicos)       

#----IMPRESIÓN DE RESULTADOS----

for i in range(1, datos_basicos[0]+1):
    print('Jugador', i, ':', datos_basicos[1][i-1],"\n")

#----ORDEN DE JUEGO----

ordenLanzamiento = sorted(datos_basicos[1], reverse=True)
print('El orden de juego será el siguiente (dado por el puntaje obtenido en el lanzamiento inicial de dados)):', ordenLanzamiento, '\n')

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
    print('Primer jugador\n')
    
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
