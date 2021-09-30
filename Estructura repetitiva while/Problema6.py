# Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura promedio de las personas.

i = 1
suma = 0
n = int(input('Ingrese la cantidad de personas: '))

while (i <= n):
    altura = float(input('Ingrese la altura de la persona {}: '.format(i)))
    suma = suma + altura
    i+=1

promedio = suma / n
print('El promedio de altura de las {} personas ingresadas es: {}'.format(n, promedio))