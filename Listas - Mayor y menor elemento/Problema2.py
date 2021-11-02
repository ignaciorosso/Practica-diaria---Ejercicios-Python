# Crear y cargar una lista con 5 enteros por teclado. Implementar un algoritmo que identifique el menor valor de la lista y la posición donde se encuentra.

entero = []

for f in range(5):
    entero.append(int(input('Cargar valor: ')))

print('La lista: {}'.format(entero))

menor_valor = entero[0]
posicion = 0
for x in range(len(entero)-1):
    if (entero[x] < menor_valor):
        menor_valor = entero[x]
        posicion = x

print('El menor elemento de la lista es: {}'.format(menor_valor))
print('Se encuentra en la posicion {} de la lista'.format(posicion))