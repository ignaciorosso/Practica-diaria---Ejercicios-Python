# Desarrollar un programa que cargue una lista con 10 enteros.
# Cargar los valores aleatorios con números enteros comprendidos entre 0 y 1000.
# Mostrar la lista por pantalla.
# Luego mezclar los elementos de la lista y volver a mostrarlo.

import random

def cargar():
    lista = []
    for x in range(10):
        lista.append(random.randint(0, 1000))
    return lista

def mostrar(lista):
    print(lista)

def mezclar(lista):
    random.shuffle(lista)

# Bloque principal del programa

lista = cargar() # Al ser variable global se va modificando y no es necesario crear una nueva variable
print('Lista generada aleatoriamente')
mostrar(lista)
mezclar(lista)
print('La misma lista pero reorganizada') 
mostrar(lista)