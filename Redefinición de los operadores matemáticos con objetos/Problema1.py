# Veamos con un ejemplo la sintaxis para redefinir el operador +.
# Crearemos una clase Cliente de un banco y redefiniremos el operador + para que nos retorne 
# la suma de los depósitos de los dos clientes que estamos sumando.

class Cliente():

    def __init__(self, nombre, monto):
        self.nombre = nombre
        self.monto = monto

    def __add__(self, objeto2): # Como parametro tambien tenemos un objeto. 
        sum = self.monto + objeto2.monto
        return sum 

# Bloque principal del programa

cliente1 = Cliente("Juan", 3000)
cliente2 = Cliente("Manuel", 1200)

print("El total depositado por los dos clientes es: ")
print(cliente1+cliente2)
