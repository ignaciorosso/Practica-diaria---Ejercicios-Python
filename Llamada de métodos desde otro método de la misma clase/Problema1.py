# Plantear una clase Operaciones que solicite en el método __init__ la carga de dos enteros
# e inmediatamente muestre su suma, resta, multiplicación y división. Hacer cada operación
# en otro método de la clase Operación y llamarlos desde el mismo método __init__

class Operaciones():

    def __init__(self):
        self.num1 = int(input('Ingrese un valor: '))
        self.num2 = int(input('Ingrese otro valor: '))
        self.sumar()
        self.restar()
        self.multiplicar()
        self.dividir()

    def sumar(self):
        suma = self.num1 + self.num2
        print('El resultado de la suma es {}'.format(suma))

    def restar(self):
        resta = self.num1 - self.num2
        print('El resultado de la resta es {}'.format(resta))

    def multiplicar(self):
        multi = self.num1 * self.num2
        print('El resultado de la multiplicacion es {}'.format(multi))

    def dividir(self):
        div = self.num1 / self.num2
        print('El resultado de la division es {}'.format(div))

# Bloque principal del programa


operacion1 = Operaciones()
