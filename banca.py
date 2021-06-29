from cards import cards

def bancaGiveCard(deck):
    card = deck.takeCard()
    return card

def checkWinner(player_score, banca_score):
    if player_score > banca_score:
        print("El jugador gana por puntaje" +
        "\nJugador: " + str(player_score) +
        "\nBanca: " + str(banca_score))
    else:
        print("La banca gana por puntaje" +
        "\nJugador: " + str(player_score) +
        "\nBanca: " + str(banca_score))
