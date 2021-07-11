import random
class Mazo:
    def __init__(self):
        self.mazo = {
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
        self.cantidad_cartas = [4,4,4,4,4,4,4,0,0,4,4,4] # El mazo contiene cuatro cartas de cada valor
        # El número de cartas disponibles de cada tipo se puede saber a través de esta lista
        # Los valores con 0 corresponden a las cartas 8 y 9 que no entran en el juego (En el mazo no hay cartas 8 ni 9)

    def tomar_carta(self): # Toma una carta random del mazo y resta esa carta del mazo (retornae el nombre de la carta)
        while True:
            random_number = random.randrange(1, 13)
            if random_number < 8 or random_number > 9: # Evita que el valor random sea 8 ó 9
                if self.cantidad_cartas[random_number-1] > 0: # Verifica que aún queden cartas de ese tipo
                    self.cantidad_cartas[random_number-1] -= 1 # Resta la carta de la lista con la cantidad de cartas (Resta esa carta del mazo)
                    return self.mazo[random_number] # Retorna la carta
                else: continue # En caso de que no queden cartas de ese tipo se toma otra random
            else: continue # En caso de que el número random sea 8 ó 9 toma otro
    
    def tomar_valor_carta(self, carta): # Método para saber el valor correspondiente a la carta parametro (retorna float)
        inverse_deck = {
                    "UNO":1.0,
                    "DOS":2.0,
                    "TRES":3.0,
                    "CUATRO":4.0,
                    "CINCO":5.0,
                    "SEIS":6.0,
                    "SIETE":7.0,
                    "SOTA(10)":0.5,
                    "CABALLO(11)":0.5,
                    "REY(12)":0.5
                }
        return inverse_deck[carta]