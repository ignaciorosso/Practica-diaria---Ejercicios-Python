# Confeccionar una función que le enviemos como parámetro un string y nos retorne la cantidad 
# de caracteres que tiene. En el bloque principal solicitar la carga de dos nombres por teclado 
# y llamar a la función dos veces. Imprimir en el bloque principal cual de las dos palabras tiene más caracteres.

def retorna_cantidad(cadena):
    return len(cadena)


# Bloque principal del programa 

print('El programa nos devuelve la cantidad de caracteres que tienen dos nombres')
nombre1 = input('Ingrese un nombre: ')
nombre2 = input('Ingrese otro nombre: ')

print('El primer nombre tiene {} caracteres'.format(retorna_cantidad(nombre1)))
print('El segundo nombre tiene {} caracteres'.format(retorna_cantidad(nombre2)))

if (len(nombre1) > len(nombre2)):
    print('El nombre con mas caracteres es: ', nombre1)
elif (len(nombre1) < len(nombre2)):
    print('El nombre con mas caracteres es: ', nombre2)
else: 
    print('Ambos nombres tienen la misma cantidad de caracteres')
