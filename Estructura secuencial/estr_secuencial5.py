# Realizar un programa que lea cuatro valores numéricos e informar su suma y promedio.

num1 = int(input('Ingrese el primer numero: '))
num2 = int(input('Ingrese el segundo numero: '))
num3 = int(input('Ingrese el tercer numero: '))
num4 = int(input('Ingrese el cuarto numero: '))

suma = num1 + num2 + num3 + num4
promedio = suma/4

print('La suma de los 4 numeros es: {}\nY el promedio es: {}'.format(suma, promedio))