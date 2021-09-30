# Almacenar en una lista de 5 elementos tuplas que guarden el nombre 
# de un pais y la cantidad de habitantes.
# Definir tres funciones, en la primera cargar la lista, en la segunda 
# imprimirla y en la tercera mostrar el nombre del país con mayor 
# cantidad de habitantes.

def cargar_lista():
    datos = []
    for x in range(5):
        pais = input('Ingrese nombre de pais: ')
        habitantes = int(input('Ingrese cantidad de habitantes: '))
        lugares = pais, habitantes # FORMA RESUMIDA: datos.append(pais, habitantes)
        datos.append(lugares)
    return datos

def imprimir_lista(datos):
    for x in range(len(datos)):
        print(datos[x])

def mayor_cantidad(datos):
    pos = 0
    for x in range(len(datos)):
        if (datos[x][1] > datos[pos][1]):
            pos = x
    print("El pais con mas habitantes es {} con {} habitantes".format(datos[pos][0], datos[pos][1]))

# Bloque principal del programa

datos = cargar_lista()
imprimir_lista(datos)
mayor_cantidad(datos)