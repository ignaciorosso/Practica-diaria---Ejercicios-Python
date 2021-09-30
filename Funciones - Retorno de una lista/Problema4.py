# En una empresa se almacenaron los sueldos de 10 personas.
# Desarrollar las siguientes funciones y llamarlas desde el bloque principal:
# 1) Carga de los sueldos en una lista.
# 2) Impresión de todos los sueldos.
# 3) Cuántos tienen un sueldo superior a $4000.
# 4) Retornar el promedio de los sueldos.
# 5) Mostrar todos los sueldos que están por debajo del promedio.


def cargar_sueldos():
    sueldos = []
    for x in range(10):
        sueldos.append(int(input('Ingrese sueldo: ')))
    return sueldos

def imprimir_sueldos(sueldos):
    for x in range(len(sueldos)):
        print('${}'.format(sueldos[x]))

def sueldo_mayor(sueldos):
    contador = 0
    for x in range(len(sueldos)):
        if (sueldos[x] >= 4000):
            contador+=1
    print('{} sueldos mayores a $4000'.format(contador))

def sueldo_promedio(sueldos):
    suma = 0
    for x in range(len(sueldos)):
        suma = suma + sueldos[x]
    
    prom = suma/len(sueldos)
    print('El promedio de los sueldos es: ${}'.format(prom))
    return prom

def menor_promedio(sueldos, prom):
    print('Sueldos menores a {}'.format(prom))
    for x in range(len(sueldos)):
        if (sueldos[x] <= prom):
            print('${}'.format(sueldos[x]))

# Bloque principal del programa

lista_sueldos = cargar_sueldos()
imprimir_sueldos(lista_sueldos)
sueldo_mayor(lista_sueldos)
promedio = sueldo_promedio(lista_sueldos)
menor_promedio(lista_sueldos, promedio)