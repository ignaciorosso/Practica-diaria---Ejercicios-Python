# Confeccionar un programa que contenga las siguientes funciones:
# 1) Carga de una lista y retorno al bloque principal.
# 2) Fijar en cero todos los elementos de la lista que tengan un valor menor a 10.
# 3) Imprimir la lista

def cargar_lista():
    lista = []
    continuar = "s"

    while (continuar == "s"):
        lista.append(int(input('Ingrese valor: ')))
        continuar = input('¿Desea ingresar otro valor? [s/n] ')

    return lista

def cambiar_elemento(lista):
    for x in range(len(lista)):
        if (lista[x] < 10):
            lista[x] = 0

def imprimir(lista):
    print(lista)

# Bloque principal del programa

lista = cargar_lista()
print('Lista antes de modificar')
imprimir(lista)
cambiar_elemento(lista)
print('Lista despues de modificar')
imprimir(lista)