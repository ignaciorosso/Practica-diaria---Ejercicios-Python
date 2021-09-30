# Escribir un programa que lea 10 números enteros y luego muestre cuántos valores ingresados 
# fueron múltiplos de 3 y cuántos de 5. Debemos tener en cuenta que hay números que son 
# múltiplos de 3 y de 5 a la vez.

cont3 = 0
cont5 = 0
cont35 = 0

for x in range(10):
    valor = int(input('Ingrese un valor:'))
    if (valor % 3 == 0 and valor % 5 == 0):
        cont35+=1
    elif (valor % 3 == 0 ):
        cont3+=1
    elif (valor % 5 == 0 ):
        cont5+=1
    else:
        pass
print('Cantidad de numeros multiplos de 3: {}'.format(cont3))
print('Cantidad de numeros multiplos de 5: {}'.format(cont5))
print('Cantidad de numeros multiplos de 3 y 5: {}'.format(cont35))
