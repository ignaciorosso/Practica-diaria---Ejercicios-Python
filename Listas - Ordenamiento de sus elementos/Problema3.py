# Crear una lista y almacenar los nombres de 5 países. Ordenar alfabéticamente la lista e imprimirla

pais = []

print('Escribir 5 paises')

for f in range(5):
    pais.append(input("Nombre pais: "))

print('Lista paises -sin ordenar-\n{}'.format(pais))

for k in range(len(pais)-1): # Ordena la lista conformada con datos tipo string en orden alfabetico
    for x in range(len(pais)-k-1):
        if (pais[x] > pais[x+1]): # Como python diferencia entre mayusculas y minusculas pone en primer lugar a las mayusculas
            aux = pais[x]
            pais[x] = pais[x+1]
            pais[x+1] = aux

print('Lista paises -ordenados-\n{}'.format(pais))