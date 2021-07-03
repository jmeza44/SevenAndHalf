from random import random
from cards import cards
from player import player
import resourses as rsc
import random
from banca import checkWinner


def playSAH():
    # iniciando constructores
    deck = cards()
    jugador = player()
    bancaPlayer = player()

    # jugador empieza el juego
    jugador.setActive()

    play = True
    while play:

        if jugador.checkActive():
            jugador.jugadorTurn(deck)
            jugador.setNotActive()
            if not jugador.isPassed():
                bancaPlayer.setActive()
                rsc.goSleep(1)
                print("Ahora es el turno de la Banca.")
                rsc.goSleep(2)
            
        elif bancaPlayer.checkActive():
            bancaPlayer.bancaTurn(deck, jugador.getScore())
            bancaPlayer.setNotActive()
        else:
            checkWinner(jugador.getScore(), jugador.isPassed(), bancaPlayer.getScore(), bancaPlayer.isPassed())
            yesornot = str(input("""
                press b to back to menu
                press x to exit
                >> """))
            if yesornot == "b":
                play = False
                return 0
            else:
                play = False
                return 1
