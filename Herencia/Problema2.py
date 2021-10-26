# Ahora plantearemos otro problema empleando herencia. Supongamos que necesitamos implementar dos clases que llamaremos Suma y Resta. 
# Cada clase tiene como atributo valor1, valor2 y resultado. Los métodos a definir son cargar1 (que inicializa el atributo valor1), carga2 
# (que inicializa el atributo valor2), operar (que en el caso de la clase "Suma" suma los dos atributos y en el caso de la clase "Resta" hace 
# la diferencia entre valor1 y valor2), y otro método mostrar_resultado.

# Si analizamos ambas clases encontramos que muchos atributos y métodos son idénticos. En estos casos es bueno definir una clase padre que agrupe dichos 
# atributos y responsabilidades comunes.

# La relación de herencia que podemos disponer para este problema es:
"""
                                        Operacion

                        Suma                              Resta
"""
# Solamente el método operar es distinto para las clases Suma y Resta (esto hace que no lo podamos disponer en la clase Operacion en principio), 
# luego los métodos cargar1, cargar2 y mostrar_resultado son idénticos a las dos clases, esto hace que podamos disponerlos en la clase Operacion. 
# Lo mismo los atributos valor1, valor2 y resultado se definirán en la clase padre Operacion.

class Operacion():

    def __init__(self):
        self.valor = 0
        self.valor2 = 0
        self.resultado = 0

    def cargar1(self):
        self.valor1 = int(input('Ingrese primer valor: '))
    
    def cargar2(self):
        self.valor2 = int(input('Ingrese segundo valor: '))

    def imprimir(self):
        print("El resultado es: {}".format(self.resultado))

class Suma(Operacion):
    
    def __init__(self):
        super().cargar1()
        super().cargar2()
    
    def sumar(self):
        self.resultado = self.valor1 + self.valor2

class Resta(Operacion):

    def __init__(self):
        super().cargar1()
        super().cargar2()

    def restar(self):
        self.resultado = self.valor1 - self.valor2

# Bloque principal del programa

operacion1 = Suma()
operacion1.sumar()
print("-SUMA-")
operacion1.imprimir()
operacion1 = Resta()
operacion1.restar()
print("-RESTA-")
operacion1.imprimir()

