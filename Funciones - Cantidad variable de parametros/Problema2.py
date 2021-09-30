# Desempaquetar una lista o tupla
# Puede ser que tengamos una función que recibe una cantidad fija 
# de parámetros y necesitemos llamarla enviando valores que se 
# encuentran en una lista o tupla. La forma más sencilla es anteceder 
# el caracter * al nombre de la variable:

def sumar(v1, v2, v3):
    sumar = v1 + v2 + v3

    return sumar

# Bloque principal del programa

li = [2, 5, 6] # Puede ser tambien una TUPLA
su = sumar(*li)

print(su)

# Lo que hicimos anteriormente es lo mismo que haremos a continuacion:

print(sumar(li[0], li[1], li[2]))
# La forma anterior en una forma mas resumidad de hacer esto mismo