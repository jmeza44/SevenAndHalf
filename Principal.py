# Clase Main de ejecución
from Recursos import iniciar_juego, mostrar_menu_princ, recibir_eleccion_num

if __name__ == "__main__":
    while True: # Ciclo de ejecución del algoritmo (Solo termina al seleccionar la opción 3 en el menú principal)
        mostrar_menu_princ()
        eleccion = recibir_eleccion_num(3)

        if eleccion == 1:
            iniciar_juego()
        elif eleccion == 2:
            print("Eleccion dos")
        else:
            print("Eleccion 3")
            break