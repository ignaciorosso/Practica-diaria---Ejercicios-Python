# En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, 
# realizar un programa que lea los sueldos que cobra cada empleado e informe cuántos 
# empleados cobran entre $100 y $300 y cuántos cobran más de $300. Además el programa 
# deberá informar el importe que gasta la empresa en sueldos al personal.

i = 1
n = int(input('Ingrese cantidad de empleados que trabajan en la empresa: '))
n1, n2 = 0, 0 # Empleados cobran mentre 100 y 300, empleados cobran mas de 300
gasto = 0

while (i <= n):
    sueldo = int(input('Ingrese el sueldo del empleado {}: '.format(i)))
    
    if (sueldo >= 100 and sueldo <= 300):
        n1+=1
    elif (sueldo > 300 and sueldo <= 500):
        n2+=1
    else: 
        print('El sueldo ingresado esta fuera de rango')
        i-=1
    i+=1
    gasto = gasto + sueldo


print('{} empleados cobran entre $100 y $300'.format(n1))
print('{} empleados cobran mas de $300'.format(n2))
print('La empresa gasta ${} en sueldos al personal'.format(gasto))