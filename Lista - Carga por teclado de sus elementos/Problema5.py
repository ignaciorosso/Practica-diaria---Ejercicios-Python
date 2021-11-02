# Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8 empleados 
# (4 por la mañana y 4 por la tarde) Confeccionar un programa que permita almacenar 
# los sueldos de los empleados agrupados en dos listas.
# Imprimir las dos listas de sueldos.

manana = []
tarde = []

print('Ingrese sueldo de los empleados turno mañana')

for f in range(4):
    manana.append(float(input('Ingrese sueldo: ')))

print('Ingrese sueldo de los empleados turno tarde')    

for f in range(4):    
    tarde.append(float(input('Ingrese sueldo: ')))

print('Sueldo de los empleados turno (mañana): {}'.format(manana))
print('Sueldo de los empleados turno (tarde): {}'.format(tarde))