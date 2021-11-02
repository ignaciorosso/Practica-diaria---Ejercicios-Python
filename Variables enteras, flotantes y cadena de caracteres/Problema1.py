# Realizar la carga de enteros por teclado. Preguntar después que ingresa el valor si 
# desea cargar otro valor debiendo el operador ingresar la cadena 'si' o 'no' por teclado.
# Mostrar la suma de los valores ingresados.

opcion = "si"
suma = 0
while (opcion == "si"):
    valor = int(input('Ingrese valor: '))
    caracter = input('Desea ingresar otro valor [si/no]: ')
    opcion = caracter.lower()
    suma = suma + valor

print('La suma de los valores ingresados es: {}'.format(suma))
