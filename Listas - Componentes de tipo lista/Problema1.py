# Crear una lista por asignación. La lista tiene que tener cuatro elementos. 
# Cada elemento debe ser una lista de 3 enteros.
# Imprimir sus elementos accediendo de diferentes modos.

lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

# De este modo se imprime la lista completa
print(lista)
print('-----------------------------------------------')

# De este modo se imprime el primer elemento de la lista
print(lista[0])
print('-----------------------------------------------')

# De este modo se imprime la primer componente de la lista que esta dentro de la lista mas grande
print(lista[0][0])
print('-----------------------------------------------')

# De este modo se imrpimen todos los indices de la primera lista dentro de la lista mas grande
for x in range(len(lista[0])):
    print(lista[0][x])
print('-----------------------------------------------')

# De este modo se imprimen todos los elementos de la lista
for k in range(len(lista)):
    for x in range(len(lista[k])):
        print(lista[k][x])
print('-----------------------------------------------')
