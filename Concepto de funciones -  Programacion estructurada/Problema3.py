# Desarrollar un programa con dos funciones. La primer solicite el ingreso de 
# un entero y muestre el cuadrado de dicho valor. La segunda que solicite la carga 
# de dos valores y muestre el producto de los mismos. LLamar desde el bloque del 
# programa principal a ambas funciones.

def carga_cuadrado():
    valor = int(input('Ingrese un valor entero: '))
    cuadrado = valor ** 2
    print('El cuadrado de {} es {}'.format(valor, cuadrado))

def carga_producto():
    valor1 = int(input('Ingrese un valor: '))
    valor2 = int(input('Ingrese otro valor: '))
    producto = valor1 * valor2
    print('{} * {} = {}'.format(valor1, valor2, producto))


# Bloque principal del programa 
carga_cuadrado()
carga_producto()