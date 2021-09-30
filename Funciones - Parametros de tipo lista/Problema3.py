# Crear una lista de enteros por asignación. Definir una función que reciba una lista de enteros 
# y un segundo parámetro de tipo entero. Dentro de la función mostrar cada elemento de la lista 
# multiplicado por el valor entero enviado.
# lista=[3, 7, 8, 10, 2]
# multiplicar(lista,3)

def multiplicar(lista, n):
    nueva_lista = []
    for k in range(len(lista)):
        nueva_lista.append(lista[k] * n)
    return nueva_lista

# Bloque principal del programa

lista = [12, 4, 56, 2, 45, 6, 1, 0]

n = int(input('Ingrese el valor por el que quiere multiplicar la lista: '))
print('La nueva lista multiplicada por {} es: {}'.format(n, multiplicar(lista, n)))