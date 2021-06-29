from player import playerTurn
from banca import bancaTurn

def playSAH(deck):

    player_results = playerTurn(deck)

    if player_results[0] == True:
        print("Juego finalizado, te pasaste" +
        "\nRepite el juego :)")
    else:
        banca_results = bancaTurn(deck)
    if banca_results[0] == True:
        print("El jugador gana, felicidades!")
    else:
        print("--------------------------" + "\nComparando puntajes...")
        checkWinner(player_results[1], banca_results[1])


def checkWinner(player_score, banca_score):
    if player_score > banca_score:
        print("El jugador gana por puntaje" +
        "\nJugador: " + str(player_score) +
        "\nBanca: " + str(banca_score))
    else:
        print("La banca gana por puntaje" +
        "\nJugador: " + str(player_score) +
        "\nBanca: " + str(banca_score))
