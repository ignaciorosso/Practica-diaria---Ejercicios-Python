# El módulo operacioneslista.py contiene todas las funciones que nos permiten cargar
# una lista, imprimir el mayor de una lista y sumar todos los elementos y mostrar dicho valor.

def carga():
    lista = []
    continuar = "s"
    while (continuar == "s"):
        lista.append(int(input('Ingrese valor: ')))
        continuar = input('¿Desea cargar otro valor? [s/n] ')
    return lista


def imprimir(lista):
    mayor = lista[0]
    for x in range(1, len(lista)):
        if (lista[x] > mayor):
            mayor = lista[x]
    print('El mayor elemento de la lista {}'.format(mayor))


def sumar(lista):
    suma = 0
    for elemento in lista:
        suma += elemento
    print('La suma de todos los elementos es {}'.format(suma))
