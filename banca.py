from cards import cards
from menu import lossMessage, lossMessageBanca

def bancaGiveCard(deck):
    card = deck.takeCard()
    return card

def checkWinner(player_score, player_is_passed, banca_score, banca_is_passed):
    if player_is_passed:
        lossMessage()
    elif banca_is_passed:
            lossMessageBanca()
    else:
        if player_score > banca_score:
            print("El jugador gana por puntaje" +
            "\nJugador: " + str(player_score) +
            "\nBanca: " + str(banca_score))
        else:
            print("La banca gana por puntaje" +
            "\nJugador: " + str(player_score) +
            "\nBanca: " + str(banca_score))
