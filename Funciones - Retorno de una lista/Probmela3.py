# Desarrollar un programa que permita cargar 5 nombres de personas 
# y sus edades respectivas. Luego de realizar la carga por teclado 
# de todos los datos imprimir los nombres de las personas mayores 
# de edad (mayores o iguales a 18 años)
# Imprimir la edad promedio de las personas.

def carga_lista():
    nombre = []
    edad = []

    for x in range(5):
        nombre.append(input('Nombre de la persona: '))
        edad.append(int(input('Edad de la persona: ')))
    return [nombre, edad]


def mayor_edad(nombre, edad):
    mayoria_edad = 18
    
    print('Personas mayores de edad: ')
    for x in range(len(edad)):
        if (edad[x] >= mayoria_edad):
            print(nombre[x], edad[x])


def edad_promedio(edad):
    suma = 0
    for x in range(len(edad)):
        suma = suma + edad[x]
    
    promedio = suma / len(edad)
    return promedio 





# Bloque principal del programa

nombre, edad = carga_lista()
mayor_edad(nombre, edad)

prom = edad_promedio(edad)
print('La edad promedio de las personas es: {}'.format(prom))