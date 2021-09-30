# Crear un diccionario en Python para almacenar los datos de empleados de una empresa. 
# La clave será su número de legajo y en su valor almacenar una lista con el nombre, profesión 
# y sueldo.
# Desarrollar las siguientes funciones:
# 1) Carga de datos de empleados.
# 2) Permitir modificar el sueldo de un empleado. Ingresamos su número de legajo para buscarlo.
# 3) Mostrar todos los datos de empleados que tienen una profesión de "analista de sistemas"

def cargar_datos():
    empleados = {}
    continuar = "s"
    while (continuar == "s"):
        legajo = int(input('Ingresar legajo: '))
        lista = []
        lista.append(input('Nombre empleado: '))
        lista.append(input('Profesión del empleado: '))
        lista.append(int(input('Sueldo empleado: ')))
        empleados[legajo] = lista
        continuar = input('¿Desea cargar datos de otro empleado? [s/n] ')
    
    return empleados

def modificar_sueldos(empleados):
    legajo = int(input('Introducir legajo para buscar empleado: '))
    if legajo in empleados:
        empleados[legajo][2] = int(input('Nuevo sueldo de empleado: '))
    else: 
        print('Legajo no corresponde al registro')

def mostrar_datos(empleados):
    for legajos in empleados:
        if (empleados[legajos][1] == "analista de sistemas"):
            print(legajos, ': ', empleados[legajos][0], ' $', empleados[legajos][2], sep = "") 

def imprimir(empleados):
    print('Listado completo de empleados')
    for legajos in empleados:
        print(legajos, empleados[legajos][0], empleados[legajos][1], empleados[legajos][2])


# Bloque principal del programa

empleados = cargar_datos()
imprimir(empleados)
print('-Modificar sueldo de empleado-')
modificar_sueldos(empleados)
imprimir(empleados)
print('-Empleados \Analista de sistemas\-')
mostrar_datos(empleados)