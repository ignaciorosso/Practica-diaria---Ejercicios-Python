# Realizar un programa que solicite la carga por teclado de dos números, 
# si el primero es mayor al segundo informar su suma y diferencia, en caso contrario 
# informar el producto y la división del primero respecto al segundo.

num1 = int(input('Ingrese un numero: '))
num2 = int(input('Ingrese otro numero: '))

if (num1 != num2):
    if (num1 > num2):
        suma = num1 + num2
        resta = num1 - num2
        print('La suma de ambos numeros es: {}\nSu diferencia es: {}'.format(suma, resta))
    else:
        producto = num1 * num2
        division = num1 / num2
        print('El producto de ambos numeros es: {}\nEl valor de primer numero dividido por el segundo es: {}'.format(producto, division))
else:
    print('Los numeros ingresados son iguales')
