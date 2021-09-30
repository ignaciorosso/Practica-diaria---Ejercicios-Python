# Confeccionar un programa que solicite la carga de un valor entero por teclado y
# luego nos muestre la raíz cuadrada del número y el valor elevado al cubo.
# Para resolver este problema utilizaremos dos funcionalidades que nos provee
# el módulo math de la biblioteca estándar de Python.

from math import sqrt, pow

valor = int(input('Ingrese un valor: '))

raiz = sqrt(valor)
print('La raiz cuadrada de {} es {}'.format(valor, raiz))

cubo = pow(valor, 3)
print('El resultado de elevar al cubo {} es {}'.format(valor, cubo))
