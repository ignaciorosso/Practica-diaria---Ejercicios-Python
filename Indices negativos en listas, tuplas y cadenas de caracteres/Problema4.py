# Confeccionar un programa con las siguientes funciones:
# 1) Cargar una lista con 5 palabras.
# 2) Intercambiar la primer palabra con la última.
# 3) Imprimir la lista

def cargar_lista():
    print('Ingresar 5 palabras: ')
    palabras = []
    for x in range(5):
        palabras.append(input('Ingrese palabra: '))
    return palabras


def intercambio(palabras):
    aux = palabras[0]
    palabras[0] = palabras[-1]
    palabras[-1] = aux


def imprimir(palabras):
    print(palabras)

# Bloque principal del programa


lista = cargar_lista()
print('Lista antes de ser modificada')
imprimir(lista)
intercambio(lista)
print('Lista despues de ser modificada')
imprimir(lista)
