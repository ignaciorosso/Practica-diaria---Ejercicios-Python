# Confeccionar un programa que permita:
# 1) Cargar una lista de 10 elementos enteros.
# 2) Generar dos listas a partir de la primera. 
# En una guardar los valores positivos y en otra los negativos.
# 3) Imprimir las dos listas generadas.


def cargar_enteros():
    lista = []
    print('INGRESE 10 VALORES ENTEROS')
    for x in range(10):
        lista.append(int(input('{}- Ingrese valor: '.format(x+1))))
    
    return lista

def generador_lista(li):
    pos = []
    neg = []

    for x in range(len(li)):
        if (li[x] > 0):
            pos.append(li[x])
        elif (li[x] < 0):
            neg.append(li[x])
    return [pos, neg]

def mostrar_listas(li):
    for x in range(len(li)):
        print(li[x])

# Bloque principal del programa

lista = cargar_enteros()
positivo, negativo = generador_lista(lista)

print('Valores POSITIVOS:')
mostrar_listas(positivo)
print('Valores NEGATIVOS:')
mostrar_listas(negativo)