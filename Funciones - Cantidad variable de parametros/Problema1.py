# Confeccionar una función que reciba entre 2 y n 
# (siendo n = 2,3,4,5,6 etc.) valores enteros, retornar 
# la suma de dichos parámetros.

def sumar(v1, v2, *lista):
    sumar = v1 + v2

    for x in range(len(lista)):
        sumar = sumar + lista[x]

    return sumar

# Bloque principal del programa
print('Suma de 1 + 2')
print(sumar(1, 2))
print('Suma de 1 + 2 + 3')
print(sumar(1, 2, 3))
print('Suma de 1 + 2 + 3 + 4 + 5 + 6')
print(sumar(1, 2, 3, 4, 5, 6))
