# Definir una lista y almacenar los nombres de 3 empleados.
# Por otro lado definir otra lista y almacenar en cada elemento una sublista 
# con los números de días del mes que el empleado faltó.
# Imprimir los nombres de empleados y los días que faltó.
# Mostrar los empleados con la cantidad de inasistencias.
# Finalmente mostrar el nombre o los nombres de empleados que faltaron menos días.

empleados = []
faltas = []

for k in range(3):
    empleados.append(input('Ingrese nombre empleado: '))
    cantidad = int(input('¿Cuantos dias faltó el empleado? '))
    sub_faltas = []
    for x in range(cantidad):
        sub_faltas.append(int(input('Dias que faltó el empleado: ')))
    faltas.append(sub_faltas)
    

print('Nombre de empleado y dias que faltó')
for k in range(3):
    print(empleados[k])
    for x in range(len(faltas[k])):
        print(faltas[k][x])

print('Nombre del empleado y cantidad de inasistencias: ')
for k in range(3):
    print(empleados[k], len(faltas[k]))

menor = len(faltas[0])
for x in range(1, 3):
    if (len(faltas[x]) < menor):
        menor = len(faltas[x])

print('Empleado o empleados que faltaron menos: ')
for x in range(x):
    if (len(faltas[x]) == menor):
        print(empleados[x])