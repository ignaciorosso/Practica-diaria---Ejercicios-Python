# Realizar un programa que solicite ingresar dos números distintos y muestre por pantalla el mayor de ellos.

num1 = int(input('Ingrese un numero: '))
num2 = int(input('Ingrese otro numero: '))

if (num1==num2):
    print('Los numeros ingresados son iguales')
else: 
    if (num1>num2):
        print('El primer numero es mayor')
    else:
        print('El segundo numero es mayor')
