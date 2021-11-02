# Se cargan por teclado tres números distintos. Mostrar por pantalla el mayor de ellos.

'''
num1 = int(input('Ingrese el primer numero: '))
num2 = int(input('Ingrese el segundo numero: '))
num3 = int(input('Ingrese el tercer numero: '))

if (num1 > num2 and num1 > num3):
    print('El primer numero ingresado es el mayor')
else:
    if (num2 > num1 and num2 > num3):
        print('El segundo numero ingresado es el mayor')
    else:
        print('El tercer numero ingresado es el mayor')
'''

num1 = int(input('Ingrese el primer numero: '))
num2 = int(input('Ingrese el segundo numero: '))
num3 = int(input('Ingrese el tercer numero: '))

print("El mayor valor ingresado es: ")

if (num1 > num2):
    if (num1 > num3):
        print(num1)
    else:
        print(num3)
else:
    if (num2 > num3):
        print(num2)
    else: 
        print(num3)