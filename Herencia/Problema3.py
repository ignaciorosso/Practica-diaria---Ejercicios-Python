# Declarar una clase Cuenta y dos subclases CajaAhorra y PlazoFijo. Definir los atributos y métodos comunes entre una caja de 
# ahorro y un plazo fijo y agruparlos en la clase Cuenta.
# Una caja de ahorro y un plazo fijo tienen un nombre de titular y un monto. Un plazo fijo añade un plazo de imposición en días 
# y una tasa de interés. Hacer que la caja de ahorro no genera intereses.
# En el bloque principal del programa definir un objeto de la clase CajaAhorro y otro de la clase PlazoFijo.

class Cuenta():

    def __init__(self, nombre, monto):
        self.nombre = nombre
        self.monto = monto

    def imprimir(self):
        print("Nombre titular: ", self.nombre)
        print("Monto: ", self.monto)

class CajaAhorro(Cuenta):

    def __init__(self, nombre, monto):
        super().__init__(nombre, monto)
    
    def imprimir(self):
        print("-CUENTA CAJA DE AHORRO-")
        super().imprimir()


class PlazoFijo(Cuenta):

    def __init__(self, nombre, monto, imposicion, interes):
        super().__init__(nombre, monto)
        self.imposicion = imposicion
        self.interes = interes

    def imprimir(self):
        print("-CUENTA PLAZO FIJO-")
        super().imprimir()
        print("Imposicion: ", self.imposicion)
        print("Interes: ", self.interes)
        self.ganacia()

    def ganacia(self):
        self.liquidacion = ((self.monto * self.interes)/12) + self.monto 
        print("Liquidacion plazo fijo {} dias: ${}".format(self.imposicion, self.liquidacion))

# Bloque principal del programa

caja_ahorro = CajaAhorro("Ignacio", 200)
caja_ahorro.imprimir()
plazo_fijo = PlazoFijo("Ignacio", 19000, 30, .20)
plazo_fijo.imprimir()

