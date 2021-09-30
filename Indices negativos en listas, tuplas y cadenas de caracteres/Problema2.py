# Confeccionar una función que reciba una palabra y verifique si es capicúa (es
# decir que se lee igual de izquierda a derecha que de derecha a izquierda)

def capicua(cadena):
    indice = -1
    igual = 0

    for x in range(0, (len(cadena)//2)):
        if (cadena[x] == cadena[indice]):
            igual += 1
        indice -= 1
    print(cadena)
    if igual == (len(cadena)//2):
        print('Es capicua')
    else:
        print('No es capicua')

# Bloque principal del programa


capicua("neuquen")
capicua("casa")
capicua("oso")
