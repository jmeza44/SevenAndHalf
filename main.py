import random
from cards import cards

def showMenu():
    print("----- 7 y un cachito -----" +
        "\n1. Iniciar un nuevo juego" +
        "\n2. Ver puntajes" +
        "\n3. Salir" + 
        "\nIngrese el número correspondiente a la elección...")

def choiseCatch():
    while True:
            try:
                choise = int(input(">> "))
                if choise == 1 or choise == 2 or choise == 3:
                    break
                else: print("Intente nuevamente...")
            except (ValueError):
                print("ERROR!")
                continue
    return choise

def playerTurn(deck):
    print("Iniciando un nuevo juego...")
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

def checkWinner(player_score, banca_score):
    if player_score > banca_score:
        print("El jugador gana por puntaje" +
        "\nJugador: " + str(player_score) +
        "\nBanca: " + str(banca_score))
    else:
        print("La banca gana por puntaje" +
        "\nJugador: " + str(player_score) +
        "\nBanca: " + str(banca_score))

class main(cards):
    deck = cards()
    while True:
        showMenu()
        choise = choiseCatch()
        
        if choise == 1:
            player_results = list(playerTurn(deck))
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
                
            continue
        elif choise == 2:
            print("Puntajes: ")
        elif choise == 3:
            break