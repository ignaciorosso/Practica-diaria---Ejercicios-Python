# Confeccionar una función que le enviemos un número de mes como parámetro y nos 
# retorne una tupla con todos los nombres de meses que faltan hasta fin de año.

def ingresar_mes():
    numero = int(input('Ingresar numero de mes: '))
    return numero-1 

def final_anio(numero):
    tupla = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')
    return tupla[(numero):]

def imprmir(anio):
    print('Meses que faltan para terminar el año: ')
    print(anio)
# Bloque principal del programa

print("Imprimir los nombres de meses que faltan hasta fin de año")
numero = ingresar_mes()
anio = final_anio(numero)
imprmir(anio)