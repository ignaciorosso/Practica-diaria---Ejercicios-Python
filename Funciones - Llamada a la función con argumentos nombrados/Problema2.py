# Cargar una lista de 10 enteros, luego mostrarlos por 
# pantalla a cada elemento separados por una coma.

def carga_enteros():
    enteros = []
    
    print('-INGRESE 10 VALORES ENTEROS-')
    
    for x in range(10):
        enteros.append(int(input('{}°- valor: '.format(x+1))))
    return enteros

def imprimir(lista):
    for x in range(len(lista)):
        if (x == 9):
            print(lista[x])
        else:
            print(lista[x], end=", ")


# Bloque principal del programa

lista = carga_enteros()
imprimir(lista)
