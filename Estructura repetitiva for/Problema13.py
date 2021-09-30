# Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos en el plano.
# Informar cuántos puntos se han ingresado en el primer, segundo, tercer y cuarto
# cuadrante. Al comenzar el programa se pide que se ingrese la cantidad de puntos a procesar.

n = int(input('Ingrese cantidad de coordenadas: '))

c1, c2, c3, c4, c = 0, 0, 0, 0, 0

for f in range(n):
    x = int(input('Ingrese coordenada de X: '))
    y = int(input('Ingrese coordenada de Y: '))
    if(x > 0 and y > 0):
        c1+=1
        print('\nPunto ubicado en primer cuadrante\n')
    elif(x < 0 and y > 0):
        c2+=1
        print('\nPunto ubicado en segundo cuadrante\n')    
    elif(x < 0 and y < 0):
        c3+=1
        print('\nPunto ubicado en tercer cuadrante\n')
    elif(x > 0 and y < 0):
        c4+=1
        print('\nPunto ubicado en cuarto cuadrante\n')
    else:
        print('\nPunto ubicado en el origen\n')
        c+=1

print('Primer cuadrante: {}\nSegundo cuadrante: {}\nTercer cuadrante: {}\nCuarto cuadrante: {}\nOrigen:{}'.format(c1, c2, c3, c4, c))    