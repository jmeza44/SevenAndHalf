import resourses as rsc

def showMenu():
    rsc.clear()
    print("----- 7 y un cachito -----" +
        "\n1. Iniciar un nuevo juego" +
        "\n2. Ver puntajes" +
        "\n3. Salir" +
        "\nIngrese el número correspondiente a la elección...")

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

def loadingBar():
    # en teoria se tendria que imprimir un loading bar
        rsc.sleep(2)
