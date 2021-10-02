# Confeccionar una clase que administre una agenda personal. Se debe almacenar el 
# nombre de la persona, teléfono y mail
# Debe mostrar un menú con las siguientes opciones:
# 1- Carga de un contacto en la agenda.
# 2- Listado completo de la agenda.
# 3- Consulta ingresando el nombre de la persona.
# 4- Modificación de su teléfono y mail.
# 5- Finalizar programa.

class Agenda():

    def __init__(self):
        self.agenda = {}


    def menu(self):
        opcion = 0
        while (opcion != 5):
            print('1- Carga de un contacto en la agenda')
            print('2- Listado completo de la agenda')
            print('3- Consulta ingresando el nombre de la persona')
            print('4- Modificación de su teléfono y mail')
            print('5- Finalizar programa')
            print('______________________________')
            opcion = int(input('Ingrese una opcion: '))
            if (opcion == 1):
                self.cargar()
            elif (opcion == 2):
                self.mostrar()
            elif (opcion == 3):
                self.consultar()
            elif (opcion == 4):
                self.modificar()


    def cargar(self):
        nombre = input('Nombre del contacto: ')
        telefono = int(input('Telefono: '))
        correo = input('Correo electronico: ')
        self.agenda[nombre] = (telefono, correo)
        print('______________________________')


    def mostrar(self):
        print('Listado completo de la agenda')
        for nombre in self.agenda:
            print('Nombre:', nombre)
            print('Telefono:', self.agenda[nombre][0])
            print('Email:', self.agenda[nombre][1])
            print('')


    def consultar(self):
        print('Buscar contacto')
        nombre = input('Ingrese nombre del contacto: ')
        if nombre in self.agenda:
            print('Contacto:', nombre)
            print('Telefono:', self.agenda[nombre][0])
            print('Email:', self.agenda[nombre][1])
            print('______________________________')
        else:
            print('Este contacto no se encuentra en la agenda')
            print('__________________________________________')
            self.menu()


    def modificar(self):
        print('Modificar contacto')
        nombre = input('Ingrese nombre del contacto: ')
        if nombre in self.agenda:
            telefono = int(input('Ingrese nuevo telefono: '))
            correo = input('Ingrese nuevo correo electronico: ')
            self.agenda[nombre] = (telefono, correo)
        else: 
            print('Este contacto no se encuentra en la agenda')
            print('__________________________________________')
            self.menu()


# Bloque principal del programa

agenda1 = Agenda()
agenda1.menu()