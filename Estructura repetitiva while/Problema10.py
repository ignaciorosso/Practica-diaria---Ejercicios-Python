# Realizar un programa que permita cargar dos listas de 15 valores cada una. 
# Informar con un mensaje cual de las dos listas tiene un valor acumulado mayor 
# (mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")
# Tener en cuenta que puede haber dos o más estructuras repetitivas en un algoritmo.

lista1 = 0
lista2 = 0

print('Vamos a ingresar valores a dos listas')
i = 1
while (i <= 15):
    valor1 = int(input('{}: Ingrese valores a la LISTA 1: '.format(i)))
    lista1 = lista1 + valor1
    i+=1
print('\n')
i = 1
while (i <=15):
    valor2 = int(input('{}: Ingrese valores a la LISTA 2: '.format(i)))
    lista2 = lista2 + valor2
    i+=1

if (lista1 == lista2):
    print('Las listas tienen el mismo valor: {}'.format(lista1))
elif (lista1 > lista2):
    print('La lista 1 es mayor a la lista 2. Valor: {}'.format(lista1))
else:
    print('La lista 2 es mayor a la lista 1. Valor: {}'.format(lista2))