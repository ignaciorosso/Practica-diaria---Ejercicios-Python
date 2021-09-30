# Desarrollar un programa que permita ingresar el lado de un cuadrado. 
# Luego preguntar si quiere calcular y mostrar su perímetro o su superficie.

def perimetro_cuadrado(lado):
    per = lado * 4
    print('El perimetro del cuadrado es: {} m'.format(per))

def superficie_cuadrado(lado):
    sup = lado * lado
    print('La superficie del cuadrado es: {} m^2'.format(sup))

def cargar_dato():
    lado = int(input('Ingrese el lado de un cuadrado: '))
    decision = input('¿Desea calcular el perimetro o la superficie? [perimetro/superficie] ').lower()
    if (decision == 'perimetro'):
        perimetro_cuadrado(lado)
    elif (decision == 'superficie'):
        superficie_cuadrado(lado)
    else:
        print('Por favor ingrese [perimetro/superficie]')
        cargar_dato()

# Bloque principal del programa

cargar_dato()

