def playerTurn(deck):
    player_passed = False
    player_score = 0.0
    while True:
        print("La banca está entregando cartas...")
        card = deck.takeCard()
        print("La banca te ha entregado un: " + str(card))
        player_score += deck.getScore(card)
        print("Ahora tu puntaje es: " + str(player_score))
        if player_score > 7.5:
            print("Te pasaste...")
            player_passed = True
            break
        else:
            print("¿Te plantas? yes/not - y/n")
            yesornot = str(input(">> "))
            if yesornot == "y" or yesornot == "yes":
                print("Te has platando con una puntación de " + str(player_score))
                break
            elif yesornot == "n" or yesornot == "not":
                continue
    return (player_passed, float(player_score))
