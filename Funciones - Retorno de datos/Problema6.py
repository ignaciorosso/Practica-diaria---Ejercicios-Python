# Confeccionar una función que calcule la superficie de un rectángulo y la retorne, 
# la función recibe como parámetros los valores de dos de sus lados:
# def retornar_superficie(lado1,lado2):

def retornar_superficie(lado1, lado2):
    return lado1 * lado2 # Des esta manera lo hacemos de una forma mas directa sin necesidas de crear una variable

# Bloque principal del programa 
print('Ingrese ambos lados del rectangulo para obtener su superficie')
lado1 = int(input('Ingrese el valor de un lado: ')) #Estas variables se puede nombrar igual a las variables de la funcion
lado2 = int(input('Ingrese el valor de otro lado: '))

print('La superficie del rectangulo es: {} m^2'.format(retornar_superficie(lado1, lado2)))