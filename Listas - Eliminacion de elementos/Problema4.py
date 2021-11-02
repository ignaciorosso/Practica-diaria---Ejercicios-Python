# Crear una lista de 5 enteros y cargarlos por teclado. Borrar los elementos mayores 
# o iguales a 10 y generar una nueva lista con dichos valores.

enteros = []

for k in range(5):
    enteros.append(int(input('Ingrese numeros enteros: ')))

print('Lista de enteros\n', enteros)

enteros2 = [] # Lista generada pra guardar elementos que se borran de la otra lista
posicion = 0
while (posicion < len(enteros)):
    if (enteros[posicion] >= 10):
        enteros2.append(enteros.pop(posicion))
    else:
        posicion+=1
print('Lista  original despues de borrar los elementos mayores o iguales a 10\n', enteros)
print('La nueva lista de enteros mayores o iguales a 10\n', enteros2)