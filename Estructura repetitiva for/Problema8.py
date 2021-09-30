# Confeccionar un programa que lea n pares de datos, cada par de datos corresponde a la medida 
# de la base y la altura de un triángulo. El programa deberá informar:
# a) De cada triángulo la medida de su base, su altura y su superficie.
# b) La cantidad de triángulos cuya superficie es mayor a 12.

n = int(input('Ingrese cantidad de pares de datos: '))
cont = 0

for x in range(n):
    base = int(input('Ingrese la medida de la base: '))
    altura = int(input('Ingrese la medida de la altura: '))

    superficie = base * altura / 2
    print('La base es: {}\nLa altura es: {}\nY la superficie es: {}'.format(base, altura, superficie))
    if (superficie  > 12):
        cont+=1
print('La cantidad de triangulos con superficie mayor a 12 es: {}'.format(cont))