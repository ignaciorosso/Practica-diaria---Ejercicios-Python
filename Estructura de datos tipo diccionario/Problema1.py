# En el bloque principal del programa definir un diccionario que almacene los 
# nombres de paises como clave y como valor la cantidad de habitantes. 
# Implementar una función para mostrar cada clave y valor.

def imprimir(paises):
    for clave in paises:
        print(clave, paises[clave])


# Bloque princilal del programa

paises = {'Argentina':40000000, 'España':46000000, 'Brasil':190000000, 'Uruguay':3400000}
imprimir(paises)