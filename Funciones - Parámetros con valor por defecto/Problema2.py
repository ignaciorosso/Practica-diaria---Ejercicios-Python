# Confeccionar una función que reciba entre 2 y 5 enteros. 
# La misma nos debe retornar la suma de dichos valores. 
# Debe tener tres parámetros por defecto.

def sumar(v1, v2, v3 = 0, v4 = 0, v5 = 0):
    suma = v1 + v2 + v3 + v4 + v5

    return suma

# Bloque principal del programa

print('La suma de 4 + 6 es:', sumar(4, 6))
print('La suma de 1 + 3 + 9 es:', sumar(1, 3, 9))
print('La suma de 4 + 6 - 3 es:', sumar(4, 6, -3))
print('La suma de 2 + 6 + 10 + 2 + 1 es:', sumar(2, 6, 10, 2, 1))

