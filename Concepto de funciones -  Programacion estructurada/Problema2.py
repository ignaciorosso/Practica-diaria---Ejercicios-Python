# Confeccionar una aplicación que solicite la carga de dos valores enteros y muestre su suma.
# Repetir la carga e impresion de la suma 5 veces.
# Mostrar una línea separadora después de cada vez que cargamos dos valores y su suma.

def carga_suma():
    valor1 = int(input('Ingrese un valor: '))
    valor2 = int(input('Ingrese otro valor: '))
    suma = valor1 + valor2 
    print('{} + {} = {}'.format(valor1, valor2, suma))

def separador():
    print('**************************')


# Bloque principal del programa
for x in range(5):
    carga_suma()
    separador()