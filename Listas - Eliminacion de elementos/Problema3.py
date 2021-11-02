# Crear dos listas paralelas. En la primera ingresar los nombres de empleados y en la 
# segunda los sueldos de cada empleado.
# Ingresar por teclado cuando inicia el programa la cantidad de empleados de la empresa.
# Borrar luego todos los empleados que tienen un sueldo mayor a 10000 (tanto el sueldo como su nombre)

empleados = []
sueldos = []

n = int(input('Cantidad de empleados en la empresa: '))

for k in range(n):
    empleados.append(input('Nombre del empleado: '))
    sueldos.append(int(input('Sueldo del empleado: ')))

print('Empleados de la empresa:')
for k in range(n):
    print(empleados[k], sueldos[k])

posicion = 0
while (posicion < len(sueldos)):
    if (sueldos[posicion] > 10000):
        sueldos.pop(posicion)
        empleados.pop(posicion)
    else:
        posicion+=1

print('Empleados que cobran menos de 10000:')
for k in range(len(sueldos)):
    print(empleados[k], sueldos[k])