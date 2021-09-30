# Confeccionar una función que reciba tres enteros y los muestre ordenados de menor a mayor. 
# En otra función solicitar la carga de 3 enteros por teclado y proceder a llamar a la primer función definida.

def ordenar_enteros(en1, en2, en3):
    if (en1 == en2 and en1 == en3):
        print('Los numeros ingresados son iguales')
    elif (en1 < en2 and en1 < en3):
        if (en2 < en3):
            print('Los valores ordenados de menor a mayor: \n{}\n{}\n{}'.format(en1, en2, en3))
        else:
            print('Los valores ordenados de menor a mayor: \n{}\n{}\n{}'.format(en1, en3, en2))
    elif (en2 < en1 and en2 < en3):
        if (en1 < en3):
            print('Los valores ordenados de menor a mayor: \n{}\n{}\n{}'.format(en2, en1, en3))
        else:
            print('Los valores ordenados de menor a mayor: \n{}\n{}\n{}'.format(en2, en3, en2))
    elif (en3 < en1 and en3 < en2):
        if (en1 < en2):
            print('Los valores ordenados de menor a mayor: \n{}\n{}\n{}'.format(en3, en1, en2))
        else:
            print('Los valores ordenados de menor a mayor: \n{}\n{}\n{}'.format(en3, en2, en1))

def solicitar_carga():
    entero1 = int(input('Ingrese un numero entero: '))
    entero2 = int(input('Ingrese un numero entero: '))
    entero3 = int(input('Ingrese un numero entero: '))
    ordenar_enteros(entero1, entero2, entero3)

# Bloque principal del programa

solicitar_carga()