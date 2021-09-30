# Crear y cargar en un lista los nombres de 5 países y en otra lista paralela la cantidad de habitantes del mismo. Ordenar alfabéticamente e imprimir los resultados. Por último ordenar con respecto a la cantidad de habitantes (de mayor a menor) e imprimir nuevamente.


pais = []
habitante = []

for f in range(5):
    pais.append(input('Ingrese nombre del pais: '))
    habitante.append(int(input('Ingrese cantidad de habitantes: ')))

#Ordenamiento por orden alfabetico de los paises
for k in range(len(pais)-1):
    for x in range(len(pais)-k-1):
        if (pais[x] > pais[x+1]):
            aux1 = pais[x]
            pais[x] = pais[x+1]
            pais[x+1] = aux1
            
            aux2 = habitante[x]
            habitante[x] = habitante[x+1]
            habitante[x+1] = aux2

print('Ordenados alfabeticamente: ')
for f in range(5):
    print(pais[f], habitante[f])

# Ordenamiento por cantidad de habitantes
for k in range(len(habitante)-1):
    for x in range(len(habitante)-k-1):
        if (habitante[x] < habitante[x+1]):
            aux1 = habitante[x]
            habitante[x] = habitante[x+1]
            habitante[x+1] = aux1

            aux2 = pais[x]
            pais[x] = pais[x+1]
            pais[x+1] = aux2

print('Ordenados por cantidad de habitantes: ')
for f in range(5):
    print(pais[f], habitante[f])


