# Se desea saber la temperatura media trimestral de cuatro paises. 
# Para ello se tiene como dato las temperaturas medias mensuales de dichos paises.
# Se debe ingresar el nombre del país y seguidamente las tres temperaturas medias mensuales.
# Seleccionar las estructuras de datos adecuadas para el almacenamiento de los datos en memoria.
# a - Cargar por teclado los nombres de los paises y las temperaturas medias mensuales.
# b - Imprimir los nombres de las paises y las temperaturas medias mensuales de las mismas.
# c - Calcular la temperatura media trimestral de cada país.
# d - Imprimir los nombres de los paises y las temperaturas medias trimestrales.
# e - Imprimir el nombre del pais con la temperatura media trimestral mayor.


pais = []
temperatura = []

for k in range(4):
    pais.append(input('Ingrese pais: '))

    t1 = int(input('Ingrese temperatura media mensual 1: ')) 
    t2 = int(input('Ingrese temperatura media mensual 2: ')) 
    t3 = int(input('Ingrese temperatura media mensual 3: ')) 
    temperatura.append([t1, t2, t3])

print('La temperatura de cada pais en los ultimos 3 meses es: ')
for k in range(4):
    print(pais[k], temperatura[k][0], temperatura[k][1], temperatura[k][2])


temperatura_media = []

for k in range(len(temperatura)):
    promedio = (temperatura[k][0] + temperatura[k][1] + temperatura[k][2]) / 3
    temperatura_media.append(promedio)

print('La temperatura media trimestral de cada pais es: ')
for k in range(4):
    print(pais[k], temperatura_media[k])

posicion_mayor = 0
for k in range(1, 4):
    if (temperatura_media[k] > temperatura_media[posicion_mayor]):
        posicion_mayor = k

print('El pais con mayor temperatura en los ultimos tres meses: ', pais[posicion_mayor])



