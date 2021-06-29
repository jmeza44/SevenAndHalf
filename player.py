from banca import bancaGiveCard
from cards import cards
import menu as mn
import resourses as rsc

class player:
    def __init__(self):
        self.active = False
        self.player_passed = False
        self.player_score = 0.0

    # get all data from attibutes, (not need in main execution)
    def getData(self):
        return (self.player_passed, float(self.player_score))

    # return the player's score
    def getScore(self):
        return float(self.player_score)

    # Set active
    def checkActive(self):
        return self.active

    def setActive(self):
        self.active = True

    def setNotActive(self):
        self.active = False

    # Bollean: if you player pass 7.5 loss
    def isPassed(self):
        if self.player_score > 7.5:
            return True
        else:
            return False
    
    def setPassed(self):
        self.player_passed = True


    def getCard(self, deck):
        # obtener una carta desde la banca
        card = bancaGiveCard(deck)
        return card
    
    def setScore(self, card):
        # en base a la carta recibida se obtienen los puntos
        self.player_score += cards.getScore(self, card)

    def jugadorTurn(self, deck):
        while True:
            mn.playing("<PLAYER NAME>")
            # rsc.sleep(3)

            # el jugador toma una carta del deck.
            card =  str(self.getCard(deck))
            mn.getCard(card)

            # en base de la carta recibida, se calcula los puntos.
            self.setScore(card)
            mn.getActualScore(self.getScore())

            if self.isPassed():
                self.setPassed()
                self.setNotActive()
                mn.lossMessage()
                break
            else:
                # plantarse o no plantarse
                print("¿Te plantas? yes/no - y/n")
                yesornot = str(input(">> "))
                if yesornot == "y" or yesornot == "yes":
                    print("Te has platando con una puntación de ", self.getScore())
                    break
                elif yesornot == "n" or yesornot == "no":
                    continue

    def bancaTurn(self, deck):
        while True:
            mn.playing("<LA BANCA>")
            # rsc.sleep(3)

            # la banca toma una carta del deck.
            card =  str(self.getCard(deck))
            mn.getCard(card)

            # en base de la carta recibida, se calcula los puntos.
            self.setScore(card)
            mn.getActualScore(self.getScore())

            if self.isPassed():
                self.setPassed()
                self.setNotActive()
                mn.lossMessageBanca()
                break
            else:
                # plantarse o no plantarse
                print("¿La Banca se plantas? ")
                print(" La banca está pensando...")
                rsc.sleep(2)

                if self.getScore() >= 7:
                    print("La Banca se planta!!")
                    break
                else:
                    rsc.sleep(3)
                    continue

