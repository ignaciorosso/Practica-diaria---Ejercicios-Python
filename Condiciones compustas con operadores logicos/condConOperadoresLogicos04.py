# Escribir un programa que pida ingresar la coordenada de un punto en el plano, es decir dos 
# valores enteros x e y (distintos a cero).
# Posteriormente imprimir en pantalla en que cuadrante se ubica dicho punto. 
# (1º Cuadrante si x > 0 Y y > 0 , 2º Cuadrante: x < 0 Y y > 0, etc.)

x = int(input("Ingrese el valor de la coordenada x: "))
y = int(input("Ingrese el valor de la coordenada y: "))

if (x > 0 and y > 0):
    print('El punto se encuentra en el 1° cuadrante')
elif (x < 0 and y > 0):
    print('El punto se encuentra en el 2° cuadrante')
elif (x < 0 and y < 0):
    print('El punto se encuentra en el 3° cuadrante')
elif (x > 0 and y < 0):
    print('El punto se encuentra en el 4° cuadrante')
else:
    print('El punto se encuntra sobre un eje o en el origen')