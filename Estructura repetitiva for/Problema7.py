# Codificar un programa que lea n números enteros y calcule la cantidad de valores mayores o 
# iguales a 1000 (n se carga por teclado)
# Este tipo de problemas también se puede resolver empleando la estructura repetitiva for. 
# Lo primero que se hace es cargar una variable que indique la cantidad de valores a ingresar. 
# Dicha variable se carga antes de entrar a la estructura repetitiva for.

n = int(input('Ingrese la cantidad de valores: '))
mayor = 0
for x in range(n):
    valor = int(input('Ingrese valor: '))
    if (valor >= 1000):
        mayor+=1
    else: 
        pass 

print('Cantidad de valores mayor o igual a 1000: {} de {} valores ingresados'.format(mayor, n) )   