# Almacenar en una lista los sueldos (valores float) de 5 operarios. Imprimir la lista y el promedio de sueldos.

sueldos = []
suma = 0

for f in range(5):
    sueldos.append(float(input('Ingrese sueldo: ')))
    suma = suma + sueldos[f]

prom = suma / 5
print('La lista de sueldo es:\n{}'.format(sueldos))
print('El promedio de los sueldos es: {}'.format(prom))
