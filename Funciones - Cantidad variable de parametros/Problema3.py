# Confeccionar una función que reciba una serie de edades 
# y me retorne la cantidad que son mayores o iguales a 18 
# (como mínimo se envía un entero a la función)

def mayoria_edad(ed1, *edades):
    cantidad = 0

    if (ed1 >= 18):
        cantidad += 1
    for x in range(len(edades)):
        if (edades[x] >= 18):
            cantidad += 1
    return cantidad

# Bloque principal del programa

lista_edades = [22, 13, 25, 10, 45, 34, 10, 77, 34, 5]

print('Cantidad de personas mayores de edad: {}'.format(mayoria_edad(18, *lista_edades)))

# Tambien se puede hacer de esta manera
print('Cantidad de personas mayores de edad: {}'.format(mayoria_edad(18, 22, 13, 25, 10, 45, 34, 10, 77, 34, 5)))