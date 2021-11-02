# Realizar un programa que contenga las siguientes funciones:
# 1) Carga de una lista de 10 enteros.
# 2) Recibir una lista y retornar otra con la primer mitad (se sabe que siempre
# llega una lista con una cantidad par de elementos)
# 3) Imprimir una lista.

def cargar_lista():
    lista = []
    for x in range(10):
        lista.append(int(input('Ingrese valor: ')))
    return lista


def retornar_mitad(lista):
    mitad = len(lista) // 2
    return lista[:mitad]


def imprimir(lista):
    print('Contenido de la lista')
    print(lista)


# Bloque principal del programa

lista = cargar_lista()
imprimir(lista)
lista2 = retornar_mitad(lista)
imprimir(lista2)
