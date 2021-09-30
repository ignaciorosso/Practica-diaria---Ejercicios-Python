# Una planta que fabrica perfiles de hierro posee un lote de n piezas.
# Confeccionar un programa que pida ingresar por teclado la cantidad de piezas a 
# procesar y luego ingrese la longitud de cada perfil; sabiendo que la pieza cuya 
# longitud esté comprendida en el rango de 1.20 y 1.30 son aptas. Imprimir por pantalla 
# la cantidad de piezas aptas que hay en el lote.

i = 1
cantidad = 0

n = int(input('Ingrese la cantidad de piezas: '))

while(i<=n):
    largo = float(input('Ingrese largo de la barra {}: '.format(i)))
    if (1.20 <= largo <= 1.30):
        cantidad+=1
    i+=1

print('La cantidad de piezas aptas es: {}'.format(cantidad))