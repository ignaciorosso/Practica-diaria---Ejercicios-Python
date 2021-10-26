# Plantear una clase llamada Jugador.
# Definir en la clase Jugador los atributos nombre y puntaje, y los métodos __init__, 
# imprimir y pasar_tiempo (que debe reducir en uno la variable de clase).
# Declarar dentro de la clase Jugador una variable de clase que indique cuantos minutos falta 
# para el fin de juego (iniciarla con el valor 30)
# Definir en el bloque principal dos objetos de la clase Jugador.
# Reducir dicha variable hasta llegar a cero.

class Jugador():

    tiempo_finalizacion = 30

    def __init__(self, nombre, puntaje):
        self.nombre = nombre
        self.puntaje = puntaje
        print("Comienza la partida")

    def imprimir(self):
        print("NOMBRE DE JUGADOR: ", self.nombre)
        print("PUNTUACION: ", self.puntaje)
        print("Finalizacion del juego en {} min".format(Jugador.tiempo_finalizacion))

    def pasar_tiempo(self):
        Jugador.tiempo_finalizacion -= 1

# Bloque principal del programa 

jugador1 = Jugador("Ignacio", 200)
jugador2 = Jugador("Ana", 59)

while (Jugador.tiempo_finalizacion > 0):
    jugador1.imprimir()
    jugador2.imprimir()
    jugador1.pasar_tiempo() # Lo podemos llamar con cualquiera de los dos jugadores