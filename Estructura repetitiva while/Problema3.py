# Desarrollar un programa que permita la carga de 10 valores por teclado y nos muestre 
# posteriormente la suma de los valores ingresados y su promedio.

x = 1
suma = 0

while (x <= 10):
    valor = int(input('Ingrese un valor a la vez: '))
    suma = suma + valor # Esto es un ACUMULADOR
    x+=1

promedio = suma/10
print('El promedio de los 10 valores ingresados es: {}'.format(promedio))
print('El programa ha finalizado')