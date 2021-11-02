# Se ingresan por teclado tres números, si todos los valores ingresados son menores a 10, 
# imprimir en pantalla la leyenda "Todos los números son menores a diez".

num1 = int(input('Ingrese el primer numero: '))
num2 = int(input('Ingrese el segundo numero: '))
num3 = int(input('Ingrese el tercer numero: '))

if (num1 < 10 and num2 < 10 and num3 < 10):
    print('Todos los numeros ingresados son menores a diez')
else:
    print('Hay uno o mas numeros mayores a 10')