# Desarrollar un programa que permita cargar n números enteros y luego nos informe cuántos valores fueron 
# pares y cuántos impares.
# Emplear el operador “%” en la condición de la estructura condicional (este operador 
# retorna el resto de la división de dos valores, por ejemplo 11%2 retorna un 1):

n = int(input('Ingrese la cantidad de valores: '))
npar = 0
nimpar = 0
i = 1

while (i <= n):
    valor = int(input('Ingrese valor: '))
    i+=1
    if(valor%2 == 0):
        npar = npar + 1
    else:
        nimpar = nimpar + 1
print('Cantidad de valores pares: {} \nCantidad de valores impares: {}'.format(npar, nimpar))