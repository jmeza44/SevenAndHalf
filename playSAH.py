from random import random
from cards import cards
from player import player
from resourses import recibir_nombre, recibir_eleccion_num
import random
from banca import checkWinner
from menu import cantidadJugadores



def playSAH():
    # iniciando constructores
    deck = cards()
    # jugador = player("batata_name")
    # bancaPlayer = player("LA BANCA")

    # mostrar menu de preguntar cuantos jugadores
    # no implementado.

    jugadores = [] 

    cantidadJugadores()
    N = recibir_eleccion_num(4)
    print("N-jugadores: ", N)

    for i in range(0, N+1):
        if i < N:
            exec("player{0} = player('{1}')".format(i, recibir_nombre()))
            exec(f"jugadores.append(player{i})")
            print("juega: ", jugadores[i].player_name)
            jugadores[i].jugadorTurn(deck)
        elif i == N:
            exec("player{0} = player('{1}')".format(i, "LA-BANCA"))
            exec(f"jugadores.append(player{i})")
            print("juega: ", jugadores[i].player_name)
            jugadores[i].bancaTurn(deck, jugadores)


        print("\n\nlista real de resultados de esta ronda:")
        for obj in jugadores:
            if obj.player_score > 7.5:
                print("\n\n", obj.player_name, obj.player_score, "\t¡Se ha pasado!\t", end = " ", flush = True)
            elif obj.player_score <= 7.5:
                print("\n\n", obj.player_name, obj.player_score, "\t              \t", end = " ", flush = True)

            print("")


            


    
















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
