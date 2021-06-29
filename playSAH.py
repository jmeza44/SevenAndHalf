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

        elif bancaPlayer.checkActive():
            bancaPlayer.bancaTurn(deck)
            bancaPlayer.setNotActive()
        else:
            checkWinner(jugador.getScore(), bancaPlayer.getScore())
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
