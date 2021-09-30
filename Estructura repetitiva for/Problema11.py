# Confeccionar un programa que permita ingresar un valor del 1 al 10 y nos muestre la 
# tabla de multiplicar del mismo (los primeros 12 términos)
# Ejemplo: Si ingreso 3 deberá aparecer en pantalla los valores 3, 6, 9, hasta el 36.
while(True):
    try: #Esto nos sirve para que no nos rompan el programa metiendo cualquier cosa
        n = int(input('Ingrese un valor entre 1 y 10: '))
        if (n >= 1 and n <= 10):
            for x in range(n, n*13, n):
                print(x)
            break        
    except:
        print('Ha ocurrido un error, introduce bien el numero')
