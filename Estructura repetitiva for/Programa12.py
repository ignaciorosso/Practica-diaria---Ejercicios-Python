# Realizar un programa que lea los lados de n triángulos, e informar:
# a) De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados iguales), 
# isósceles (dos lados iguales), o escaleno (ningún lado igual)
# b) Cantidad de triángulos de cada tipo.

n = int(input('Cantidad de triangulos: '))
n1, n2, n3 = 0, 0, 0

for x in range(n):
    lado1 = int(input('\nIngrese el primer lado del triangulo: '))
    lado2 = int(input('Ingrese el segundo lado del triangulo: '))
    lado3 = int(input('Ingrese el tercer lado del triangulo: '))
    if (lado1 == lado2 and lado1 == lado3):
        n1+=1
        print('\nTriangulo equilatero')
    elif (lado1 == lado2 or lado1 == lado3 or lado2 == lado3):
        n2+=1
        print('\nTriangulo isósceles')
    else:
        n3+=1
        print('\nTriangulo escaleno')

print('\nTriangulo equilatero: {}\nTriangulo isósceles: {}\nTriangulo escaleno: {}'.format(n1, n2, n3))