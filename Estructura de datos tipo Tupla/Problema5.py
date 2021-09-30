# Confeccionar un programa con las siguientes funciones:
# 1)Cargar el nombre de un empleado y su sueldo. Retornar una tupla 
# con dichos valores
# 2)Una función que reciba como parámetro dos tuplas con los nombres 
# y sueldos de empleados y muestre el nombre del empleado con sueldo mayor.
# En el bloque principal del programa llamar dos veces a la función 
# de carga y seguidamente llamar a la función que muestra el nombre 
# de empleado con sueldo mayor.

def cargar_empleado():
    nombre = input("Ingrese nombre del empleado: ")
    sueldo = int(input('Ingrese su sueldo: '))

    return (nombre, sueldo)

def mayor_sueldo(empleado1, empleado2):
    if (empleado1[1] == empleado2[1]):
        print('Ambos empleados tiene el mismo sueldo')
    elif (empleado1[1] > empleado2[1]):
        print('{} tiene sueldo mayor'.format(empleado1[0]))
    else:    
        print('{} tiene sueldo mayor'.format(empleado2[0]))

# Bloque principal del programa

empleado1 = cargar_empleado()
empleado2 = cargar_empleado()
mayor_sueldo(empleado1,empleado2)