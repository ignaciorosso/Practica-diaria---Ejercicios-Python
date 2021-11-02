# Definir dos listas de 3 elementos.
# La primer lista cada elemento es una sublista con el nombre del padre y la madre de una familia.
# La segunda lista está constituida por listas con los nombres de los hijos de cada familia. 
# Puede haber familias sin hijos.
# Imprimir los nombres del padre, la madre y sus hijos.
# También imprimir solo el nombre del padre y la cantidad de hijos que tiene dicho padre.

padres = []
hijos = []

for k in range(3):
    sub_padres = []
    for x in range(1):
        sub_padres.append(input('Ingrese nombre del padre: '))
        sub_padres.append(input('Ingrese nombre de la madre: '))
        n = int(input('Ingrese la cantidad de hijos: '))
        for k in range(1):
            sub_hijos = []
            if (n != 0):
                for x in range(n):
                    sub_hijos.append(input('Ingrese nombre de hijo/a: '))
            hijos.append(sub_hijos)
    padres.append(sub_padres)

for k in range(len(padres)):
    print('Padres: {} y {}'.format(padres[k][0],padres[k][1]))
    for x in range(len(hijos[k])):
        print("Hijo:",hijos[k][x])

print("Listado del padre y cantidad de hijos que tiene")
for k in range(len(padres)):
    print('El padre: {} tiene {} hijos'.format(padres[k][0],len(hijos[k])))


# Otra forma de hacerlo

"""
padres=[]
hijos=[]
for k in range(3):
    pa=input("Ingrese el nombre del padre:")
    ma=input("Ingrese el nombre de la madre:")    
    padres.append([pa, ma])
    cant=int(input("Cuantos hijos tienen esta familia:"))
    hijos.append([])
    for x in range(cant):
        nom=input("Ingrese el nombre del hijo:")
        hijos[k].append(nom)

print("Listado del padre, madre y sus hijos")
for k in range(3):
    print("Padre:",padres[k][0])
    print("Madre:",padres[k][1])
    for x in range(len(hijos[k])):
        print("Hijo:",hijos[k][x])

print("Listado del padre y cantidad de hijos que tiene")
for x in range(3):
    print("padre:",padres[x][0])
    print("Cantidad de hijos:",len(hijos[x]))
"""