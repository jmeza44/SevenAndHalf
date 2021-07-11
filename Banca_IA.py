# Modulo de comportamiento del bot
from time import sleep


class Banca:
    def __init__(self, puntuacion=0.0):
        self.puntuacion = puntuacion

    def decidir_plantar_banca(self, puntuacion_banca, jugadores):
        puntuaciones_jugadores = [] # Lista con las puntuaciones de los jugadores
        for jugador in jugadores:
            puntuaciones_jugadores.append(jugador.puntuacion) # Agrega las puntuaciones de los jugadores a la lista

        print(
            """
        + -------------- La banca está pensando -------------- +
        + ---------------------------------------------------- +""")
        sleep(6.0)
        if puntuacion_banca == 7.5: # Si la banca tiene una puntuación de 7.5...
            return True # ...Planta
        elif puntuacion_banca >= max(puntuaciones_jugadores): # Si la banca tiene una puntuación más alta que el resto de jugadores...
            return True # ...Planta (Si su puntuación es igual a la del jugador con mayor puntuación también se planta)
        else: return False # Sino NO planta