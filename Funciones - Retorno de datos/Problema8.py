# Plantear una función que reciba un string en mayúsculas o minúsculas y retorne la cantidad de letras 'a' o 'A'.

def contar_cadena(cadena):
    contador = 0
    for k in range(len(cadena)):    
        if (cadena[k] == 'a' or cadena[k] == 'A'):
            contador+=1
    return contador

# Bloque principal del programa

palabra = input('Ingrese una palabra: ')
print('Cantidad de letras "a" o "A" de la palabra "{}" es: {}'.format(palabra, contar_cadena(palabra)))