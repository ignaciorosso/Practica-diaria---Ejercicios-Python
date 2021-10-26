# Desarrollar una clase llamada Lista, que permita pasar al método __init__ una lista de valores enteros.
# Redefinir los operadores +,-,* y // con respecto a un valor entero.

class Lista():

    def __init__(self, lista):
        self.lista = lista

    def imprimir(self):
        print(self.lista)

    def __add__(self, entero):
        nueva = []
        for x in range(len(self.lista)):
            nueva.append(self.lista[x]+entero)
        return nueva

    def __sub__(self, entero):
        nueva = []
        for x in range(len(self.lista)):
            nueva.append(self.lista[x]-entero)
        return nueva

    def __mul__(self, entero):
        nueva = []
        for x in range(len(self.lista)):
            nueva.append(self.lista[x]*entero)
        return nueva

    def __floordiv__(self, entero):
        nueva = []
        for x in range(len(self.lista)):
            nueva.append(self.lista[x]//entero)
        return nueva

# Bloque principal del programa 

lista1 = Lista([10, 20, 30, 40])
lista1.imprimir()
print(lista1+10) #Con esto podemos ver que no necesitamos llamar a los metodos, sino que lo estamos haciendo
print(lista1-10) # con los operadores +, -, *, //
print(lista1*10)
print(lista1//10)