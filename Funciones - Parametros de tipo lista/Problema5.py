# Definir una lista de enteros por asignación en el bloque principal. 
# Llamar a una función que reciba la lista y nos retorne el producto de todos sus elementos. 
# Mostrar dicho producto en el bloque principal de nuestro programa.

def producto_lista(list):
    producto = 1
    for k in range(len(list)):
        producto = producto * list[k]
    return producto
# Bloque principal del programa 

lista = [3, 5, 1, 23, 1]

print('La lista definida es: ', lista)
print('El producto de todos los elementos de la lista es: {}'.format(producto_lista(lista)))