# Desarrollar un programa que permita la carga de 10 valores por teclado y nos muestre posteriormente 
# la suma de los valores ingresados y su promedio. Este problema ya lo desarrollamos, lo resolveremos 
# empleando la estructura for para repetir la carga de los diez valores por teclado.

suma = 0

for x in range(10):
    valor = int(input('Ingrese valor: '))
    suma = suma + valor

promedio = suma / 10

print('La suma de los valores ingresados es: {}'.format(suma))
print('El promedio de los valores ingresados es: {}'.format(promedio))