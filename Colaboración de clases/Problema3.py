# Plantear una clase Club y otra clase Socio.
# La clase Socio debe tener los siguientes atributos: nombre y la antigüedad en el club 
# (en años).
# En el método __init__ de la clase Socio pedir la carga por teclado del nombre y su 
# antigüedad.
# La clase Club debe tener como atributos 3 objetos de la clase Socio.
# Definir una responsabilidad para imprimir el nombre del socio con mayor 
# antigüedad en el club

class Socio:
    
    def __init__(self):
        self.nombre = input('Ingrese nombre del socio: ')
        self.antiguedad = int(input('Ingrese su antigüedad: '))


    def imprimir(self):
        print('El socio {} tiene {} años de antiguedad'.format(self.nombre, self.antiguedad))

    def retornar_antiguedad(self):
        return self.antiguedad
    

class Club: 

    def __init__(self):
        self.socio1 = Socio()
        self.socio2 = Socio()
        self.socio3 = Socio()

    def mayor_antiguedad(self):
        print('Socio con mayor antiguedad')
        if(self.socio1.retornar_antiguedad() > self.socio2.retornar_antiguedad() and
        self.socio1.retornar_antiguedad() > self.socio3.retornar_antiguedad()):
            self.socio1.imprimir() 
        else: 
            if (self.socio2.retornar_antiguedad() > self.socio3.retornar_antiguedad()):
                self.socio2.imprimir()
            else:
                self.socio3.imprimir()
                

# Bloque principal del programa

club1 = Club()
club1.mayor_antiguedad()