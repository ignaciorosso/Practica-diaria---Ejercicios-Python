# Se ingresan tres valores por teclado, si todos son iguales se imprime la suma del 
# primero con el segundo y a este resultado se lo multiplica por el tercero.

num1 = int(input('Ingrese el primer numero: '))
num2 = int(input('Ingrese el segundo numero: '))
num3 = int(input('Ingrese el tercer numero: '))

if (num1 == num2 and num1 == num3):
    suma = num1 + num2
    print(suma)    
    resultado = (suma) * num3
    print(resultado)
else:
    print('Lo siento, no son los numeros iguales')