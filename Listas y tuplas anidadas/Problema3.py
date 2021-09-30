# Almacenar en una lista 5 empleados, cada elemento de la lista es una 
# sub lista con el nombre del empleado junto a sus últimos tres sueldos 
# (estos tres valores en una tupla)
# El programa debe tener las siguientes funciones:
# 1)Carga de los nombres de empleados y sus últimos tres sueldos.
# 2)Imprimir el monto total cobrado por cada empleado.
# 3)Imprimir los nombres de empleados que tuvieron un ingreso trimestral 
# mayor a 10000 en los últimos tres meses.
# Tener en cuenta que la estructura de datos si se carga por asignación 
# debería ser similar a:
# empleados = [["juan",(2000,3000,4233)] , ["ana",(3444,1000,5333)] ,  etc.   ]


def cargar_lista():
    empleados = []
    print('Ingrese nombre del empleado y sus ultimos 3 sueldos')
    for x in range(5):
        nombre = input('Ingrese nombre del empleado: ')
        sueldo1 = int(input('Sueldo: '))
        sueldo2 = int(input('Sueldo: '))
        sueldo3 = int(input('Sueldo: '))
        empleados.append([nombre,(sueldo1, sueldo2, sueldo3)])
    return empleados

def imprimir_total(empleados):
    for x in range(len(empleados)):
        suma = empleados[x][1][0] + empleados[x][1][1] + empleados[x][1][2]
        print('Empleado: {} cobra ${}'.format(empleados[x][0], suma))

def imprimir_mayor(empleados):
    print('Empleados con sueldo trimestral mayor a $10000')
    for x in range(len(empleados)):
        suma = empleados[x][1][0] + empleados[x][1][1] + empleados[x][1][2]
        if (suma >= 10000):
            print('Empleado: {} cobra ${}'.format(empleados[x][0], suma))

# Bloque principal del programa

lista = cargar_lista()
imprimir_total(lista)
imprimir_mayor(lista)