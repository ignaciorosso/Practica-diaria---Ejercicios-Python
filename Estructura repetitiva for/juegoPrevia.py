import random

def juego():
    x = random.uniform(1, 10)
    if (x <= 5):
        print('\n----Tomas, gil----\n')
    else: 
        print('\n----Te salvaste----\n')

print('\n¿Arrancamos?\n')

while(True):
    try:
        inicio = input("Presione 'S' para comenzar el juego:\nPresione 'N' para salir:\n\n")
        y = inicio.lower()
        if (y == "s"):
            juego()
        elif (y == "n"):
            print('\nSos un ¡CAGON!\n')
        else:
            print('\nNo seas gil y ingresa una de las dos opciones\n')
    except:
        print('No es correcto')