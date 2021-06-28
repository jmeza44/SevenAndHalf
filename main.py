import random
from cards import cards

class main(cards):
    deck = cards()
    while True:
        print("----- 7 y un cachito -----" +
        "\n1. Iniciar un nuevo juego" +
        "\n2. Ver puntajes" +
        "\n3. Salir" + 
        "\nIngrese el número correspondiente a la elección...")
        
        while True:
            try:
                choise = int(input(">> "))
                if choise == 1 or choise == 2 or choise == 3:
                    break
                else: print("Intente nuevamente...")
            except (ValueError):
                print("ERROR!")
                continue
            
        if choise == 1:
            print("Iniciando un nuevo juego...")
            planted = False
            passed = False
            score = 0.0
            while True:
                print("La banca está entregando cartas...")
                card = deck.takeCard()
                print("La banca te ha entregado un: " + str(card))
                score += deck.getScore(card)
                print("Ahora tu puntaje es: " + str(score))
                if score > 7.5:
                    print("Te pasaste...")
                    passed = True
                    break
                else:
                    print("¿Te plantas? yes/not - y/n")
                    yesornot = str(input(">> "))
                    if yesornot == "y" or yesornot == "yes":
                        break
                    elif yesornot == "n" or yesornot == "not":
                        continue
            if passed == True:
                print("Juego finalizado, te pasaste" +
                "\nIntenta nuevamente :)")
            else:
                print("La banca está jugando...")
                card = deck.takeCard()
                print("La banca ha recibido un: " + str(card))
                score += deck.getScore(card)
                print("Ahora el puntaje de la banca es: " + str(score))
            
            continue
        elif choise == 2:
            print("Puntajes: ")
        elif choise == 3:
            break