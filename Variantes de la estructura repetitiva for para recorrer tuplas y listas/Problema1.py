# Confeccionar un programa que permita la carga de una lista de 5 enteros por teclado.
# Luego en otras funciones:
# 1) Imprimirla en forma completa.
# 2) Obtener y mostrar el mayor.
# 3) Mostrar la suma de todas sus componentes.
# Utilizar la nueva sintaxis de for vista en este concepto.

def carga_enteros():
    enteros = []
    print('-Ingrese 5 numeros enteros-')
    for x in range(5):
        enteros.append(int(input('Numero {}: '.format(x+1))))
    return enteros

def imprimir_lista(lista):
    print('-Elementos de la lista-')
    for elemento in lista:
        print(elemento)

def mayor_elemento(lista):
    mayor = lista[0]
    for elemento in lista:
        if (mayor <= elemento):
            mayor = elemento
    print('El mayor es {}'.format(mayor)) 

def suma_elementos(lista):
    suma = 0
    for elemento in lista:
        suma = suma + elemento 
    print('La suma de los elementos de la lista es: {}'.format(suma))

# Bloque principal del programa

lista = carga_enteros()
imprimir_lista(lista)
mayor_elemento(lista)
suma_elementos(lista)