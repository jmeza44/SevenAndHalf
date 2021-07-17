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
        self.player_coins = 100
    """Boleans"""
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
    def isPassed(self) -> bool:
        if self.player_score > 7.5:
            return True
        else:
            return False

    def isPassedCard(self, card) -> bool:
        print("\n TRAYENDO VALOR DE CARTA: ", cards.getScore(self, card))
        if self.player_score + cards.getScore(self, card) > 7.5:
            return True
        else:
            return False
    # set the player just passed 7.5 points
    def setPassed(self):
        self.player_passed = True
    # set the player still playing
    def setNotPassed(self):
        self.player_passed = False

    """getters"""
    def getName(self):
        return self.player_name

    def getScore(self) -> float:
        return self.player_score

    def getCoins(self):
        return float(self.player_coins)

    def getData(self):
        return ( 
        self.active,
        self.player_passed,
        self.player_name,
        self.player_score,
        self.player_coins)
    """setters"""
    def setName(self, name):
        self.player_name = name
    
    def setScore(self, score):
        self.player_score = score

    """Methods"""
    # the player get a card from the bank.
    def getCard(self, deck):
        card = bancaGiveCard(deck)
        return card
    
    # depent of which card the player received, this compute his score.
    def addScore(self, card):
        self.player_score += cards.getScore(self, card)


    """player logic"""
    def jugadorTurn(self, deck):
        self.setActive()
        while not self.isPassed() and self.checkActive():
            mn.playing(self.player_name)
            rsc.sleep(0.3)

            # el jugador toma una carta del deck.
            card =  str(self.getCard(deck))
            mn.getCard(card)

            if self.isPassedCard(card):
                input("\t\tse ha pasado.")
                self.setPassed()
                self.setNotActive()
                self.setScore(0.0)
                # break
            else:
                self.addScore(card)
                mn.getActualScore(self.getScore())
                print("¿Te plantas? si/no - s/n")
                yesornot = rsc.recibir_eleccion_str()
                print("TEMP, se refibe el valor de: ", yesornot)
                if yesornot == "y" or yesornot == "si" or yesornot == "s" :
                    print("Te has platando con una puntación de ", self.getScore())
                    # break
                    self.setNotActive()
                elif yesornot == "n" or yesornot == "no":
                    continue                

            print("\n EL VALOR ACTUAL EN PUNTOS ES: ", self.getScore())
            input("press any key to continue.. final del turno")
        self.setNotActive()

        """Banca Logic"""
    def bancaTurn(self, deck):
        self.setActive()
        while not self.isPassed() and self.checkActive():
            mn.playing(self.player_name)
            # rsc.sleep(3)

            # el jugador toma una carta del deck.
            card =  str(self.getCard(deck))
            mn.getCard(card)

            if self.isPassedCard(card):
                input("\t\tse ha pasado.")
                self.setPassed()
                self.setNotActive()
                # break
            else:
                self.addScore(card)
                mn.getActualScore(self.getScore())
                print("¿Te plantas? si/no - s/n")
                yesornot = rsc.recibir_eleccion_str()
                print("TEMP, se refibe el valor de: ", yesornot)
                if yesornot == "y" or yesornot == "si" or yesornot == "s" :
                    print("Te has platando con una puntación de ", self.getScore())
                    # break
                    self.setNotActive()
                elif yesornot == "n" or yesornot == "no":
                    continue                

            print("\n EL VALOR ACTUAL EN PUNTOS ES: ", self.getScore())
            input("press any key to continue.. final del turno")
        self.setNotActive()



    # def bancaTurnOld(self, deck, list_scores):
    #     while True:
    #         mn.playing(self.player_name)
    #         # la banca toma una carta del deck.
    #         card =  str(self.getCard(deck))
    #         mn.getCardBanca(card)

    #         # en base de la carta recibida, se calcula los puntos.
    #         self.setScore(card)
    #         mn.getActualBancaScore(self.getScore())

    #         # plantarse o no plantarse
    #         print("¿La Banca se planta? ")
    #         print(" La banca está pensando", end=" ", flush = True)
    #         rsc.sleep(1)
    #         # print(".", end=" ", flush = True)
    #         # rsc.sleep(1)
    #         # print(".", end=" ", flush = True)
    #         # rsc.sleep(1)
    #         # print(".", end=" ", flush = True)

    #         max = list_scores[0].player_score
    #         for scores in list_scores[:-2]:
    #             if max < scores.player_score():
    #                 max = scores.player_score()

    #         # puntos = []
    #         # max = list_scores[0].player_score
    #         # for scores in list_scores[:-2]:
    #             # print("TEST: ", scores.player_score)

    #         print("\n\n###TEMPORAL: EL MAYOR de entre los jugadores es: ", max)

    #         if max < self.getScore() and self.getScore() <= 7.5:
    #             print("La Banca se planta!!")
    #             break              
    #         elif self.getScore() >= 6:
    #             print("La Banca se planta!!")
    #             break
    #         elif self.getScore() > 7.5:
    #             print("la banca pierde, y se pone los puntos a cero.............")
    #             self.resetScore()
    #         else:
    #             rsc.sleep(1)
    #             continue

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

