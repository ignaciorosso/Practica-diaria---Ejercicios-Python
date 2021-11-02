# Solicitar por teclado dos enteros. El primer valor indica la cantidad de elementos que 
# crearemos en la lista. El segundo valor indica la cantidad de elementos que tendrá cada 
# una de las listas internas a la lista principal.
# Mostrar la lista y la suma de todos sus elementos.

n1 = int(input('Ingrese la cantidad de elementos que tendrá la lista: '))
n2 = int(input('Ingrese la cantidad de elementos que tendrán los elementos contenidos en la lista: '))

lista = []

for k in range(n1):
    sub_lista = []
    for x in range(n2):
        
        sub_lista.append(int(input('Ingrese valor: ')))
    lista.append(sub_lista)
print(lista)

suma = 0
for k in range(len(lista)):
    for x in range(len(lista[k])):
        suma = suma + lista[k][x]

print('La suma de los elementos de la lista es: {}'.format(suma))