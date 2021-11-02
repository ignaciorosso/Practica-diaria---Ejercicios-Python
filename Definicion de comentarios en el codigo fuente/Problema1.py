# Realizar un programa que solicite la carga de valores enteros por teclado y los sume. 
# Finalizar la carga al ingresar el valor -1. Dejar como comentario dentro del 
# código fuente el enunciado del problema.

"""
suma = 0
n = int(input('Cantidad de valores a ingresar: '))

for f in range(n):
    valor = int(input('Ingrese valor: '))
    if (valor != -1):
        suma = suma + valor
    else:
        print('El programa ha finalizado')
        break

print('La suma de valores ingresados es: {}'.format(suma))
"""
# Otra forma de resolverlo

suma = 0
valor = int(input('Ingrese valor, el programa finaliza al ingresar -1 ')) # Se carga el primer valor
while (valor != -1):
    suma = suma + valor
    valor = int(input('Ingrese valor: ')) # Se carga del segundo valor en adelante 

print('La suma de valores ingresados es: {}'.format(suma))