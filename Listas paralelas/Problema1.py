# Desarrollar un programa que permita cargar 5 nombres de personas y sus edades respectivas. Luego de realizar la carga por teclado de todos los datos imprimir los nombres de las personas mayores de edad (mayores o iguales a 18 años)

nombre = []
edad = []

for f in range(5):
    nombre.append(input('Ingrese nombre de la persona: '))
    edad.append(int(input('Ingrese la edad de dicha persona: ')))


for x in range(len(edad)):
    if (edad[x] >= 18):
        print('{} es mayor de edad. Su edad es {}'.format(nombre[x], edad[x]))
