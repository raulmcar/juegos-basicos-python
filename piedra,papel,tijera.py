import random

'''He hecho estas variables para poder manejarlas mas comodamente y poder ver con claridad los
valores de la maquina y del jugador. Se almacenan las jugadas de las dos partes aqui'''
jugada_jugador = None
jugada_maquina = None

def obtener_eleccion_persona():
    '''En esta función se almacena la jugada del jugador. Inicializo jugada valida en false por si
    el jugador me mete una jugada que no este registrada entre las validas'''
    global jugada_jugador
    jugada_valida = False
    
    while jugada_valida == False:
        '''En este bucle while es donde se pide la variable jugada al usuario. Si la variable jugada
        entra dentro de las jugadas validas, el bucle termina y la variable global jugada_jugador sera la que
        ha introducido el usuario. Si la jugada no fuese valida, se imprime por pantalla y la vuelve a pedir'''
        jugada = input("Dime que jugada quieres hacer (piedra/papel/tijera): ")
        if jugada == 'piedra' or jugada == 'papel' or jugada == 'tijera':
            jugada_valida == True
            jugada_jugador = jugada
            break
        else:
            print("Esa jugada no es valida")

def obtener_eleccion_computadora():
    '''Esta es la funcion donde se genera la jugada de la maquina. Usamos la variable global para
    que se almacene fuera y tener mayor comodidad a la hora de manejar ese resultado'''
    global jugada_maquina
    
    opciones = ["piedra", "papel", "tijera"]
    jugada_maquina = random.choice(opciones)

def comprobar_jugada():
    '''Se revisan todas las posibilidades. Siempre se muestra la eleccion de la maquina.
    Si la jugada del jugador y de la maquina es la misma, se imprime empate. Si la jugada del 
    jugador esta en una de las posibilidades ganadoras, se imprime como gana el jugador. En el resto
    de posibilidades posibles que no son las anteriores, se imprime que gana la maquina'''
    if jugada_jugador == jugada_maquina:
        print(f"La maquina ha elegido {jugada_maquina}. Es un empate!")
    elif jugada_jugador == 'piedra' and jugada_maquina == 'tijera':
        print(f"La maquina ha elegido {jugada_maquina}. El jugador ha ganado!")
    elif jugada_jugador == 'tijera' and jugada_maquina == 'papel':
        print(f"La maquina ha elegido {jugada_maquina}. El jugador ha ganado!")
    elif jugada_jugador == 'papel' and jugada_maquina == 'piedra':
        print(f"La maquina ha elegido {jugada_maquina}. El jugador ha ganado!")
    else:
        print(f"La maquina ha elegido {jugada_maquina}. La maquina ha ganado!")

def piedra_papel_tijera():
    '''Primero se incializa preguntando si quieres jugar o no para controlar cuando quieres dejar de jugar.
    Si la opcion es si, se inicia el juego y se llama a las funciones, primero el movimiento del jugador, luego
    se genera la jugada de la maquina y por ultimo se comprueba la jugada. Si la respuesta es no se termina
    el juego, y si se intenta introducir alguna otra opcion se imprime que no es una opcion valida'''
    while True:
        opcion = input("Bienvenido! Quieres jugar? (si/no)")
        if opcion == 'si':
            obtener_eleccion_persona()
            obtener_eleccion_computadora()
            comprobar_jugada()
        elif opcion == 'no':
            break
        else:
            print("No es una opcion valida, prueba otra vez")

'''Se invoca la funcion que te permite jugar al juego'''
piedra_papel_tijera()