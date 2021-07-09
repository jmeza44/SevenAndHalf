# from menu import loadingGame, mainMenu, showMenu, choiseMenu, showMenuUser, showMenuUserName, tableScore
# from playSAH import playSAH
# import time
# import resourses as rsc

from game import Game

g = Game()

while g.running:
    g.game_loop()


# mostrar el menu, solo la primera vez.
# showMenu()
# exit = 0
# while True and exit == 0:
#     # Opcion del menu elegida por el usuario
#     choise = choiseMenu()

#     # Iniciar un nuevo juego
#     if choise == 1:
#         showMenuUser()
#         choiseUser = choiseMenu()
#         if choiseUser == 1:
#             showMenuUserName()
#             playerName = str(input(">> "))

#             rsc.sleep(1)

#             # start the game1
#             showMenu()
#             loadingGame()
#             time.sleep(1)
#             rsc.clear()


#     # Ver los puntajes
#     elif choise == 2:
#         showMenu()
#         tableScore()

#     # Salir del programa
#     elif choise == 3:
#         break

#     if exit < 1:
#         showMenu()



            # exit = playSAH(playerName)