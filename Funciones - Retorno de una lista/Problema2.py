# Confeccionar una función que cargue por teclado una lista de 5 enteros y la retorne. 
# Una segunda función debe recibir una lista y retornar el mayor y el menor valor de la lista. 
# Desde el bloque principal del programa llamar a ambas funciones e imprimir el mayor 
# y el menor de la lista.


def cargar_lista():
    li = []
    print('Cargue 5 valores a la lista')
    for x in range(5):
        li.append(int(input('Ingrese valor: ')))
    return li

def mayor_menor(lista):
    mayor = lista[0]
    menor = lista[0]
    for x in range(1,len(lista)):
        if (lista[x] > mayor):
            mayor = lista[x]
        if (lista[x] < menor):
            menor = lista[x]
    return [mayor, menor] # Cuando tenemos que retornar varios valores podemos hacerlo con una lista


# Bloque principal del programa

lista = cargar_lista()
print('La lista ingresada es: ', lista)

lista_retornada = mayor_menor(lista)

print('El valor mayor de la lista es: {}'.format(lista_retornada[0]))
print('El valor menor de la lista es: {}'.format(lista_retornada[1]))

"""
#Otra forma de hacerlo:

mayor, menor = mayor_menor(lista)

print('El valor mayor de la lista es: {}'.format(mayor))
print('El valor menor de la lista es: {}'.format(menor))
"""