# Confeccionar un programa que solicite la carga de 10 valores reales por teclado. 
# Mostrar al final su suma. Definir varias líneas de comentarios indicando el nombre 
# del programa, el programador y la fecha de la última modificación. Utilizar el caracter # para los comentarios.

# Sumador de numeros
# Prog: Ignacio Rosso
# Ult. Mod. 2 jun 2021 - 12:18
suma = 0

for f in range(10):
    valor = float(input('Ingrese valores reales: '))
    suma = suma + valor

print('La suma de los 10 valores es: {}'. format(suma))