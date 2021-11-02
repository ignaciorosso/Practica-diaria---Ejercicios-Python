# Implementar la clase Operaciones. Se deben cargar dos valores enteros por teclado en el
# método __init__, calcular su suma, resta, multiplicación y división, cada una en un
# método, imprimir dichos resultados.

class Operaciones():

    def __init__(self):
        self.valor1 = int(input('Cargar un valor: '))
        self.valor2 = int(input('Cargar otro valor: '))

    def suma(self):
        suma = self.valor1 + self.valor2
        print('La suma es {}'.format(suma))

    def resta(self):
        resta = self.valor1 - self.valor2
        print('La resta es {}'.format(resta))

    def producto(self):
        prod = self.valor1 + self.valor2
        print('El producto es {}'.format(prod))

    def division(self):
        div = self.valor1 / self.valor2
        print('La division es {}'.format(div))

# Bloque principal del programa


operacion1 = Operaciones()
operacion1.suma()
operacion1.resta()
operacion1.producto()
operacion1.division()
