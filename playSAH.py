from random import random
from cards import cards
from player import player
from resourses import recibir_nombre, recibir_eleccion_num
import random
from banca import checkWinner
import menu as mn 



def playSAH():
    # iniciando constructores
    deck = cards()

    jugadores = [] 

    # Asking how many players will play
    mn.cantidadJugadores()
    N = recibir_eleccion_num(2, 4)
    print("N-jugadores: ", N)
    # N = 2
    for i in range(0, N):
        exec("player{0} = player('{1}')".format(i, recibir_nombre(i)))
        exec(f"jugadores.append(player{i})")

    z = 0  
    while z<3: # for the moment checking only thrree rounds
        for i in range(0, N):
            print("juega: ", jugadores[i].player_name)
            if i < N - 1:
                jugadores[i].jugadorTurn(deck)
            elif i == N - 1:
                jugadores[i].bancaTurn(deck) #original

        for i in range(0, N-1):
            if jugadores[i].player_score < jugadores[-1].playe_Score:
                print("juega: ", jugadores[i].player_name)
            if i < N - 1:
                jugadores[i].jugadorTurn(deck)
            elif i == N - 1:
                jugadores[i].bancaTurn(deck) #original

        print("TEMP")
        for x in jugadores:
            print(x.getData())
        print("TEMP")
        input("TEMP CHECK THE RESULTS")

        for i in  jugadores:
            i.setScore(0.0)

        print("TERMINA PRIMERA RONDA")
        z += 1 
        input("press any key to continue next round...")

    print(
            """
            + ---------------------------------------------------- +
            + -------------- Resultados de la mesa --------------- +""")


    # for obj in jugadores[:-1]:
    #     if obj.player_coins < 0:
    #         print("Se le expulsa de la mesa")
    #     else:
    #         obj.player_coins -= 10

    #     if obj.player_score > 7.5:
    #         jugadores[-1].player_coins += 10 # pasa a la Banca
    #         print("\n\n", obj.player_name, obj.player_score)
    #         print("\n\t¡Se ha pasado!      ", "\t ¡Ha perdido 10 monedas!", "\t Ahora tiene: ", obj.player_coins)

    #     elif obj.player_score < jugadores[-1].player_score:
    #         jugadores[-1].player_coins += 10
    #         print("\n\n", obj.player_name, obj.player_score)
    #         print("\n\t¡Menos que la Banca!", "\t ¡Ha perdido 10 monedas!", "\t Ahora tiene: ", obj.player_coins)
    #     elif obj.player_score <= 7.5 and obj.player_score > jugadores[-1].player_score:
    #         obj.player_coins += 20
    #         print("\n\n", obj.player_name, obj.player_score)
    #         print("\t              ", "\t\t ¡Ganó 20 monedas!", "\t Ahora tiene: ", obj.player_coins)
    #     print("")

    # print("\n\n", jugadores[-1].player_name, jugadores[-1].player_score)
    # print("\t              ", "\t                 !", "\t Ahora tiene: ",jugadores[-1].player_coins)
    # print("")


            


    
















    # # jugador empieza el juego
    # jugador.setActive()

    # play = True
    # while play:

    #     if jugador.checkActive():
    #         jugador.jugadorTurn(deck)
    #         jugador.setNotActive()
    #         if not jugador.isPassed():
    #             bancaPlayer.setActive()
    #             rsc.goSleep(1)
    #             print("Ahora es el turno de la Banca.")
    #             rsc.goSleep(2)
            
    #     elif bancaPlayer.checkActive():
    #         bancaPlayer.bancaTurn(deck, jugador.getScore())
    #         bancaPlayer.setNotActive()
    #     else:
    #         checkWinner(jugador.getScore(), jugador.isPassed(), bancaPlayer.getScore(), bancaPlayer.isPassed())
    #         yesornot = str(input("""
    #             press b to back to menu
    #             press x to exit
    #             >> """))
    #         if yesornot == "b":
    #             play = False
    #             return 0
    #         else:
    #             play = False
    #             return 1
