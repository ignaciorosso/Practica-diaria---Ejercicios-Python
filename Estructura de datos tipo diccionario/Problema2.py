# Crear un diccionario que permita almacenar 5 artículos, utilizar como clave el 
# nombre de productos y como valor el precio del mismo.
# Desarrollar además las funciones de:
# 1) Imprimir en forma completa el diccionario
# 2) Imprimir solo los artículos con precio superior a 100.

def cargar_articulos():
    articulos = {}
    for x in range(5):
        nombre = input('Ingrese nombre articulo: ')
        valor = int(input('Ingrese precio: '))
        articulos[nombre] = valor
    return articulos

def imprimir(articulos):
    print('-Lista de articulos-')
    for clave in articulos:
        print(clave, articulos[clave])

def precio_mayor100(articulos):
    print('-Articulos con precio mayor a $100-')
    for clave in articulos:
        if (articulos[clave] > 100):
            print(clave, articulos[clave])

# Bloque principal del programa

articulos = cargar_articulos()
imprimir(articulos)
precio_mayor100(articulos)