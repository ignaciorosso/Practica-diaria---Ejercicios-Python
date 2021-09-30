# Realizar un programa que imprima 25 términos de la serie 11 - 22 - 33 - 44, etc. 
# (No se ingresan valores por teclado)

i = 1
serie = 0

while (i <= 25):
    serie = serie + 11
    print('{}: {}'.format(i, serie))
    i+=1

print('El programa ha finalizado')