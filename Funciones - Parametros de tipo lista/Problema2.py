# Crear y cargar por teclado en el bloque principal del programa una lista de 5 enteros. 
# Implementar una función que imprima el mayor y el menor valor de la lista.

def mayor_menor(li):
    mayor = lista[0]
    menor = lista[0]
    for k in range(1, len(lista)):
        if (lista[k] > mayor):
            mayor = lista[k]
        if (lista[k] < menor):
            menor = lista[k]
    print('El mayor valor de la lista es: ', mayor)
    print('El menor valor de la lista es: ', menor)

# Bloque principal del programa 

lista = []
print('Ingrese 5 valores enteros a la lista')
for k in range(5):
    lista.append(input('Ingrese valor: '))

print('Los valores de la lista son: ', lista)
mayor_menor(lista) #En este caso vemos que la funcion no retorna nada, sino que la misma funcion es la encargada de imprimir los resultados