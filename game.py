from menu import menu, menu1
from resourses import recibir_eleccion_num
from playSAH import playSAH

class Game():
    def __init__(self):
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.menu_level = 0
        self.option = 0


    def game_loop(self):
        while self.running:
            self.events()


    def events(self):
            menu()

            self.option = recibir_eleccion_num(3)
            # if self.option == 0:
            #     self.option = menu()


            if self.option == 1:
                print("opcion 1 iniciar juego")
                playSAH("batata")
            #     self.option = menu1()
            #     if self.option == 11:
            #      print("opcion 11 Crear nuevo usuario.")
            #     elif self.option == 12:
            #         print("opcion 12 Cargar usuario.")
            #     elif self.option == 13:
            #         print("opcion 13 Volver.")
            #         # self.option = menu()
            elif self.option == 2:
                print("opcion 2 ver puntajes")
            elif self.option == 3:
                print("saliendo del juego")
                self.running = False # stop running

            # if self.option == 10:
            #     self.option = 
            
 





