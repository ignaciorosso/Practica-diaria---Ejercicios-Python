# Confeccionar una función que le enviemos como parámetros dos enteros y nos retorne el mayor.


def retorno_mayor(v1, v2):
    if (v1 == v2):
        return print("¡Los valores son iguales!")
    elif (v1 > v2):
        return v1
    else:
        return v2


# Bloque principal del programa

print('Ingrese dos valores para determinar cual es mayor')
valor1 = int(input('Ingrese un valor: '))
valor2 = int(input('Ingrese otro valor: '))

if (valor1 != valor2):
    print('El valor mayor es: ', retorno_mayor(valor1, valor2))
else:
    retorno_mayor(valor1, valor2)
