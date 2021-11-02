# Se ingresan tres notas de un alumno, si el promedio es mayor o igual a siete mostrar un mensaje "Promocionado".

num1 = int(input('Ingrese nota del primer parcial: '))
num2 = int(input('Ingrese nota del segundo parcial: '))
num3 = int(input('Ingrese nota del tercer parcial: '))

promedio = (num1+num2+num3)/3
if (promedio > 0 and promedio <= 10):
    if (promedio >= 7):
        print('Condicion: PROMOCIONADO\nNota igual a: {}'.format(promedio))
    else:
        print('Condicion: REGULAR\nNota igual a: {}'.format(promedio))
else:
    print('¡Favor de revisar notas ingresadas!')