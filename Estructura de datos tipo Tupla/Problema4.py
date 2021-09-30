# Confeccionar un programa con las siguientes funciones:
# 1)Cargar una lista de 5 enteros.
# 2)Retornar el mayor y menor valor de la lista mediante una tupla.
# Desempaquetar la tupla en el bloque principal y mostrar el mayor y menor.

def cargar_lista():
    enteros = []
    for x in range(5):
        enteros.append(int(input('Ingrese valor: ')))

    return enteros

def mayor_menor(enteros):
    mayor = enteros[0]
    menor = enteros[0]  
    for x in range(len(enteros)):
        if (mayor <= enteros[x]):
            mayor = enteros[x]
        if (menor >= enteros[x]):
            menor = enteros[x]

    return (mayor, menor)


# Bloque principal del programa

ent = cargar_lista()
may, men = mayor_menor(ent)
print('El valor mayor de la lista es {} y el valor menor {}'.format(may, men))