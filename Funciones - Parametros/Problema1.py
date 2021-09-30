# Confeccionar una aplicación que muestre una presentación en pantalla del programa. 
# Solicite la carga de dos valores y nos muestre la suma. Mostrar finalmente un mensaje de 
# despedida del programa.

def mensaje_programa(mensaje):
    print('****************************************')
    print(mensaje)
    print('****************************************')

def carga_suma(): # En este caso a esta funcion no le pasamos valores
    valor1 = int(input('Ingrese un valor: '))
    valor2 = int(input('Ingrese otro valor: '))
    suma = valor1 + valor2 
    print('{} + {} = {}'.format(valor1, valor2, suma))

# Bloque principalS
mensaje_programa('Este programa pide al usuario ingresar dos valores para luego sumarlos')
carga_suma()
mensaje_programa('Gracias por utilizar nuesto sencillo programa')



