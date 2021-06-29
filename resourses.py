


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
