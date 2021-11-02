# Implementar una clase llamada Alumno que tenga como atributos su nombre y su nota.
# Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje
# si está regular (nota mayor o igual a 4)
# Definir dos objetos de la clase Alumno.

class Alumno:

    def inicializar(self, nom, no):
        self.nombre = nom
        self.nota = no

    def imprimir(self):
        print('Nombre: ', self.nombre, ' Nota: ', self.nota)

    def mostrar_regular(self):
        if (self.nota >= 4):
            print(self.nombre, ' esta REGULAR')
        else:
            print(self.nombre, ' esta LIBRE')

# Bloque principal del programa


alumno1 = Alumno()
alumno1.inicializar("Ignacio", 7)
alumno1.imprimir()
alumno1.mostrar_regular()


alumno2 = Alumno()
alumno2.inicializar("Javier", 10)
alumno2.imprimir()
alumno2.mostrar_regular()
