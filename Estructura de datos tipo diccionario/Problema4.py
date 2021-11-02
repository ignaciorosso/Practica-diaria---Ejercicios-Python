# Crear un diccionario en Python que defina como clave el número de documento de una 
# persona y como valor un string con su nombre.
# Desarrollar las siguientes funciones:
# 1) Cargar por teclado los datos de 4 personas.
# 2) Listado completo del diccionario.
# 3) Consulta del nombre de una persona ingresando su número de documento.

def cargar_datos():
    personas = {}
    for x in range(4):
        nombre = input('Ingrese nombre: ')
        documento = int(input('Ingrese DNI: '))
        personas[documento] = nombre

    return personas

def imprimir(personas):
    print('-Listado de personas-')
    for documento in personas:
        print(personas[documento], documento)

def consulta_nombre(personas):
    dni = int(input('Ingrese DNI de la persona para obtener nombre: '))
    if dni in personas:
        print(dni, ': ', personas[dni], sep="")
    else:
        print('No existe persona en la lista con ese DNI')

# Bloque principal del programa

pers = cargar_datos()
imprimir(pers)
consulta_nombre(pers )