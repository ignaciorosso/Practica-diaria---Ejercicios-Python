#Realizar la carga de dos números enteros por teclado e imprimir su suma y su producto.

num1 = int(input('Ingrese un numero: '))
num2 = int(input('Ingrese otro numero: '))

suma = num1 + num2
producto = num1 * num2

print('La suma de los numeros ingresados es {} \nEl resultado de la multiplicacion es {}'.format(suma, producto))

#Estaba probando el ejercicio con una funcion
"""
def sum(num1, num2):
    suma = num1 + num2
    mult = num1 * num2
    return suma, mult

num1 = int(input('Ingrese un numero: '))
num2 = int(input('Ingrese otro numero: '))

print(sum(num1, num2))
"""