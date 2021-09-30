# Realizar un programa que pida la carga de dos listas numéricas enteras de 4 elementos cada una. Generar una tercer lista que surja de la suma de los elementos de la misma posición de cada lista. Mostrar esta tercer lista.

lista1 = []
lista2 = []

print('Ingrese valores para la primer lista')
for f in range(4):
    lista1.append(int(input('Ingrese un valor: ')))
    
print('Ingrese valores para la segunda lista')
for f in range(4):
    lista2.append(int(input('Ingrese un valor: ')))

print(lista1)
print(lista2)

lista3 = []

for x in range(4):
    aux = lista1[x] + lista2[x]
    lista3.append(aux)


print('El resultado de sumar las dos listas es:\n{}'.format(lista3))
