# Se tiene que cargar los votos obtenidos por tres candidatos a una 
# elección.
# En una lista cargar en la primer componente el nombre del candidato 
# y en la segunda componente cargar una lista con componentes de tipo 
# tupla con el nombre de la provincia y la cantidad de votos obtenidos 
# en dicha provincia.
# Se deben cargar los datos por teclado, pero si se cargaran por asignación
#  tendría una estructura similar a esta:
# candidatos=[ ("juan",[("cordoba",100),("buenos aires",200)]) , ("ana", [("cordoba",55)]) , 
# ("luis", [("buenos aires",20)]) ]
# 1) Función para cargar todos los candidatos, sus nombres y las provincias con los 
# votos obtenidos.
# 2) Imprimir el nombre del candidato y la cantidad total de votos obtenidos en 
# todas las provincias.

def carga_datos():
    candidatos = []
    for x in range(3):
        nombre = input('Ingrese nombre del candidato: ')
        n = int(input("Ingrese la cantidad de provincias donde recibió votos: "))
        provincias = []
        for x in range(n):
            prov = input('Ingrese nombre de la provincia: ')
            votos = int(input('Ingrese cantidad de votos: '))
            provincias.append((prov, votos))
        candidatos.append((nombre, provincias))

    return candidatos 

def imprimir_datos(candidatos):
    for x in range(len(candidatos)):
        suma = 0
        for k in range(len(candidatos[x][1])):
            suma=suma+candidatos[x][1][k][1]
        print(candidatos[x][0],suma)    

# Bloque principal del programa

candidatos = carga_datos()
imprimir_datos(candidatos)