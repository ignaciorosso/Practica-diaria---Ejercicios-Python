# Desarrollar una funcion que reciba un string como parametro y nos muestre 
# la cantidad de vocales. Llamarla desde el bloque principal del programa 3 veces con string distintos.

def contador_cadena(cadena):
    contador = 0
    for x in range(len(cadena)):
        if (cadena[x] == 'a' or cadena[x] == 'e' or cadena[x] == 'i' or cadena[x] == 'o' or cadena[x] == 'u' ):
            contador+=1
    print('El texto contiene {} vocales'.format(contador))

# Bloque principal del programa
cad = input('Escriba un breve texto: ')
contador_cadena(cad)
cad = input('Escriba un breve texto: ')
contador_cadena(cad)
cad = input('Escriba un breve texto: ')
contador_cadena(cad)

