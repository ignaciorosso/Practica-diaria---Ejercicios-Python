# Definir por asignación una lista con 8 elementos enteros. 
# Contar cuantos de dichos valores almacenan un valor superior a 100.

lista = [23, 456, 23, 56, 123, 98, 478, 101]

cont = 0

for f in range(8):
    if (lista[f] > 100):
        cont+=1
    else:
        pass

print('Cantidad de elementos mayores a 100 en la lista: {}'.format(cont))