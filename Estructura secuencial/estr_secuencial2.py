# Realizar la carga del precio de un producto y la cantidad a llevar. 
# Mostrar cuanto se debe pagar (se ingresa un valor entero en el precio del producto)


precio = int(input('Ingrese el precio del producto: '))
cantidad = int(input('Ingrese la cantidad de productos: '))
if(precio>= 0 and cantidad>=0):
    importe = precio * cantidad
    print('El importe total es: ${}'.format(importe))
else:
    print('Los valores ingresados no son validos')



