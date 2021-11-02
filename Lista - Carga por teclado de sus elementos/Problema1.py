# Definir una lista vacía y luego solicitar la carga de 5 enteros por teclado 
# y añadirlos a la lista. Imprimir la lista generada.

lista = []

for f in range(5):
    lista.append(int(input('Ingrese valor a la lista: ')))

print(lista)