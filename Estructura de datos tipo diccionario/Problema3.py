# Desarrollar una aplicación que nos permita crear un diccionario ingles/castellano. 
# La clave es la palabra en ingles y el valor es la palabra en castellano.
# Crear las siguientes funciones:
# 1) Cargar el diccionario.
# 2) Listado completo del diccionario.
# 3) Ingresar por teclado una palabra en ingles y si existe en el diccionario mostrar 
# su traducción.

def ingresar_palabras():
    diccionario = {}
    continua = "s"
    while(continua == "s"): 
        espanol = input("Ingrese palabra en ESPAÑOL: ")
        ingles = input("Ingrese palabra en INGLES: ")
        diccionario[ingles] = espanol
        continua = input('¿Quiere ingresar otra palabra? [s/n] ')
    return diccionario

def imprimir(diccionario):
    print('-Listado de palabras-')
    for ingles in diccionario:
        print(ingles, diccionario[ingles])

def mostrar_traduccion(diccionario):
    print('-Ingrese palabra en INGLES para obtener su traduccion en ESPAÑOL-')
    nuevaPalabra = input("Ingrese palabra: ")
    if nuevaPalabra in diccionario: # El operador IN busca en todo el diccionario si la palabra EXISTE
        print(nuevaPalabra, ': ', diccionario[nuevaPalabra], sep="")
    else:
        print('La palabra no se encuentra en el listado')
# Bloque principal del programa
dicc = ingresar_palabras()
imprimir(dicc)
mostrar_traduccion(dicc)