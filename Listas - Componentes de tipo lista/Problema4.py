# Imprimir la lista. Luego fijar con el valor cero todos los elementos mayores a 50 del 
# primer elemento de "lista". Volver a imprimir la lista.

lista=[[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]

print(lista)

for k in range(1): # El codigo que hice es mas generico
    for x in range(len(lista[k])):
        if (lista[k][x] > 50):
            lista[k][x] = 0

print(lista)

# Pero tambien se puede resolver de esta manera: 
"""
for x in range(len(lista[0])):
    if (lista[0][x] > 50):
        lista[0][x] = 0

print(lista)
"""