from menu import menu, menu1

class Game():
    def __init__(self):
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.menu_level = 0
        self.option = 0

    def events(self):
            self.option = menu()
            # if self.option == 0:
            #     self.option = menu()

            
            if self.option == 1:
                print("opcion 1 activada")
                self.option = 10
            elif self.option == 2:
                print("opcion 2 activada")
            elif self.option == 3:
                print("saliendo del juego")
                self.running = False # stop running

            # if self.option == 10:
            #     self.option = menu1()
            
            # if self.option == 11:
            #     print("Crear nuevo usuario.")
            # elif self.option == 12:
            #     print("Cargar usuario.")
            # elif self.option == 12:
            #     print("Volver.")


    def game_loop(self):
        while self.running:
            self.events()


