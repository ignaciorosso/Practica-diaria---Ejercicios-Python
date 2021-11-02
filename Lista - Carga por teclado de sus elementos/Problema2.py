# Realizar la carga de valores enteros por teclado, almacenarlos en una lista. 
# Finalizar la carga de enteros al ingresar el cero. Mostrar finalmente el tamaño de la lista.

lista = []

valor = True

while(valor):
    entero = int(input('Ingrese valor entero a la lista: '))
    if (entero == 0):
        valor = False
    else:
        lista.append(entero)

print('El temaño de la lista es de: {} elementos'.format(len(lista)))


"""
OTRA FORMA DE HACERLO:

lista = []
elemento = int(input('Ingrese elemento a la lista: '))

while (elemento != 0):
    lista.append(elemento)

print(len(elemento))

"""