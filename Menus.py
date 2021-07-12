from os import system, name # importa solo system desde os
from time import sleep # importa sleep para mostrar una salida por algún periodo de tiempo

def limpiar_consola(): # Método para limpiar la consola en cada sistema operativo
    if name == "nt": _ = system("cls") # for windows
    else: _ = system("clear") # for mac, android, linux

def mostrar_cargando(duracion): # Muestra una barra de carga
    for x in list(range(duracion)):
        print(end="#", flush=True)
        sleep(0.05)

def mostrar_menu_juego(): # Muestra el menú de elección del número de jugadores
    mostrar_cargando(40)
    limpiar_consola()
    print("""
    + ----------- ¿Cuántas personas se unirán a la mesa? ----------- +
    +  1 jugador      2 jugadores      3 jugadores     4 jugadores   +
    + -------------------------------------------------------------- +
    """)

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

def mezclar_mazo(): # Muestra un mensaje y una barra de carga antes de iniciar el juego
    limpiar_consola()
    print(
        """
    + ---------------------------------------------------- +
    + --------- el mazo está siendo mezclado... ---------- +
    + ---------------------------------------------------- +""")
    mostrar_cargando(40)

def mostar_menu_plantar(): # Muestra el menú para plantarse al jugador en turno
    print(
        """
        + ---------------------------------------------------- +
        + ------------------- ¿Te plantas? ------------------- +
        +              Sí/no                  y/n              +
        + ---------------------------------------------------- +""")

def mostrar_banca_continua(): # Muestra un mensaje cuando la banca continua jugando
    print(
        """
        + ------------ La banca continua jugando ------------- +
        + ---------------------------------------------------- +""")
    sleep(5.0)

def mostar_banca_plantada(): # Muestra un mensaje cuando la banca se planta
    print(
        """
        + -------------- La banca se plantó... --------------- +
        + ---------------------------------------------------- +""")
    sleep(5.0)

def mostrar_banca_pasada(): # Muestra un mensaje cuando la banca sobre pasa la puntuación límite
    print(
        """
        + --------------- La banca se pasó... ---------------- +
        + ---------------------------------------------------- +""")
    sleep(5.0)

def mostrar_jugador_pasado(nombre): # Muestra un mensaje al jugador en turno en caso de que pase la puntuación límite
    print(
        """
        + -------------- Te pasaste, lo siento --------------- +
        + -------- Es el turno del siguiente jugador --------- +
        + ---------------------------------------------------- +""")
    sleep(5.0)

def mostrar_puntaje(puntaje): # Muestra el puntaje del jugador en turno
    print(
        """
        + ---------------------------------------------------- +
        +               Tu puntaje actual es: {}
        + ---------------------------------------------------- +""".format(puntaje))

def mostrar_puntaje_banca(puntaje): # Muestra el puntaje de la banca
    print(
        """
        + ---------------------------------------------------- +
        +          El puntaje actual de la banca es: {}
        + ---------------------------------------------------- +""".format(puntaje))

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

def mostar_carta_banca(carta): # Muestra cuál es la carta que recibe la banca
    print(
        """\t+ ---------------------------------------------------- +
        + --- La banca se prepara para quitar una carta... --- +
        """)
    sleep(3.0)
    print(
        """
        + ------------ La banca ha recibido un: -------------- +
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

def mostrar_jugador_actual(nombre): # Indica quien está jugando en el turno en ejecución
    limpiar_consola()
    print(
        """
        + ---------------------------------------------------- +
                Es el turno de + --- {} --- +""".format(str(nombre)))