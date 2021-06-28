def bancaTurn(deck):
    banca_passed = False
    banca_score = 0.0
    while True:
        print("La banca está jugando...")
        card = deck.takeCard()
        print("La banca ha recibido un: " + str(card))
        banca_score += deck.getScore(card)
        print("Ahora el puntaje de la banca es: " + str(banca_score))
        if banca_score == 7:
            print("La banca se ha plantado con una puntación de: " + str(banca_score))
            break
        elif banca_score > 7.5:
            banca_passed = True
            print("La banca se ha pasado")
            break
    return (banca_passed, float(banca_score))
