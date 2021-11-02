# Desarrollar una clase que represente un punto en el plano y tenga los siguientes métodos:
# inicializar los valores de x e y que llegan como parámetros, imprimir en que cuadrante se
# encuentra dicho punto (concepto matemático, primer cuadrante si x e y son positivas,
# si x<0 e y>0 segundo cuadrante, etc.)

class Punto():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        print('Coordenada del punto')
        print('(', self.x, ',', self.y, ')', sep="")

    def cuadrante(self):
        if (self.x == 0 and self.y == 0):
            print('El punto se encuentra en el ORIGEN')
        elif (self.x > 0 and self.y > 0):
            print('El punto se encuentra en el PRIMER CUADRANTE')
        elif (self.x < 0 and self.y > 0):
            print('El punto se encuentra en el SEGUNDO CUADRANTE')
        elif (self.x < 0 and self.y < 0):
            print('El punto se encuentra en el TERCER CUADRANTE')
        else:
            print('El punto se encuentra en el CUARTO CUADRANTE')

# Bloque principal del programa


punto1 = Punto(0, 0)
punto1.imprimir()
punto1.cuadrante()

punto2 = Punto(10, 50)
punto2.imprimir()
punto2.cuadrante()

punto3 = Punto(-6, 5)
punto3.imprimir()
punto3.cuadrante()

punto4 = Punto(-3, -1)
punto4.imprimir()
punto4.cuadrante()

punto5 = Punto(7, -5)
punto5.imprimir()
punto5.cuadrante()
