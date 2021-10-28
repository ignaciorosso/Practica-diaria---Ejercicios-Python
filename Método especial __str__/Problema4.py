# Desarrollar un programa que implemente una clase llamada Jugador.
# Definir como atributos su nombre y puntaje.
# Codificar el método especial __str__ que retorne el nombre y si es principiante 
# (menos de 1000 puntos) o experto (1000 o más puntos)

class Jugador():

    def __init__(self, nombre, puntaje = 0):
        self.nombre = nombre
        self.puntaje = puntaje

    def nivel_jugador(self):
        if (self.puntaje < 1000):
            return f"Principiante"
        else:
            return f"Experto"
    
    def __str__(self):
        return  f"Nombre: {self.nombre} \n" \
                f"Puntaje: {self.puntaje} \n" \
                f"Puntaje: {self.nivel_jugador()}" 

# Bloque principal del programa

jugador1 = Jugador("Ignacio", 1500)
print(jugador1)
jugador2 = Jugador("Mariano", 200)
print(jugador2)
jugador3 = Jugador("Claudio")
print(jugador3)