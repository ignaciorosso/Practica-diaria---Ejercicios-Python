# Se debe crear y cargar una lista donde almacenar 5 sueldos. Ordenar de menor a mayor la lista.

sueldo = []

print('Debe cargar 5 sueldos')

for f in range(5):
    sueldo.append(int(input('Ingrese sueldo: ')))

print('Lista de sueldos -sin ordenar-\n{}'.format(sueldo))

for x in range(len(sueldo)-1):
    for f in range(len(sueldo)-1):
        if (sueldo[f] > sueldo[f+1]):
            aux = sueldo[f]
            sueldo[f] = sueldo[f+1]
            sueldo[f+1] = aux

print('Lista de sueldos -ordenadas-\n{}'.format(sueldo))        