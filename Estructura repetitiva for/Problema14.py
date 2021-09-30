# Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
# a) La cantidad de valores ingresados negativos.
# b) La cantidad de valores ingresados positivos.
# c) La cantidad de múltiplos de 15.
# d) El valor acumulado de los números ingresados que son pares.

c1, c2, c3 = 0, 0, 0
suma = 0 

for f in range(10):
    valor = int(input('Ingrese valor: '))
    if (valor > 0):
        c1+=1
    elif (valor < 0):
        c3+=1
    else:
        print('El cero no esta incluido en este ejercicio')
    if (valor%15 == 0):
        c2+=1
    if (valor%2 == 0):
        suma=suma+valor
print('Valores negativos {}\nValores positivos: {}\nMultiplos de 15: {}\nSuma acumulado valores pares: {}'.format(c3, c1, c2, suma))    