# Se ingresan por teclado tres números, si al menos uno de los valores ingresados es menor a 10, 
# imprimir en pantalla la leyenda "Alguno de los números es menor a diez".

num1 = int(input('Ingrese el primer numero: '))
num2 = int(input('Ingrese el segundo numero: '))
num3 = int(input('Ingrese el tercer numero: '))

if (num1 < 10 or num2 < 10 or num3 < 10):
    print('Alguno de los 3 numeros ingresados es menor a 10')
else:
    print('Todos los numeros ingresados son mayores a 10')