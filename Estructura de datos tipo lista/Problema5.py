# Definir una lista por asignación con 5 enteros. 
# Mostrar por pantalla solo los elementos con valor iguales o superiores a 7.

lista = [1, 30, 2, 7, 0]
cont = 0

print(lista)

for f in range(len(lista)):
    if (lista[f] >= 7):
        cont+=1
        print(lista[f])
    else:
        pass

print('Cantidad de valores mayores o igual a 7: {}'.format(cont))