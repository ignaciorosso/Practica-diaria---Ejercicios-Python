# Elaborar una función que muestre la tabla de multiplicar del 
# valor que le enviemos como parámetro. Definir un segundo parámetro 
# llamado termino que por defecto almacene el valor 10. Se deben mostrar 
# tantos términos de la tabla de multiplicar como lo indica el segundo 
# parámetro.
# Llamar a la función desde el bloque principal de nuestro programa con 
# argumentos nombrados.

def tabla_multiplicar(valor, termino = 10):
    for x in range(1, termino):
        mult = x * valor 
        print(valor, "{} = {}".format(x, mult), sep = " x ", )

# Bloque principal del programa

tabla_multiplicar(5)
tabla_multiplicar(termino = 50, valor = 2)
tabla_multiplicar(3,16)