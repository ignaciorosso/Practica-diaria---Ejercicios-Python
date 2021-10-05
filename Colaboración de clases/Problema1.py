# Un banco tiene 3 clientes que pueden hacer depósitos y extracciones. 
# También el banco requiere que al final del día calcule la cantidad de dinero que hay 
# depositado.
# Lo primero que hacemos es identificar las clases:
# Podemos identificar la clase Cliente y la clase Banco.
# Luego debemos definir los atributos y los métodos de cada clase:
"""
Cliente		
    atributos
        nombre
        monto
    métodos
        __init__
        depositar
        extraer
        retornar_monto

Banco
    atributos
        3 Cliente (3 objetos de la clase Cliente)
    métodos
        __init__
        operar
        depositos_totales
"""

class Cliente(): 

    def __init__(self, nombre):
        self.nombre = nombre
        self.monto = 0


    def depositar(self, monto):
        self.monto += monto


    def extraer(self, monto):
        self.monto -= monto


    def retornar_monto(self):
        return self.monto


    def imprimir(self):
        print('{} tiene depositado la suma de ${}'.format(self.nombre, self.monto))

class Banco():

    def __init__(self):
        self.cliente1 = Cliente("Ignacio")
        self.cliente2 = Cliente("Juan")
        self.cliente3 = Cliente("Fernando")

    def operar(self):
        self.cliente1.depositar(20000)
        self.cliente2.extraer(1000)
        self.cliente3.depositar(5000)
        self.cliente2.depositar(3000)

    def depositos_totales(self):
        total = self.cliente1.retornar_monto() + self.cliente2.retornar_monto() + self.cliente3.retornar_monto()
        print('El total del dinero en el banco es: ${}'.format(total))
        self.cliente1.imprimir()
        self.cliente2.imprimir()
        self.cliente3.imprimir()

# Bloque principal del programa

banco1 = Banco()
banco1.operar()
banco1.depositos_totales()