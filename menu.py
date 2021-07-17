import resourses as rsc
import keyboard # using module keyboard
import time

tiempo = 0.0

def menu():
    rsc.clear()
    print("""        + ----------------- 7 y un cachito ---------------- +
        + 1. Iniciar un nuevo juego.                        +
        + 2. Ver puntajes.                                  +
        + 3. Salir.                                         +
        +                                                   +
        + Ingrese el número correspondiente a la elección...+
        +---------------------------------------------------+\n""")
    
def menu1():
    option_value = int(input("""        + ----------------- 7 y un cachito ---------------- +
        + 1. Crear nuevo usuario.                           +
        + 2. Cargar usuario. (not implemented)              +
        + 3. Volver.                                         +
        +                                                   +
        + Ingrese el número correspondiente a la elección...+
        +---------------------------------------------------+\n"""))
    option_value = option_value + 10
    return option_value

def mainMenu():
    tiempo = time.time() 
    while True:
        try:
            if keyboard.is_pressed('a'):
                showMenu()
                # print("IZQUIERDA: ", tiempo_p - tiempo)
            elif keyboard.is_pressed('d'):
                tiempo_p =time.time()
                print("DERECHA: ", tiempo_p - tiempo)
            elif keyboard.is_pressed('w'):
                tiempo_p =time.time()
                print("ARRIBA: ", tiempo_p - tiempo)
            elif keyboard.is_pressed('s'):
                tiempo_p =time.time()
                print("ABAJO: ", tiempo_p - tiempo)

        except:
            break


def showMenu():
    rsc.clear()
    print(
"""        + ----------------- 7 y un cachito ---------------- +
        + 1. Iniciar un nuevo juego.                        +
        + 2. Ver puntajes.                                  +
        + 3. Salir.                                         +
        +                                                   +
        + Ingrese el número correspondiente a la elección...+
        +---------------------------------------------------+""" + "\n")

def showMenuUser():
    rsc.clear()
    print(
"""        + ----------------- 7 y un cachito ---------------- +
        + 1. Crear nuevo usuario.                           +
        + 2. Cargar usuario. (not implemented)              +
        + 3. Salir.                                         +
        +                                                   +
        + Ingrese el número correspondiente a la elección...+
        +---------------------------------------------------+""" + "\n")

def showMenuUserName():
    rsc.clear()
    print(
"""        + ----------------- 7 y un cachito ---------------- +
        + Ingrese un nuevo nombre de usuario:               +
        +                                                   +
        +                                                   +
        +                                                   +
        + Ingrese el número correspondiente a la elección...+
        +---------------------------------------------------+""" + "\n")

def choiseMenu():
    while True:
            try:
                choise = int(input(">> "))
                if choise == 1 or choise == 2 or choise == 3:
                    break
                else: print("Intente nuevamente...")
            except (ValueError):
                print("ERROR!")
                continue
    return choise

def loadingGame():
    rsc.clear()
    print("""
            EL MAZO SE ESTA MESCLANDO...
            """)
    for x in list(range(0, 30)):
        print(end="#", flush=True)
        rsc.sleep(0.05)

def tableScore():
    print("""

    LOS PUNTAJES SON: 
    
    """)

def loadingBar():
    # en teoria se tendria que imprimir un loading bar
        rsc.sleep(2)

def playing(name):
    rsc.clear()
    print("_________________________________")
    print("\n\tEs el turno de {}...".format(str(name)))
    print("--------------------------------------------")

def getCard(card):
    print("La banca se prepara para quitar una carta...")
    # rsc.sleep(1.3)
    print("La banca te ha entregado un: \n")
    print("""
        |---------------|
        | {}            
        |               |
        |               |
        |               |
        |               |
        |               |
        |               |
        |               |
        |_______________|""".format(str(card)))

def getCardBanca(card):
    print("La banca se prepara para quitar una carta...")
    # rsc.sleep(1.3)
    print("La banca se ha entregado un: \n")
    print("""
                                    |---------------|
                                    | {}            
                                    |               |
                                    |               |
                                    |               |
                                    |               |
                                    |               |
                                    |               |
                                    |               |
                                    |_______________|""".format(str(card)))
    
def getActualScore(score):
    print("\n\tTu puntaje total es: ", score, "\n\t-----------------------------")

def getActualBancaScore(score):
    print("\n\tEl puntaje total de la Banca es: ", score, "\n\t-----------------------------")

def lossMessage():
    print("///////////////No puede ser, tu haz perdido..........")

def lossMessageBanca():
    print("///////////////LA BANCA HA PERDIDO..........")

def cantidadJugadores(): # Muestra el menú de elección del número de jugadores
    # mostrar_cargando(40)
    # limpiar_consola()
    print("""
    + ----------- ¿Cuántas personas se unirán a la mesa? ----------- +
    +  1 jugador      2 jugadores      3 jugadores     4 jugadores   +
    + -------------------------------------------------------------- +
    """)