# Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe 
# cuántos tienen notas mayores o iguales a 7 y cuántos menores

i = 1
a = 0
d = 0

while (i <= 10):
    nota = int((input('Ingrese la nota {}: '.format(i))))
    if(nota >= 7 and nota <= 10):
        a = a + 1
    elif (nota < 7):
        d = d + 1
    else:
        i-=1
        print('Ingrese valores comprendidos entre 0 y 10')
    i+=1
print('{} alumnos tienen notas mayor o igual a 7 y \n{} tienen nota menores a 7'.format(a, d))