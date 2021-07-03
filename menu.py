import resourses as rsc

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
    print("""
            EL JUEGO SE ESTÁ INICIALIZANDO..
            """)
def tableScore():
    print("""

    LOS PUNTAJES SON: 
    
    """)

def loadingBar():
    # en teoria se tendria que imprimir un loading bar
        rsc.sleep(2)

def playing(name):
    print("_________________________________")
    print("\n\tEs el turno de {}...".format(str(name)))
    print("--------------------------------------------")

def getCard(card):
    rsc.clear()
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
    rsc.clear()
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