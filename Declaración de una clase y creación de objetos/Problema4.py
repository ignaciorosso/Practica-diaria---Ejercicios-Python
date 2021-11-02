# Desarrollar un programa que cargue los lados de un triángulo e implemente los
# siguientes métodos: inicializar los atributos, imprimir el valor del lado mayor
# y otro método que muestre si es equilátero o no. El nombre de la clase llamarla Triangulo.

class Triangulo():

    def inicializar(self):
        self.lado1 = int(input('Ingrese primer lado del triangulo: '))
        self.lado2 = int(input('Ingrese segundo lado del triangulo: '))
        self.lado3 = int(input('Ingrese tercer lado del triangulo: '))

    def imprimir(self):
        print('Lado 1:', self.lado1)
        print('Lado 2:', self.lado2)
        print('Lado 3:', self.lado3)

    def lado_mayor(self):
        if (self.lado1 >= self.lado2 and self.lado1 >= self.lado3):
            print(self.lado1, 'es mayor')
        elif (self.lado2 >= self.lado1 and self.lado2 >= self.lado3):
            print(self.lado2, 'es mayor')
        else:
            print(self.lado3, 'es mayor')

    def es_equilatero(self):
        if (self.lado1 == self.lado2 and self.lado1 == self.lado3):
            print('Es un triangulo EQUILATERO')
        else:
            print('No es equilatero')

# Bloque principal del programa


triangulo1 = Triangulo()
triangulo1.inicializar()
triangulo1.imprimir()
triangulo1.lado_mayor()
triangulo1.es_equilatero()
