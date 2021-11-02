# Escribir un programa en el cual: dada una lista de tres valores numéricos distintos 
# se calcule e informe su rango de variación (debe mostrar el mayor y el menor de ellos)


print('Ingrese 3 numeros')

num1 = int(input('Ingrese el primer numero: '))
num2 = int(input('Ingrese el segundo numero: '))
num3 = int(input('Ingrese el tercer numero: '))

if (num1 > num2 and num1 > num3):
    if (num2 > num3):
        print('El MAYOR es: {} y el MENOR es: {}'.format(num1, num3))
    else:
        print('El MAYOR es: {} y el MENOR es: {}'.format(num1, num2))
else:
    if (num2 > num1 and num2 > num3):
        if (num1 > num3):
            print('El MAYOR es: {} y el MENOR es: {}'.format(num2, num3))
        else:
            print('El MAYOR es: {} y el MENOR es: {}'.format(num2, num1))
    else:
        if (num3 > num1 and num3 > num2):
            if (num1 > num2):
                print('El MAYOR es: {} y el MENOR es: {}'.format(num3, num2))
            else:
                print('El MAYOR es: {} y el MENOR es: {}'.format(num3, num1))
        else:
            print('Los numeros son iguales')

"""
OTRA FORMA DE RESOLVERLO:

if num1<num2 and num1<num3:
    print(num1)
else:
    if num2<num3:
        print(num2)
    else:
        print(num3)
if num1>num2 and num1>num3:
    print(num1)
else:
    if num2>num3:
        print(num2)
    else:
        print(num3)
"""
