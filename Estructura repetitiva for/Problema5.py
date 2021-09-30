# Escribir un programa que solicite por teclado 10 notas de alumnos y nos informe 
# cuántos tienen notas mayores o iguales a 7 y cuántos menores.

cont1 = 0
cont2 = 0

for x in range(10):
    nota = int(input('Ingrese nota: '))
    if (nota >= 7 and nota <= 10):
        cont1+=1
    elif (nota > 0 and nota < 7):
        cont2+=1
    else:
        print('El valor ingresado no es correcto')
print('Cantidad de alumnos con nota mayor a 7: {}'.format(cont1))    
print('Cantidad de alumnos con nota menor a 7: {}'.format(cont2))