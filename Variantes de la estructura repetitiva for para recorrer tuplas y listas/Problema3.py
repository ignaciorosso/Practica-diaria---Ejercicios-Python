# Definir una función que cargue una lista con palabras y la retorne.
# Luego otra función tiene que mostrar todas las palabras de la lista que tienen más de 
# 5 caracteres.


def cargar_lista():
    palabras = []
    n = int(input('Cantidad de palabras a cargar: '))
    for x in range(n):
        palabras.append(input('{}° palabra: '.format(x+1)))
    
    return palabras

def mostrar_palabras(palabras):
    print('Lista de palabras con mas de 5 caracteres: ')
    for elemento in palabras:
        if (len(elemento) > 5):
            print(elemento)



# Bloque principal del programa

palabras = cargar_lista()
mostrar_palabras(palabras)