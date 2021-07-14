from banca import bancaGiveCard
from cards import cards
import menu as mn
import resourses as rsc

class player:
    def __init__(self, playerName):
        # player's states
        self.active = False
        self.player_passed = False

        # player's own data
        self.player_name = playerName
        self.player_score = 0.0
        self.player_coins = 0.0


    def getName(self):
        return self.player_name

    # get all data from attibutes, (not need in main execution)
    def getData(self):
        return (self.player_passed, float(self.player_score))

    # return the player's score
    def getScore(self):
        return float(self.player_score)

    # check if this player is active
    def checkActive(self):
        return self.active

    # set focus on this player
    def setActive(self):
        self.active = True

    # this player lost the focus
    def setNotActive(self):
        self.active = False

    # Bolean: if player pass 7.5 points, the player lost
    def isPassed(self):
        if self.player_score > 7.5:
            return True
        else:
            return False
    # set the player just passed 7.5 points
    def setPassed(self):
        self.player_passed = True

    # the player get a card from the bank.
    def getCard(self, deck):
        card = bancaGiveCard(deck)
        return card
    
    # depent of which card the player received, this compute his score.
    def setScore(self, card):
        self.player_score += cards.getScore(self, card)

    def jugadorTurn(self, deck):
        while True:
            mn.playing(self.player_name)
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
                break
            else:
                # plantarse o no plantarse
                print("¿Te plantas? si/no - s/n")
                yesornot = str(input(">> "))
                if yesornot == "s" or yesornot == "si":
                    print("Te has platando con una puntación de ", self.getScore())
                    break
                elif yesornot == "n" or yesornot == "no":
                    continue

    def bancaTurn(self, deck, list_scores):
        while True:
            mn.playing(self.player_name)
            # la banca toma una carta del deck.
            card =  str(self.getCard(deck))
            mn.getCardBanca(card)

            # en base de la carta recibida, se calcula los puntos.
            self.setScore(card)
            mn.getActualBancaScore(self.getScore())

            # plantarse o no plantarse
            print("¿La Banca se planta? ")
            print(" La banca está pensando", end=" ", flush = True)
            rsc.sleep(1)
            # print(".", end=" ", flush = True)
            # rsc.sleep(1)
            # print(".", end=" ", flush = True)
            # rsc.sleep(1)
            # print(".", end=" ", flush = True)

            max = list_scores[0].player_score
            for scores in list_scores[:-2]:
                if max < scores.player_score:
                    max = scores.player_score

            # puntos = []
            # max = list_scores[0].player_score
            # for scores in list_scores[:-2]:
                # print("TEST: ", scores.player_score)

            print("\n\nEL MAYOR de entre los jugadores es: ", max)

            if max < self.getScore() and self.getScore() <= 7.5:
                print("La Banca se planta!!")
                break              
            elif self.getScore() >= 7:
                print("La Banca se planta!!")
                break
            else:
                rsc.sleep(1)
                continue

    # def bancaTurn(self, deck, player_score):
    #     while True:
    #         mn.playing(self.player_name)
    #         # rsc.sleep(3)

    #         # la banca toma una carta del deck.
    #         card =  str(self.getCard(deck))
    #         mn.getCardBanca(card)

    #         # en base de la carta recibida, se calcula los puntos.
    #         self.setScore(card)
    #         mn.getActualBancaScore(self.getScore())

    #         if self.isPassed():
    #             self.setPassed()
    #             self.setNotActive()
    #             break
    #         else:
    #             # plantarse o no plantarse
    #             print("¿La Banca se plantas? ")
    #             print(" La banca está pensando", end=" ", flush = True)
    #             rsc.sleep(1)
    #             print(".", end=" ", flush = True)
    #             rsc.sleep(1)
    #             print(".", end=" ", flush = True)
    #             rsc.sleep(1)
    #             print(".", end=" ", flush = True)

    #             if self.getScore() > player_score and self.getScore() <= 7.5:
    #                 print("La Banca se planta!!")
    #                 break              
    #             elif self.getScore() >= 7:
    #                 print("La Banca se planta!!")
    #                 break
    #             else:
    #                 rsc.sleep(1)
    #                 continue

