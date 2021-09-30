# Resolveremos el mismo problema anterior pero definiendo dos alias para las funciones
# sqrt y pow del módulo math.

from math import sqrt as raiz, pow as elevar

# Definición de alias para una funcionalidad

valor = int(input('Ingrese un valor: '))

valor1 = raiz(valor)
print('La raiz cuadrada de {} es {}'.format(valor, valor1))

valor2 = elevar(valor, 3)
print('El resultado de elevar al cubo {} es {}'.format(valor, valor2))
