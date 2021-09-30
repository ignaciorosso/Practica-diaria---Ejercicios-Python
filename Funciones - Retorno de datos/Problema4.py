# Elaborar una función que reciba tres enteros y nos retorne el valor promedio de los mismos.

def promedio(n1, n2, n3):
    prom = (n1 + n2 + n3) / 3
    return prom

# Bloque principal del programa

print('Ingrese 3 numeros para obtener su promedio')

num1 = int(input('Ingrese el primer numero: '))
num2 = int(input('Ingrese el segundo numero: '))
num3 = int(input('Ingrese el tercer numero: '))

print('El promedio de los numeros ingresados es: {}'.format(num1, num2, num3))
