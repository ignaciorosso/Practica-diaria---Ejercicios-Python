# Solicitar por teclado la cantidad de empleados que tiene la empresa. 
# Crear y cargar una lista con todos los sueldos de dichos empleados. 
# Imprimir la lista de sueldos ordenamos de menor a mayor.

n = int(input('¿Cuantos empleados tiene la empresa? '))
sueldo = []

for f in range(n):
    sueldo.append(int(input('Ingrese sueldo empleado {}: '.format(f+1))))

print('Lista de sueldos -sin ordenar-\n{}'.format(sueldo))

for k in range(len(sueldo)-1):
    for x in range(len(sueldo)-k-1):
        if(sueldo[x] > sueldo[x+1]):
            aux = sueldo[x]
            sueldo[x] = sueldo[x+1]
            sueldo[x+1] = aux

print('Lista de sueldos -ordenada-\n{}'.format(sueldo))