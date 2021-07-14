


# import only system from os
from os import system, name

# import sleet to show output for some time period
from time import sleep

# define our clear function
def clear():

    # for windows
    if name == "nt":
        _ = system("cls")

    # for mac, android, linux
    else:
        _ = system("clear")

def goSleep(seconds):
    sleep(seconds)

def recibir_eleccion_num(num_opciones) -> int: # Recibe una elección de cualquien menú con opciones numericas (parametro: número de opciones)
    while True: # Fuerza que la entrada esté entre las opciones
        try: # Fuerza que la entrada se un número entero
            eleccion = int(input(">> ")) # Toma la entrada
            if eleccion in range(1, num_opciones+1): # Verifica que la entrada esté en el rango de opciones
                break
            else: print("Intente nuevamente...")
        except (ValueError):
            print("ERROR!")
            continue
    return eleccion

def recibir_nombre() -> str: # Recibe el nombre del jugador en turno (El nombre es retornado para ser almacenado en una variable)
    # limpiar_consola()
    print(
        """
    + ----------- ¿Cuál es el nombre del jugador {} ------------ +
    + --------------------------------------------------------- +
        """.format(str()))
    nombre = input(">> ")
    return nombre