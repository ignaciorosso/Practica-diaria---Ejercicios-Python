# Escribir un programa en el cual se ingresen cuatro números, calcular e informar la suma 
# de los dos primeros y el producto del tercero y el cuarto

num1 = int(input('Ingrese el primer numero: '))
num2 = int(input('Ingrese el segundo numero: '))
num3 = int(input('Ingrese el tercero numero: '))
num4 = int(input('Ingrese el cuarto numero: '))

suma = num1 + num2
producto = num3 * num4

print('La suma de los dos primeros es: {}\nEl producto de los dos segundos es: {}'.format(suma, producto))