# Crear y cargar una lista con 5 enteros. Implementar un algoritmo que identifique el mayor valor de la lista.

entero = []

for f in range(5):
    entero.append(int(input('Cargar valor: ')))

print('La lista: {}'.format(entero))
# Basicamente toma un elemento cualquiera de la lista y lo compara con los demas

mayor = entero[0]

for x in range(len(entero)-1):
    if (entero[x] > mayor):
        mayor = entero[x]

print('El mayor elemento de la lista es: {}'.format(mayor))        

