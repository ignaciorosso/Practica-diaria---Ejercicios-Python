# Plantear una clase que administre dos listas de 5 nombres de alumnos y sus notas.
# Mostrar un menú de opciones que permita:
# 1- Cargar alumnos.
# 2- Listar alumnos.
# 3- Mostrar alumnos con notas mayores o iguales a 7.
# 4- Finalizar programa.

class Alumnos():

    def __init__(self):
        self.nombres = []
        self.notas = []

    def menu(self):
        opcion = 0
        while (opcion != 4):
            print('1- Cargar alumnos')
            print('2- Listar alumnos')
            print('3- Mostrar alumnos con notas mayores o iguales a 7')
            print('4- Finalizar programa')
            opcion = int(input('Ingrese numero de opcion: '))
            if(opcion == 1):
                self.cargar()
            elif (opcion == 2):
                self.lista()
            elif (opcion == 3):
                self.mostrar()


    def cargar(self):
        for x in range(5):
            self.nombres.append(input('Nombre alumno: '))
            self.notas.append(int(input('Nota alumno: ')))

    def lista(self):
        for x in range(len(self.nombres)):
            print('Alumno: {} - Nota: {}'.format(self.nombres[x], self.notas[x]))
        print('___________________________')


    def mostrar(self):
        print('Alumnos con nota mayor o igual a 7')
        for x in range(len(self.notas)):
            if (self.notas[x] >= 7):
                print(self.nombres[x], ':', self.notas[x])
        print('___________________________')

# Bloque principal del programa

alumnos1 = Alumnos()
alumnos1.menu()