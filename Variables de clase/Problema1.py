# Definir una clase Cliente que almacene un código de cliente y un nombre.
# En la clase Cliente definir una variable de clase de tipo lista que almacene todos los clientes que tienen 
# suspendidas sus cuentas corrientes.
# Imprimir por pantalla todos los datos de clientes y el estado que se encuentra su cuenta corriente.


class Cliente():

    suspendidos = []

    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre 

    def imprimir(self):
        print("Codigo:", self.codigo)
        print("Nombre:", self.nombre)
        self.esta_suspendido()

    def esta_suspendido(self):
        if self.codigo in Cliente.suspendidos:
            print("Esta suspendido")
        else:
            print("Esta habilitado")

    def suspender(self):
        Cliente.suspendidos.append(self.codigo)

# Bloque principal del programa

cliente1 = Cliente(5343, "Ignacio")
cliente2 = Cliente(3454, "Juan")
cliente3 = Cliente(1211, "Veronica")

cliente1.imprimir()
cliente2.imprimir()
cliente3.imprimir()

cliente1.suspender()
cliente1.imprimir()

print(Cliente.suspendidos)