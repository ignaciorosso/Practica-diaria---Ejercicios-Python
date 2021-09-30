# Crear y cargar dos listas con los nombres de 5 productos en una y sus respectivos precios en otra. Definir dos listas paralelas. Mostrar cuantos productos tienen un precio mayor al primer producto ingresado.

producto = []
precio = []

for f in range(5):
    producto.append(input('Ingrese el nombre del producto: '))
    precio.append(int(input('Ingrese el valor de dicho producto: ')))

print('El valor del primer producto ingresado es: {}'.format(precio[0]))
cont = 0
print('Productos con mayor precio que el primero: ')
for x in range(1, 5): #Iniciamos desde la posicion 1 y no desde la posicion 0 ya que no tiene sentido comparar el elemento mismo
    if(precio[x] > precio[0]):
        print(producto[x])
        cont+=1

print('Cantidad de productos con mayor precio que el primero: {}'.format(cont))