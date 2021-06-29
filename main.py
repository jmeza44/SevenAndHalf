from menu import loadingGame, showMenu, choiseMenu, tableScore
from playSAH import playSAH
import time
import resourses as rsc

# mostrar el menu, solo la primera vez.
showMenu()
exit = 0
while True and exit == 0:
    # Opcion del menu elegida por el usuario
    choise = choiseMenu()

    # Iniciar un nuevo juego
    if choise == 1:
        showMenu()
        loadingGame()
        time.sleep(1)
        rsc.clear()
        exit = playSAH()

    # Ver los puntajes
    elif choise == 2:
        showMenu()
        tableScore()

    # Salir del programa
    elif choise == 3:
        break

    if exit < 1:
        showMenu()
