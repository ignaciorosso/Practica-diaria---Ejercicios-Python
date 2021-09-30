# Se debe crear y cargar una lista donde almacenar 5 sueldos. Desplazar el valor mayor de la lista a la última posición.

sueldo = []

print('Debemos cargar 5 sueldos')

for f in range(5):
    sueldo.append(float(input('Ingrese sueldo: ')))

print('Lista sin ordenar\n{}'.format(sueldo))

for f in range(len(sueldo)-1): # Con solo UN for solo se ordena el mayor elemento en el ultimo lugar
    if (sueldo[f] > sueldo[f+1]):
        aux = sueldo[f]
        sueldo[f] = sueldo [f+1]
        sueldo [f+1] = aux       

print('Lista con el ultimo elemento ordenado\n{}'.format(sueldo))