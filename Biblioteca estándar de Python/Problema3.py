# Confeccionar un programa que genere un número aleatorio entre 1 y 100 y no se muestre.
# El operador debe tratar de adivinar el número ingresado.
# Cada vez que ingrese un número mostrar un mensaje "Gano" si es igual al generado o 
# "El número aleatorio es mayor" o "El número aleatorio es menor".
# Mostrar cuando gana el jugador cuantos intentos necesitó.

import random

def generador():
    numero = random.randint(1, 100)
    return numero

def comparador(numero):
    nuevo_numero = int(input('Ingrese numero: '))
    intentos = 0
    while (nuevo_numero != numero):
        if (nuevo_numero > numero):
            print('El numero generado es menor al ingresado')
        else: 
            print('El numero generado es mayor al ingresado')
        intentos += 1
        nuevo_numero = int(input('Ingrese numero: '))    
    print('¡¡GANADOR!!')
    print('Cantidad de intentos: {}'.format(intentos))

# Bloque principal del programa 

numero = generador()
print('Debe tratar de adivinar el numero... ')
print('*GENERANDO NUMERO')
comparador(numero)