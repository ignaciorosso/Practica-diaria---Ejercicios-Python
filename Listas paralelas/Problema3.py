# En un curso de 4 alumnos se registraron las notas de sus exámenes y se deben procesar de acuerdo a lo siguiente:
# a) Ingresar nombre y nota de cada alumno (almacenar los datos en dos listas paralelas)
# b) Realizar un listado que muestre los nombres, notas y condición del alumno. En la condición, colocar "Muy Bueno" si la nota es mayor o igual a 8, "Bueno" si la nota está entre 4 y 7, y colocar "Insuficiente" si la nota es inferior a 4.
# c) Imprimir cuantos alumnos tienen la leyenda “Muy Bueno”.

alumno = []
nota = []

for f in range(4):
    alumno.append(input('Ingrese nombre del alumno: '))
    nota.append(int(input('Ingrese nota del alumno: ')))

cont = 0
for x in range(4):
    if (nota[x] >= 8 and nota[x] <= 10):
        print('Alumno: {}\nNota: {}\nCondicion: Muy bueno'.format(alumno[x], nota[x]))
        cont+=1
    elif (nota[x] >= 4 and nota[x] <= 7):
        print('Alumno: {}\nNota: {}\nCondicion: Bueno'.format(alumno[x], nota[x]))
    elif (nota[x] > 0 and nota[x] < 4):
        print('Alumno: {}\nNota: {}\nCondicion: Insuficiente'.format(alumno[x], nota[x]))


print('{} alumnos tienen condicion: MUy bien'.format(cont))