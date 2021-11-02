# Confeccionar un programa que permita cargar un código de producto 
# como clave en un diccionario. Guardar para dicha clave el nombre del producto, 
# su precio y cantidad en stock.
# Implementar las siguientes actividades:
# 1) Carga de datos en el diccionario.
# 2) Listado completo de productos.
# 3) Consulta de un producto por su clave, mostrar el nombre, precio y stock.
# 4) Listado de todos los productos que tengan un stock con valor cero.

def cargar():
    productos = {}
    continuar = "s"

    while (continuar == "s"):
        codigo = int(input('Ingrese codigo: '))
        nombre = input('Ingrese nombre: ')
        precio = int(input('Precio: '))
        cantidad = int(input('Cantidad: '))
        productos[codigo] = (nombre, precio, cantidad)

        continuar = input('¿Desea seguir cargando productos? [s/n] ')
    
    return productos

def imprimir(productos):
    print('-Listado completo de productos-')
    for clave in productos:
        print(clave, productos[clave][0], productos[clave][1], productos[clave][2])

def mostrar(productos):
    cla = int(input('Ingrese clave del producto: '))
    if cla in productos: 
        print(productos[cla][0], productos[cla][1], productos[cla][2])
    else:
        print('El producto no se encuentra en la lista')

def valor_nulo(productos):
    print('-Listado de productos sin stock-')
    for clave in productos:
        if(productos[clave][2] == 0):
            print(clave, productos[clave][0], productos[clave][1])
    

# Bloque principal del programa

produ = cargar()
imprimir(produ)
mostrar(produ)
valor_nulo(produ)