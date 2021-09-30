# Desarrollar una función que reciba una lista de string y nos retorne el que tiene más caracteres. 
# Si hay más de uno con dicha cantidad de caracteres debe retornar el que tiene un valor de componente más baja.
# En el bloque principal iniciamos por asignación la lista de string:
# palabras=["enero", "febrero", "marzo", "abril", "mayo", "junio"]
# print("Palabra con mas caracteres:",mascaracteres(palabras))


def mas_caracteres(lista):
    posicion = 0
    for k in range(1, len(palabras)):
        if (len(palabras[k]) > len(palabras[posicion])):
            posicion = k
    for x in range(len(palabras)):
        if (len(palabras[x]) == len(palabras[posicion])):       
            if(palabras[x] < palabras[posicion]):
                posicion = x     
            
    return palabras[posicion]

# Bloque princilap del programa
palabras = ["enero", "marzo", "abril", "mayo", "junio"]
print('La lista completa es: ', palabras)
print('--------------------------------------------------------')
print("Palabra con mas caracteres:",mas_caracteres(palabras))