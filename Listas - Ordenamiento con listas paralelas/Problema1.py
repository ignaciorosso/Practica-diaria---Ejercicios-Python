# Confeccionar un programa que permita cargar los nombres de 5 alumnos y sus notas respectivas. Luego ordenar las notas de mayor a menor. Imprimir las notas y los nombres de los alumnos.

alumno = []
nota = []

for f in range(5):
    alumno.append(input('Nombre del alumno: '))
    nota.append(int(input('Ingrese nota del alumno: ')))

for k in range(len(nota)-1):
    for x in range(len(nota)-k-1):
        if (nota[x] < nota[x+1]):
            aux = nota[x]
            nota[x] = nota[x+1]
            nota[x+1] = aux

            aux2 = alumno[x]
            alumno[x] = alumno[x+1]
            alumno[x+1] = aux2

for f in range(5):
    print(alumno[f], nota[f])