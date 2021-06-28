import random
class cards:
    def __init__(self):
        self.deck = {
                1:"UNO",
                2:"DOS",
                3:"TRES",
                4:"CUATRO",
                5:"CINCO",
                6:"SEIS",
                7:"SIETE",
                10:"SOTA(10)",
                11:"CABALLO(11)",
                12:"REY(12)"
            }
    def takeCard(self):
        while True:
            random_number = random.randrange(1,13)
            if random_number < 8 or random_number > 9:
                return self.deck[random_number]
            else: continue
    
    def getScore(self, value):
        inverse_deck = {
                    "UNO":1,
                    "DOS":2,
                    "TRES":3,
                    "CUATRO":4,
                    "CINCO":5,
                    "SEIS":6,
                    "SIETE":7,
                    "SOTA(10)":0.5,
                    "CABALLO(11)":0.5,
                    "REY(12)":0.5
                }
        return inverse_deck[value]
        