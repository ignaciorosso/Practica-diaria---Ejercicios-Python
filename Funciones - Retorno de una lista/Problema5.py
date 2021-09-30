# Desarrollar una aplicación que permita ingresar por teclado los 
# nombres de 5 artículos y sus precios.
# Definir las siguientes funciones:
# 1) Cargar los nombres de articulos y sus precios.
# 2) Imprimir los nombres y precios.
# 3) Imprimir el nombre de artículo con un precio mayor
# 4) Ingresar por teclado un importe y luego mostrar todos los 
# artículos con un precio menor igual al valor ingresado.

def ingreso_datos():
    art = []
    prec = []

    print('Ingrese articulo y su correspondiente precio')
    for x in range(5):
        art.append(input('{}- Articulo: '.format(x+1)))
        prec.append(int(input('Precio: ')))
    
    return [art, prec]

def imprimir_listas(art, prec):
    print('Lista de articulos con sus precios')
    for x in range(5):
        print('{} ${}'.format(art[x], prec[x]))

def mayor_precio(prec):
    mayor = prec[0]
    posic = 0

    for x in range(1, len(prec)):
        if (mayor <= prec[x]):
            mayor = prec[x]
            posic = x
    print('Articulo de mayor precio: {}'.format(articulo[posic]))

def articulo_menor(prec):
    menor = int(input('Ingrese un monto para obtener articulos de menor valor: '))
    for x in range(5):
        if (prec[x] <= menor):
            print('{} ${}'.format(articulo[x], prec[x]))


# Bloque principal del programa

articulo, precio = ingreso_datos()
imprimir_listas(articulo, precio)
mayor_precio(precio)
articulo_menor(precio)