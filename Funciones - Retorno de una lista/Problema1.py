# Confeccionar una función que cargue por teclado una lista de 5 enteros y la retorne. 
# Una segunda función debe recibir una lista y mostrar todos los valores mayores a 10. 
# Desde el bloque principal del programa llamar a ambas funciones.

def cargar_lista():
    lista = []
    for k in range(5):
        lista.append(int(input('Ingrese numero entero: ')))
    return lista

def mayor_diez(li):
    lista_mayor = []
    for k in range(len(li)):
        if (li[k] > 10):
            lista_mayor.append(li[k])
    return lista_mayor


# Bloque principal del programa

print('Ingrese 5 valores enteros')
lista = cargar_lista()
print('Los valores de la lista son: ',lista)
print('La nueva lista con valores mayor a 10 es: {}'.format(mayor_diez(lista)))