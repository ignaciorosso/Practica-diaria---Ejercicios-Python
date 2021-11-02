name = []

for f in range(5):
    name.append(input('Ingrese nombre: '))

print('La lista de nombres:\n{}'.format(name))

name_menor = name[0]

for x in range(len(name)-1):
    if (name[x] < name_menor):
        name_menor = name[x]

print('El nombre de menor orden alfabetico es:\n{}'.format(name_menor))