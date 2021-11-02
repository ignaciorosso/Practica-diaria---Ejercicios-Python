# Se desea almacenar los datos de 3 alumnos. Definir un diccionario cuya clave sea el 
# número de documento del alumno. Como valor almacenar una lista con componentes de tipo 
# tupla donde almacenamos nombre de materia y su nota.
# Crear las siguientes funciones:
# 1) Carga de los alumnos (de cada alumno solicitar su dni y los nombres de las 
# materias y sus notas)
# 2) Listado de todos los alumnos con sus notas
# 3) Consulta de un alumno por su dni, mostrar las materias que cursa y sus notas.


def cargar_datos():
    alumnos = {}
    print('-Ingrese datos de 3 alumnos-')
    for x in range(3):
        documento = int(input('Numero de documento: '))
        lista = []
        continuar = "s"
        while (continuar == "s"):
            materia = input('Nombre de la materia: ')
            nota = int(input('Nota del alumno en {}: '.format(materia)))
            lista.append((materia, nota))
            continuar = input('¿Desea cargar nota de otra materia? [s/n] ')
        alumnos[documento] = lista
    return alumnos

def listado_notas(alumnos):
    for documento in alumnos:
        print('Las notas del alumno {} son: '.format(documento))
        for materia, notas in alumnos[documento]:
            print(materia, notas)

def consulta_alumno(alumnos):
    dni = int(input('Ingrese DNI del alumno: '))
    if dni in alumnos:
        for materia, notas in alumnos[dni]:
            print(materia, notas)
    else:
        print("El alumno no se encuentra en el listado")


# Bloque principal del programa
alumn = cargar_datos()
listado_notas(alumn)
consulta_alumno(alumn)