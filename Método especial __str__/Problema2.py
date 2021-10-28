# Definir una clase llamada Punto con dos atributos x e y.
# Crearle el método especial __str__ para retornar un string con el formato (x,y).


class Punto():

    def __init__(self, x = 0, y = 0): # Si no le pasamos uno de los dos parametros por defecto tenemos 0
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

# Bloque principal del programa

punto1 = Punto(4,7)
print(punto1)
punto2 = Punto()
print(punto2) # Aca vemos que si no le pasamos valores a los parametros nos improme (0,0)