# Confeccionar un programa que contenga las siguientes funciones:
# 1) Carga de una lista de 5 nombres.
# 2) Ordenar alfabéticamente la lista.
# 3) Imprimir la lista de nombres

def cargar_nombres():
    nombres = []
    for x in range(5):
        nombres.append(input('Ingrese nombre: '))
    return nombres

def ordenar_nombres(nombres):
    for k in range(4):
        for x in range(4):
            if (nombres[x] > nombres[x+1]):
                aux = nombres[x]
                nombres[x] = nombres[x+1]
                nombres[x+1] = aux

def imprimir(nombres):
    for elemento in nombres:
        print(elemento)

# Bloque principal del programa

nombres = cargar_nombres()
print('Elementos sin ordenar')
imprimir(nombres)
ordenar_nombres(nombres)
print('Elementos ordenados alfabeticamente')
imprimir(nombres)
