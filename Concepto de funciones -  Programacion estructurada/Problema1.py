# Confeccionar una aplicación que muestre una presentación en pantalla del programa. 
# Solicite la carga de dos valores y nos muestre la suma. Mostrar finalmente un 
# mensaje de despedida del programa.
# Implementar estas actividades en tres funciones.

def presentacion():
    print('Este es un programa que nos muestra la suma de dos valores')

def operacion_suma():
    valor1 = int(input('Ingrese un valor: '))
    valor2 = int(input('Ingrese otro valor: '))
    suma = valor1 + valor2
    print('{} + {} = {}'.format(valor1, valor2, suma))

def saludo_despedida():
    print('Gracias por utilizar nuestro programa')


# Bloque principal del programa
presentacion()
operacion_suma()
saludo_despedida()