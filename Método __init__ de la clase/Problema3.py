# Desarrollar una clase que represente un Cuadrado y tenga los siguientes métodos:
# inicializar el valor del lado llegando como parámetro al método __init__
# (definir un atributo llamado lado), imprimir su perímetro y su superficie.

class Cuadrado():

    def __init__(self, lado):
        self.lado = lado

    def perimetro(self):
        per = self.lado * 4
        print('El perimetro del cuadrado es {}m'.format(per))

    def superficie(self):
        sup = self.lado ** 2
        print('La superficie del cuadrado es {}m^2'.format(sup))

# Bloque principal del programa


cuadrado1 = Cuadrado(10)
cuadrado1.perimetro()
cuadrado1.superficie()
