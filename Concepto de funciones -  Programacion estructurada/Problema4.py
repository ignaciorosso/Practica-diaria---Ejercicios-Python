# Desarrollar un programa que solicite la carga de tres valores y muestre el menor. 
# Desde el bloque principal del programa llamar 2 veces a dicha función (sin utilizar una estructura repetitiva)


def carga_menor():
    valor1 = int(input('Ingrese primer valor: '))
    valor2 = int(input('Ingrese segundo valor: '))
    valor3 = int(input('Ingrese tercer valor: '))
    
    if (valor1 == valor2 and valor1 == valor3):
        print('Los valores ingresados son iguales')
    else:
        if (valor1 < valor2 and valor1 < valor3):
            print('El valor menor ingresado es: {}'.format(valor1))
        elif (valor2 < valor1 and valor2 < valor3):
            print('El valor menor ingresado es: {}'.format(valor2))
        else:
            print('El valor menor ingresado es: {}'.format(valor3))

# Bloque principal del programa

carga_menor()
carga_menor()