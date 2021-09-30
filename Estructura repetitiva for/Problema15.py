# Se cuenta con la siguiente información:
# Las edades de 5 estudiantes del turno mañana.
# Las edades de 6 estudiantes del turno tarde.
# Las edades de 11 estudiantes del turno noche.
# Las edades de cada estudiante deben ingresarse por teclado.
# a) Obtener el promedio de las edades de cada turno (tres promedios)
# b) Imprimir dichos promedios (promedio de cada turno)
# c) Mostrar por pantalla un mensaje que indique cual de los tres turnos tiene un promedio de edades mayor.

suma_manana = 0
suma_tarde = 0
suma_noche = 0

for f in range(5):
    edad_manana = int(input('Ingrese edad de los estudiantes turno mañana: '))
    suma_manana = suma_manana + edad_manana

for f in range(6):
    edad_tarde = int(input('Ingrese edad de los estudiantes turno tarde: '))
    suma_tarde = suma_tarde + edad_tarde

for f in range(11):
    edad_noche = int(input('Ingrese edad de los estudiantes turno noche: '))
    suma_noche = suma_noche + edad_noche

prom_manana = suma_manana / 5
prom_tarde = suma_tarde / 6
prom_noche = suma_noche / 11

if (prom_manana > prom_tarde and prom_manana > prom_noche):
    print('El promedio de edad del turno mañana es mayor')
elif (prom_tarde > prom_manana and prom_tarde > prom_noche):
    print('El promedio de edad del turno tarde es mayor')
else:
    print('El promedio de edad del turno noche es mayor')

print('Edad promedio turno mañana: {}\nEdad promedio turno tarde: {}\nEdad promedio turno noche: {}'.format(prom_manana, prom_tarde, prom_noche))

