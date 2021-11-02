# Cargar por teclado y almacenar en una lista las alturas de 5 personas (valores float)
# Obtener el promedio de las mismas. Contar cuántas personas son más altas que el promedio y cuántas más bajas.

altura = []

suma = 0

for f in range(5):
    altura.append(float(input('Ingrese altura: ')))
    suma = suma + altura[f]
    
prom = suma / 5

altas = 0
bajas = 0
for i in range(len(altura)):
    if (altura[i] > prom):
        altas+=1
    else:
        bajas+=1

print('El promedio de altura es: {}'.format(prom))
print('La cantidad de personas mas altas que el promedio es: {}'.format(altas))
print('La cantidad de personas mas bajas que el promedio es: {}'.format(bajas))