# Modulo de comportamiento del bot
from time import sleep


class Banca:
    def __init__(self, puntuacion=0.0):
        self.puntuacion = puntuacion

    def decidir_plantar_banca(self, puntuacion_banca, jugadores):
        puntuaciones_jugadores = [] # Lista con las puntuaciones de los jugadores
        for jugador in jugadores:
            if jugador.puntuacion <= 7.5: # Si la puntuación es menor o igual a 7.5 (Si el jugador no se pasó)...
                puntuaciones_jugadores.append(jugador.puntuacion) # ... Agrega las puntuaciones de los jugadores a la lista
            else: puntuaciones_jugadores.append(0.0) # Si el jugador se pasó se agrega 0.0 para evitar conflictos con el max() (Line 23)

        print(
            """
        + -------------- La banca está pensando -------------- +
        + ---------------------------------------------------- +""")
        sleep(6.0)
        if puntuacion_banca == 7.5: # Si la banca tiene una puntuación de 7.5...
            return True # ...Planta
        elif puntuacion_banca >= max(puntuaciones_jugadores): # Si la banca tiene una puntuación más alta que el resto de jugadores...
            if max(puntuaciones_jugadores) == 0.0 and puntuacion_banca == 0.5: # Si la banca tiene una puntuación de 0.5 y el resto de jugadores se pasaron...
                return False # NO se planta
            else: # Si la banca no tiene una puntuación de 0.5 ó alguno de los jugadores no se pasó...
                return True # ...Planta (Si su puntuación es igual a la del jugador con mayor puntuación también se planta)
        else: return False # Sino NO planta