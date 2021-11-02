# Confeccionar una agenda. Utilizar un diccionario cuya clave sea la fecha. 
# Permitir almacenar distintas actividades para la misma fecha (se ingresa la hora y 
# la actividad)
# Implementar las siguientes funciones:
# 1) Carga de datos en la agenda.
# 2) Listado completo de la agenda.
# 3) Consulta de una fecha.

def cargar():
    agenda = {}
    continuar1 = "s"

    while (continuar1 == "s"):
        fecha = input('Ingrese fecha en formato dd/mm/aa : ')
        continuar2 = "s"
        lista = []

        while (continuar2 == "s"):
            hora = input('Ingrese hora de actividad en fomato hh:mm : ')
            actividad = input('Ingrese la descripcion de la actividad: ')
            lista.append((hora, actividad))
            continuar2 = input('Ingresa otra actividad para la misma fecha [s/n] ')
        agenda[fecha] = lista
        continuar1 = input('Ingresar otra fecha [s/n] ')

    return agenda

def mostrar(agenda):
    print('Listado completo de las actividades')
    for fecha in agenda:
        print('Actividades de la fecha: ', fecha)
        for hora, actividad in agenda[fecha]:
            print(hora, actividad)

def mostrar_fecha(agenda):
    print('-Buscar actividada por fecha-')
    dia = input('Ingrese fecha en formato dd/mm/aa : ')
    if dia in agenda:
        for hora, actividad in agenda[dia]:
            print(hora, actividad)
    else:
        print("No hay actividad para esa fecha")

# Bloque principal del programa 

agen = cargar()
mostrar(agen)
mostrar_fecha(agen)