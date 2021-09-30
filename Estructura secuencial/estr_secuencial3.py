# Realizar la carga del lado de un cuadrado, mostrar por pantalla el perímetro del mismo 
# (El perímetro de un cuadrado se calcula multiplicando el valor del lado por cuatro)

lado = float(input('Ingresa el largo de un lado del cuadrado: '))

if(lado>0):
    perim = 4 * lado
    print('El perimetro total del cuadado es: {}'.format(perim))
else:
    print('¡Favor de ingresar bien la medida!')

