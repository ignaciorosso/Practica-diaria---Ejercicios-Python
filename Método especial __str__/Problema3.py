# Declarar una clase llamada Familia. Definir como atributos el nombre del padre, madre y una lista con 
# los nombres de los hijos.
# Definir el método especial __str__ que retorne un string con el nombre del padre, la madre y de 
# todos sus hijos.

class Familia():

    def __init__(self, padre, madre, hijos = []):
        self.padre = padre
        self.madre = madre
        self.hijos = hijos

    def lista(self):
        cadena = ""
        for nombre in self.hijos:
            if nombre != (self.hijos[-1]):
                cadena += nombre + ", "
            else:
                cadena += nombre
        return cadena

    def __str__(self):
        return  f"Padre: {self.padre} \n" \
                f"Madre: {self.madre} \n" \
                f"Hijos: {self.lista()}"

# Bloque principal del programa

familia1 = Familia("Lucas", "Maria", ["Elio", "Jazmin"])
print(familia1)
familia2 = Familia("Mario", "Susana")
print(familia2)
familia3 = Familia("Nestor", "Estela", ["Javier", "Alcides", "Ignacio"])
print(familia3)