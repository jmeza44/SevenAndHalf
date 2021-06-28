import random
import resourses as rsc
from cards import cards

def showMenu():
    rsc.clear()
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

def loadingBar():
    # en teoria se tenria que imprimir un loading bar
        rsc.sleep(2)

def playerTurn(deck):
    print("Iniciando un nuevo juego...")
    # Loading animation
    loadingBar()
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
        return player_passed

class main(cards):
    deck = cards()
    while True:
        showMenu()
        choise = choiseCatch()

        if choise == 1:
            player_passed = playerTurn(deck)
            if player_passed == True:
                print("Juego finalizado, te pasaste" +
                "\nRepite el juego :)")
            else:
                while True:
                    banca_score = 0.0
                    print("La banca está jugando...")
                    card = deck.takeCard()
                    print("La banca ha recibido un: " + str(card))
                    banca_score += deck.getScore(card)
                    print("Ahora el puntaje de la banca es: " + str(banca_score))
                    if banca_score == 7:
                        banca_planted = True
                        print("La banca se ha plantado")
                        break
                    elif banca_score > 7.5:
                        print("La banca se ha pasado")

            continue
        elif choise == 2:
            print("Puntajes: ")
        elif choise == 3:
            break
