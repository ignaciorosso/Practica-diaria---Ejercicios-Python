# Almacenar los nombres de 5 productos y sus precios. Utilizar una lista y 
# cada elemento una tupla con el nombre y el precio.
# Desarrollar las funciones:
# 1) Cargar por teclado.
# 2) Listar los productos y precios.
# 3) Imprimir los productos con precios comprendidos entre 10 y 15.

def cargar_productos():
    productos = []
    print('-Ingresamos 5 productos con sus respectivos precios-')
    for x in range(5):
        nombre = input('Nombre del producto: ')
        precio = int(input('Precio: '))
        productos.append((nombre, precio))
    return productos

def imprimir(productos):
    print('-Lista de productos-')
    for nombre, precio in productos:
        print(nombre, ': $', precio, sep="")

def precios_entre(productos):
    print('Lista de elementos comprendidos entre $10 y $15')
    for nombre, precio in productos:
        if (10 <= precio <= 15):
            print(nombre, ': $', precio, sep="")
            
# Bloque principal del programa

productos = cargar_productos()
imprimir(productos)
precios_entre(productos)