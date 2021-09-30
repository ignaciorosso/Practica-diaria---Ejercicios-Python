# Definir una lista que almacene 5 enteros. Sumar todos sus elementos y mostrar dicha suma.

lista = [34, 5, 64, 1, 3]

suma = 0
i = 0
while (i < len(lista)):
    suma = suma + lista[i]
    i+=1

print('El valor de los elementos de la lista es: {}'.format(suma))