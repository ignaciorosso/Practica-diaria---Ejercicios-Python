# En el bloque principal del programa cargar los lados de dos rectángulos y 
# luego mostrar cual de los dos tiene una superficie mayor.

def retornar_superficie(lado1, lado2):
    return lado1 * lado2

# Bloque principal del programa

print('Primer rectangulo')
lado1 = int(input('Ingrese un lado del rectangulo: '))
lado2 = int(input('Ingrese otro lado del rectangulo: '))
print('Segundo rectangulo')
lado3 = int(input('Ingrese un lado del rectangulo: '))
lado4 = int(input('Ingrese otro lado del rectangulo: '))

if (retornar_superficie(lado1, lado2) != retornar_superficie(lado3, lado4)):
    if (retornar_superficie(lado1, lado2) > retornar_superficie(lado3, lado4)):
        print('El primer rectangulo es mayor, con una superficie: {} m^2'.format(retornar_superficie(lado1, lado2)))
    else:
        print('El segundo rectangulo es mayor, con una superficie: {} m^2'.format(retornar_superficie(lado3, lado4)))
else:
    print('Los rectangulos son iguales, con una superficie: {} m^2'.format(retornar_superficie(lado1, lado2)))