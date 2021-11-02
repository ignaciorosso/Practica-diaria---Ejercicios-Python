# Crear una lista por asignación. La lista tiene que tener 2 elementos. 
# Cada elemento debe ser una lista de 5 enteros.
# Calcular y mostrar la suma de cada lista contenida en la lista principal.


# Vamos a resolver este ejercicio de 3 maneras distintas.
"""
lista = [[3, 67, 3, 5, 67],[85, 5, 23, 5, 90]]

suma1 = lista[0][0] + lista[0][1] +lista[0][2] + lista[0][3] + lista[0][4]
suma2 = lista[1][0] + lista[1][1] +lista[1][2] + lista[1][3] + lista[1][4]

print('La suma del elemento 0 de la lista que contiene numeros enteros es: {}'.format(suma1))
print('La suma del elemento 1 de la lista que contiene numeros enteros es: {}'.format(suma2))
"""
# Segunda forma
"""
lista = [[3, 67, 3, 5, 67],[85, 5, 23, 5, 90]]

suma1 = 0
for f in range(len(lista[0])):
    suma1 = suma1 + lista[0][f]


suma2 = 0
for f in range(len(lista[1])):
    suma2 = suma2 + lista[1][f]

print('La suma del elemento 0 de la lista que contiene numeros enteros es: {}'.format(suma1))
print('La suma del elemento 1 de la lista que contiene numeros enteros es: {}'.format(suma2))
"""

# Tercerm forma

lista = [[3, 67, 3, 5, 67],[85, 5, 23, 5, 90]]

for k in range(len(lista)):
    suma = 0
    for x in range(len(lista[k])):
        suma = suma + lista [k][x]
    print('La suma del elemento {} de la lista que contiene numeros enteros es: {}'.format(k,suma))