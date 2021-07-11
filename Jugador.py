# Modulo con la información de los jugadores

class Jugador:
    def __init__(self, nombre, puntuacion=0.0): # Crea un jugador con su nombrer
        # En caso de que no se indique, la puntuación por defecto es 0.0
        self.nombre = nombre
        self.puntuacion = puntuacion