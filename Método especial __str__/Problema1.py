# ¿Qué sucede cuando llamamos a la función print y le pasamos como parámetro un objeto?

class Persona():
    
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

# Si queremos que se muestre el nombre y el apellido separado por una coma, definimos:

    def __str__(self):
        cadena = self.nombre + ", " + self.apellido
        return cadena


persona1 = Persona("Ignacio", "Rosso")
print(persona1) # Nos muestra el lugar en memoria. No se puede imprimir el objeto en si. (Debemos definir 
# el metodo __str__)

# Tambien podemos hacer esto

persona2 = Persona("Ana", "Martinez")
persona3 = Persona("Lula", "Depetris")
print(str(persona2) + " - " + str(persona3))