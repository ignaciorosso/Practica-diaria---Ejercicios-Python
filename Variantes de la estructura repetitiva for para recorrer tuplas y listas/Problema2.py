# Almacenar en una lista de 5 elementos las tuplas con el nombre de empleado y su sueldo.
# Implementar las funciones:
# 1) Carga de empleados.
# 2) Impresión de los empleados y sus sueldos.
# 3) Nombre del empleado con sueldo mayor.
# 4) Cantidad de empleados con sueldo menor a 1000.

def carga_empleados():
    empleados = []
    for x in range(5):
        nombre = input('Nombre de empleado: ')
        sueldo = int(input('Sueldo: '))
        empleados.append((nombre, sueldo))
    return empleados

def impresion(empleados):
    for elemento in empleados:
        print(elemento[0], elemento[1])

def mayor_sueldo(empleados):
    empleado = empleados[0] # Ej: ('Ignacio', 5000)
    for emple in empleados:
        if emple[1]>empleado[1]: # Compara solo la segunda posicion que es un numero entero
            empleado = emple
    print("Empleado con mayor sueldo:",empleado[0],"su sueldo es",empleado[1])


def sueldo_menor1000(empleados):
    contador = 0
    for elementos in empleados:
        if (elementos[1] < 1000):
            contador +=1
    print('Cantidad de empleados con sueldo menor a 1000: {}'.format(contador))
# Bloque principal del programa

empleados = carga_empleados()
impresion(empleados)
mayor_sueldo(empleados)
sueldo_menor1000(empleados)