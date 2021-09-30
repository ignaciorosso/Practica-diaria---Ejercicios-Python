# Cargar una cadena de caracteres por teclado. Mostrar la cadena del final al principio
# utilizando subíndices negativos.

def mostrar_reves(cadena):
    for x in range(1, (len(cadena)+1)):
        print(cadena[-x], sep="", end="")


# Bloque principal del programa


cadena = input('Ingrese un texto: ')
mostrar_reves(cadena)
