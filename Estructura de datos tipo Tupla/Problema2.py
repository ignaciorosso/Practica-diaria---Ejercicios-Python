# Desarrollar una función que solicite la carga del dia, mes y año 
# y almacene dichos datos en una tupla que luego debe retornar. 
# La segunda función a implementar debe recibir una tupla con la fecha 
# y mostrarla por pantalla.

def creaciom_tupla():
    dd = int(input('Ingrese el dia: '))
    mm = int(input('Ingrese el mes: '))
    aa = int(input('Ingrese el año: '))

    return (dd, mm, aa)

def imprimir_tupla(fecha):
    print('La fecha elegida es: {} de {} del año {}'.format(fecha[0], fecha[1], fecha[2]))
    # Otra manera de imprimir la fecha
    print(fecha[0], fecha[1], fecha[2], sep = "/")

# Bloque principal del programa 


fecha = creaciom_tupla()
imprimir_tupla(fecha)
