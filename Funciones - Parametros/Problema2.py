# Confeccionar una función que reciba tres enteros y nos muestre el mayor de ellos. 
# La carga de los valores hacerlo por teclado.

def mostrar_mayor(valor1, valor2, valor3):   
    if (valor1 == valor2 and valor1 == valor3):
        print('Los valores ingresados son iguales')
    elif (valor1 > valor2 and valor1 > valor3):
        print('El primer valor ingresado es el mayor {}'.format(valor1))
    elif (valor2 > valor1 and valor2 > valor3):
        print('El segundo valor ingresado es el mayor {}'.format(valor2))
    else:
        print('El tercer valor ingresado es el mayor {}'.format(valor3)) 


def cargar():
    v1 = int(input('Ingrese primer valor: ')) # Estas son variables locales de la funcion
    v2 = int(input('Ingrese primer valor: '))
    v3 = int(input('Ingrese primer valor: '))
    mostrar_mayor(v1, v2, v3)


# Bloque principal del programa
cargar()