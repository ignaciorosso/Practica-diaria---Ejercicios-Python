# Elaborar una función que nos retorne el perímetro de un cuadrado pasando como parámetros el valor de un lado.

def perimetro_cuadrado(lado):
    perim = lado * 4
    return perim

# Bloque principal del programa 

valor = int(input('Ingrese lado del cuadrado para obtener su perimetro: '))
print('El perimetro es: {}'.format(perimetro_cuadrado(valor)))