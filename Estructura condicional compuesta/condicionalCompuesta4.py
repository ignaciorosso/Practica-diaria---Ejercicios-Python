# Se ingresa por teclado un número positivo de uno o dos dígitos (1..99) mostrar un mensaje indicando 
# si el número tiene uno o dos dígitos.
# (Tener en cuenta que condición debe cumplirse para tener dos dígitos un número entero)

num = int(input('Ingrese un numero: '))

if (num>0 and num < 100):
    if (num < 10):
        print('El numero ingresado tiene un digito')
    else:
        print('El numero ingresado tiene dos digitos')
else:
    print('El numero ingresado debe ser entre 1 y 99')