
from cards import cards

# import resourses
from menu import showMenu, choiseMenu
from playSAH import playSAH


deck = cards()

print(deck.takeCard())

showMenu()
while True:
    # Opcion del menu elegida por el usuario
    choise = choiseMenu()

    # Iniciar un nuevo juego
    if choise == 1:
        showMenu()
        print("""
            USTED ELIGIÓ LA OPCION UNO
            
            EL JUEGO SE ESTÁ INICIALIZANDO..
            
            """)
        playSAH(deck)
        # player_results = list(playerTurn(deck))

    # Ver los puntajes
    elif choise == 2:
        showMenu()
        print("""
        
            LOS PUNTAJES SON: 
            
            """)
    # Salir del programa
    elif choise == 3:
        break