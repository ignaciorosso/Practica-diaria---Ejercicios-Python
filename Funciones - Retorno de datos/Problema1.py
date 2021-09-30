# Confeccionar una función que le enviemos como parámetro el valor del 
# lado de un cuadrado y nos retorne su superficie.

def retorno_superficie(lado):
    sup = lado * lado
    return sup


# Bloque principal del programa

valor = int(input('Ingrese el lado de un cuadrado: '))
superficie = retorno_superficie(valor)
print('La superficie del cuadrado es: {}'.format(superficie))

# Otra forma de escribirlo

"""

def retorno_superficie(lado):
    sup = lado * lado
    return sup


# Bloque principal del programa

valor = int(input('Ingrese el lado de un cuadrado: '))
print('La superficie del cuadrado es: ', retorno_superficie(valor))
"""