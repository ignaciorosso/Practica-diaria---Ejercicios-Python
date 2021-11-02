# Se tiene que cargar la siguiente información:
# · Nombres de 3 empleados
# · Ingresos en concepto de sueldo, cobrado por cada empleado, en los últimos 3 meses.
# Confeccionar el programa para:
# a) Realizar la carga de los nombres de empleados y los tres sueldos por cada empleado.
# b) Generar una lista que contenga el ingreso acumulado en sueldos en los últimos 3 meses para cada empleado.
# c) Mostrar por pantalla el total pagado en sueldos a cada empleado en los últimos 3 meses
# d) Obtener el nombre del empleado que tuvo el mayor ingreso acumulado

nombre = []
sueldo = []

for f in range(3):
    nombre.append(input('Ingrese nombre de empleado: '))
    mes1 = int(input('Ingrese sueldo primer mes: '))
    mes2 = int(input('Ingrese sueldo segundo mes: '))
    mes3 = int(input('Ingrese sueldo tercer mes: '))
    sueldo.append([mes1, mes2, mes3])

total_sueldo = []

for k in range(len(sueldo)):
    total_sueldo.append(sueldo[k][0] + sueldo[k][1] + sueldo[k][2])

print(total_sueldo)

for k in range(len(total_sueldo)):
    print(nombre[k], total_sueldo[k])


mayor = total_sueldo[0] 
indice = 0
for k in range(1, len(total_sueldo)): # Arranca de ! y no de 0. Esto hace que no se compare el primer elemento consigo mismo 
    if (mayor < total_sueldo[k]):
        mayor = total_sueldo[k]
        indice = k

print('El empleado con mayor ingreso es los ultimos 3 meses: {}\nCon un sueldo de: {}'.format(nombre[indice], mayor))
