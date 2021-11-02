# Confeccionar un programa que permita cargar un número entero positivo de hasta tres cifras 
# y muestre un mensaje 
# indicando si tiene 1, 2, o 3 cifras. Mostrar un mensaje de error si el número de cifras es mayor.


num = int(input('Ingrese un numero entero positivo: '))

if (num <= 99):
    if (num <= 9):
        print('Tiene 1 CIFRA')
    else:
        print('Tiene 2 CIFRAS')
else:
    if (num <= 999):
        print('Tiene 3 CIFRAS')
    else:
        print('Error')
