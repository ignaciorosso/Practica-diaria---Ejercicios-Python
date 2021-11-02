# Confeccionar una clase que permita carga el nombre y la edad de una persona.
# Mostrar los datos cargados. Imprimir un mensaje si es mayor de edad (edad>=18)

class Persona:

    def inicializar(self):
        self.nombre = input('Escriba el nombre de la persona: ')
        self.edad = int(input('Ingrese edad: '))

    def mostrar(self):
        print('Datos de la persona')
        print('*Nombre:', self.nombre, '*Edad:', self.edad)

    def es_mayor(self):
        if (self.edad >= 18):
            print(self.nombre, 'es MAYOR de edad')
        else:
            print(self.nombre, 'es MENOR de edad')

# Bloque principal del programa


persona1 = Persona()
persona1.inicializar()
persona1.mostrar()
persona1.es_mayor()

persona2 = Persona()
persona2.inicializar()
persona2.mostrar()
persona2.es_mayor()
