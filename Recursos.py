# Clase de los recursos utilizados en la ejecución del código
from os import system, name # importa solo system desde os
from time import sleep # importa sleep para mostrar una salida por algún periodo de tiempo
from Mazo import Mazo
from Jugador import Jugador
from Banca_IA import Banca

def limpiar_consola(): # Método para limpiar la consola en cada sistema operativo
    if name == "nt": _ = system("cls") # for windows
    else: _ = system("clear") # for mac, android, linux

def mostrar_cargando(duracion): # Muestra una barra de carga
    for x in list(range(duracion)):
        print(end="#", flush=True)
        sleep(0.05)

def recibir_eleccion_num(num_opciones): # Recibe una elección de cualquien menú con opciones numericas (parametro: número de opciones)
    while True: # Fuerza que la entrada esté entre las opciones
        try: # Fuerza que la entrada se un número entero
            eleccion = int(input(">> ")) # Toma la entrada
            if eleccion in range(1, num_opciones+1): # Verifica que la entrada esté en el rango de opciones
                break
            else: print("Intente nuevamente...")
        except (ValueError):
            print("ERROR!")
            continue
    return eleccion

def recibir_eleccion_str(): # Recibe una elección de cualquier menú con opciones alfanumericas (Sí/no)
    while True: # Mientras no haya una entrada valida...
        eleccion = input(">> ") # ... Recibe una entrada
        eleccion.lower() # Convierte a minuscúlas
        if eleccion == "y" or eleccion == "si" or eleccion == "n" or eleccion == "no": # Chequea que la elección sea valida
            break
        else: # Sino toma la entrada nuevamente
            print("Intente nuevamente...")
            continue
    return eleccion

def mostrar_menu_princ(): # Muestra el menú principal
    limpiar_consola()
    print(
    """        + ------------------ 7 y un cachito ----------------- +
        + 1. Iniciar un nuevo juego.                          +
        + 2. Ver puntajes.                                    +
        + 3. Salir.                                           +
        +                                                     +
        + Ingrese el número correspondiente a la elección...  +
        + --------------------------------------------------- +""" + "\n")

def mostrar_menu_juego(): # Muestra el menú de elección del número de jugadores
    mostrar_cargando(40)
    limpiar_consola()
    print("""
    + ----------- ¿Cuántas personas se unirán a la mesa? ----------- +
    +  1 jugador      2 jugadores      3 jugadores     4 jugadores   +
    + -------------------------------------------------------------- +
    """)

def recibir_nombre(jugador_en_turno): # Recibe el nombre del jugador en turno (El nombre es retornado para ser almacenado en una variable)
    limpiar_consola()
    print(
        """
    + ----------- ¿Cuál es el nombre del jugador {} ------------ +
    + --------------------------------------------------------- +
        """.format(str(jugador_en_turno)))
    nombre = input(">> ")
    return nombre

def mezclar_mazo(): # Muestra un mensaje y una barra de carga antes de iniciar el juego
    limpiar_consola()
    print(
        """
    + ---------------------------------------------------- +
    + --------- el mazo está siendo mezclado... ---------- +
    + ---------------------------------------------------- +""")
    mostrar_cargando(40)

def mostrar_jugador_actual(nombre): # Indica quien está jugando en el turno en ejecución
    limpiar_consola()
    print(
        """
        + ---------------------------------------------------- +
                Es el turno de + --- {} --- +""".format(str(nombre)))

def mostar_carta(carta): # Muestra cuál es la carta que recibe el jugador en turno
    print(
        """\t+ ---------------------------------------------------- +
        + --- La banca se prepara para quitar una carta... --- +
        """)
    sleep(3.0)
    print(
        """
        + ---------- La banca te ha entregado un: ------------ +
        + ---------------------------------------------------- +
                |---------------|
                | {}            
                |               |
                |               |
                |               |
                |               |
                |               |
                |               |
                |               |
                |_______________|
        + ---------------------------------------------------- +""".format(carta))
    
def mostrar_puntaje(puntaje): # Muestra el puntaje del jugador en turno
    print(
        """
        + ---------------------------------------------------- +
        +               Tu puntaje actual es: {}
        + ---------------------------------------------------- +""".format(puntaje))

def mostar_menu_plantar(): # Muestra el menú para plantarse al jugador en turno
    print(
        """
        + ---------------------------------------------------- +
        + ------------------- ¿Te plantas? ------------------- +
        +              Sí/no                  y/n              +
        + ---------------------------------------------------- +""")

def chequear_jugador_pasado(puntuacion_actual): # Chequea si el jugador se ha pasado la puntuación límite
    if puntuacion_actual > 7.5: # Si la puntuación supera los 7.5 puntos se considera que el jugador se pasó
        return True
    else: return False

def mostrar_jugador_pasado(nombre): # Muestra un mensaje al jugador en turno en caso de que pase la puntuación límite
    print(
        """
        + -------------- Te pasaste, lo siento --------------- +
        + -------- Es el turno del siguiente jugador --------- +
        + ---------------------------------------------------- +""")
    sleep(5.0)

def mostrar_banca_pasada(): # Muestra un mensaje cuando la banca sobre pasa la puntuación límite
    print(
        """
        + --------------- La banca se pasó... ---------------- +
        + ---------------------------------------------------- +""")
    sleep(5.0)

def mostar_banca_plantada(): # Muestra un mensaje cuando la banca se planta
    print(
        """
        + -------------- La banca se plantó... --------------- +
        + ---------------------------------------------------- +""")
    sleep(5.0)

def mostrar_banca_continua(): # Muestra un mensaje cuando la banca continua jugando
    print(
        """
        + ------------ La banca continua jugando ------------- +
        + ---------------------------------------------------- +""")
    sleep(5.0)

def mostrar_resultados(jugadores, banca): # Muestra los resultados despúes de que todos hayan jugado
    limpiar_consola()
    print(
        """
        + ---------------------------------------------------- +
        + -------------- Resultados de la mesa --------------- +""")
    sleep(2.0)
    for jugador in jugadores: # Por cada jugador...
        if jugador.puntuacion <= 7.5: # Si la puntuación es menor o igual a 7.5 (No se pasó)
            print("\t+", jugador.nombre + ": {} puntos".format(jugador.puntuacion)) # Muestra la puntuación
            sleep(1.0)
        else: # Sino...
            print("\t+", jugador.nombre + ": ¡Pasado(a)!") # Muestra al jugador como pasado o pasada
            sleep(1.0)
    if banca.puntuacion <= 4.5: # Si la puntuación es menor o igual a 7.5 (No se pasó)
        print("\t+ Banca:", banca.puntuacion, "puntos") # Muestra la puntuación
        print("\t+ ---------------------------------------------------- +")
    else: # Sino...
        print("\t+ Banca: ¡Pasada!")  # Muestra a la banca como pasada
        print("\t+ ---------------------------------------------------- +")
    sleep(10.0)

def buscar_mayor_puntuacion(jugadores): # Busca el jugador con la puntuación más alta
    jugadores_mayor_puntuacion = [] # Lista de jugadores con la mayor puntuación (en caso de que dos tengan la mayor puntuación)
    puntuacion_mayor_jugadores = 0.0 # 
    for jugador in jugadores: # Por cada jugador...
        if jugador.puntuacion <= 7.5: # ... Si la puntuación del jugador es menor o igual a 7.5 (No se pasó) y...
            if jugador.puntuacion >= puntuacion_mayor_jugadores: # ... Si la puntuación del jugador es la mayor entre todos
                jugadores_mayor_puntuacion.append()

def mostrar_ganador(jugadores, banca):
    puntuacion_mayor_jugadores = 0
    for jugador in jugadores: # Por cada jugador...
        if jugador.puntuacion <= 7.5: # ... Si la puntuación del jugador es menor o igual a 7.5 (No se pasó) y...
            if jugador.puntuacion >= puntuacion_mayor_jugadores: # ... Si la puntuación del jugador es la mayor entre todos
                puntuacion_mayor_jugadores = jugador.puntuacion
            
    

def iniciar_juego(): # 
    mostrar_menu_juego() # Muestra el menú de elección del número de jugadores
    eleccion_num = recibir_eleccion_num(4) # Toma una elección de 1 a 4 jugadores
    mazo = Mazo() # Crea un mazo de cartas
    mezclar_mazo() # Muestra un mensaje para indicar que el juego está apunto de inciar
    jugadores = [] # Lista para guardar los jugadores y su información

    for i in range(1, eleccion_num+1): # Ciclo que controla los turnos de cada jugador
        nombre = recibir_nombre(i) # Muestra un mensaje en el que se toma el nombre (str) del jugador en turno
        exec("jugador{0} = Jugador('{1}')".format(i, nombre)) # Crea una instancia de la clase Jugador...
        # ... ]Para cada jugador siempre que haya iniciado su turno (Los nombre de las instancias son jugador1, jugador2, jugador3 ... jugador(n))
        # En la instancia del jugador en turno se guarda información de su nombre
        exec("jugadores.append(jugador{})".format(i)) # Guarda cada instancia en la lista jugadores[]
        puntuacion = 0 # Puntuación inicial de cada jugador
        while True: # Ciclo que controla la ejecucción del turno
            nombre = jugadores[i-1].nombre # Guarda el nombre el jugador en turno (Posiblemente se pueda eliminar)
            mostrar_jugador_actual(nombre) # Muestra el nombre del jugador en turno
            carta = mazo.tomar_carta() # Guarda una carta del mazo en la variable carta
            mostar_carta(carta) # Muestra la carta que recibe el jugador en turno
            puntuacion += mazo.tomar_valor_carta(carta) # Suma el valor de la carta del jugador a su puntuación
            mostrar_puntaje(puntuacion) # Muestra el puntaje que ha acumulado el jugador en turno
            if chequear_jugador_pasado(puntuacion) == True: # Valida si el jugador sobrepasó la puntuación límite
                mostrar_jugador_pasado(i) # Muestra un mensaje indicando que el jugador sobrepasó la puntuación límite
                jugadores[i-1].puntuacion = puntuacion # Guarda la puntuación del jugador en turno
                break
            else: # En caso de que no haya sobrepasado la puntuación límite...
                mostar_menu_plantar() # Muestra un menú en el que el jugador en turno decide si plantar
                eleccion_str = recibir_eleccion_str() # Recibe la elección del jugador
                if eleccion_str == "y" or eleccion_str == "si": # Si la elección es plantarse...
                    jugadores[i-1].puntuacion = puntuacion # Guarda la puntuación del jugador en turno
                    break
                else: continue # Si la elección es NO plantarse continua jugando
    
    puntuacion = 0
    banca = Banca()
    while True:
        mostrar_jugador_actual("La banca") # Inicia el turno de la banca
        carta = mazo.tomar_carta() # Guarda una carta del mazo en la variable carta
        mostar_carta(carta) # Muestra la carta que recibe la banca
        puntuacion += mazo.tomar_valor_carta(carta) # Suma el valor de la carta de la banca a su puntuación 
        mostrar_puntaje(puntuacion) # Muestra el puntaje que ha acumulado la banca
        if chequear_jugador_pasado(puntuacion) == True: # Valida si la banca sobrepasó la puntuación límite
            mostrar_banca_pasada() # Muestra un mensaje indicando que la banca sobrepasó la puntuación límite
            banca.puntuacion = puntuacion # Guarda la puntuación de la banca
            break
        else: # En caso de que no haya sobrepasado la puntuación límite...
            if banca.decidir_plantar_banca(puntuacion, jugadores) == True: # Si la banca decide plantarse
                banca.puntuacion = puntuacion # Guarda la puntuación de la banca
                mostar_banca_plantada() # Muestra un mensaje indicando que la banca se plantó
                break
            else: # Si la banca NO se planta
                mostrar_banca_continua()
                continue

    mostrar_resultados(jugadores, banca)