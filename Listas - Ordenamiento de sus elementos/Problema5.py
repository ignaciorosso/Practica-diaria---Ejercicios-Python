# Cargar una lista con 5 elementos enteros. Ordenarla de menor a mayor y mostrarla 
# por pantalla, luego ordenar de mayor a menor e imprimir nuevamente.

entero = []

for f in range(5):
    entero.append(int(input('Ingrese valor: ')))

print('La lista de numeros enteros -sin ordenar-\n{}'.format(entero))

for k in range(len(entero)-1):  # Ordena de menor a mayor
    for x in range(len(entero)-k-1):
        if (entero[x] > entero[x+1]):
            aux = entero[x]
            entero[x] = entero[x+1]
            entero[x+1] = aux

print('La lista de numeros enteros -menor a mayor-\n{}'.format(entero))

for k in range(len(entero)-1): # Ordena de mayor a menor
    for x in range(len(entero)-k-1):
        if (entero[x] < entero[x+1]):
            aux = entero[x]
            entero[x] = entero[x+1]
            entero[x+1] = aux

print('La lista de numeros enteros -mayor a menor-\n{}'.format(entero))
