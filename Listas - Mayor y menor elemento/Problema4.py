# Cargar una lista con 5 elementos enteros. Imprimir el mayor y un mensaje si se repite dentro de la lista (es decir si dicho valor se encuentra en 2 o más posiciones en la lista)

entero = []

for f in range(5):
    entero.append(int(input('Ingrese valor: ')))

entero_mayor = entero[0]
cont = 0

for x in range(len(entero)-1):
    if (entero[x] > entero_mayor):
        entero_mayor = entero[x]

for x in range(len(entero)): #Aqui debemos recorrer toda la lista
    if (entero[x] == entero_mayor):
        cont+=1

print('El mayor valor es: {}'.format(entero_mayor))

if (cont > 1):
    print('Se repite {} veces'.format(cont))
else:
    print('El valor no se repite ninguna vez en la lista')