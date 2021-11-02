# Crear y cargar una lista con los nombres de tres alumnos. Cada alumno tiene dos notas, 
# almacenar las notas en una lista paralela. Cada componente de la lista paralela debe ser 
# también una lista con las dos notas. Imprimir luego cada nombre y sus dos notas.
"""
nombre = []
nota = []

for f in range(3):
    nombre.append(input('Nombre alumno: '))
    par_nota = []
    nota.append(par_nota)
    for f in range(1):
        par_nota.append(int(input('Nota 1: ')))
        par_nota.append(int(input('Nota 2: ')))

print(nombre)
print(nota)

for x in range(3):
    print(nombre[x], nota[x][0], nota[x][1])
"""
# Otra forma de resolverlo

nombre = []
nota = []

for x in range(3):
    nombre.append(input('Ingrese nombre: '))
    no1 = int(input('Ingrese la primer nota: '))
    no2 = int(input('Ingrese la segunda nota: '))
    nota.append([no1, no2])

for x in range(3):
    print(nombre[x], nota[x][0], nota[x][1])
