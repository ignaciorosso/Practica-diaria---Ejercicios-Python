# Definir por asignación una lista de enteros en el bloque principal del programa. 
# Elaborar tres funciones, la primera recibe la lista y retorna la suma de todos sus elementos, 
# la segunda recibe la lista y retorna el mayor valor y la última recibe la lista y retorna el menor.

def retorna_suma(li):
    suma = 0
    for k in range(len(lista)):
        suma = suma + lista[k]
    return suma

def valor_mayor(li):
    mayor = lista[0]
    for k in range(1, len(lista)):
        if (lista[k] > mayor):
            mayor = lista[k]
    return mayor
    
def valor_menor(li):
    menor = lista[0]
    for k in range(1, len(lista)):
        if (lista[k] < menor):
            menor = lista[k]
    return menor



# Bloque principal del programa 

lista = [24, 56, 4, 34, 55, 6, 2, 20, 34, 56, 77]
print('La lista con valores enteros es: ', lista)
print('--------------------------------------------')
print('La suma de los elementos de la lista es: {}'.format(retorna_suma(lista)))
print('--------------------------------------------')
print('El mayor valor de la lista es: {}'.format(valor_mayor(lista)))
print('--------------------------------------------')
print('El menor valor de la lista es: {}'.format(valor_menor(lista)))