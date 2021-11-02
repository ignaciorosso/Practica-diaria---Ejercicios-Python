# Ingresar un mail por teclado. Verificar si el string ingresado contiene solo un caracter "@".

mail = input('Ingrese su mail: ')

x = 0
cantidad = 0

while (x<len(mail)):
    if (mail[x] == "@"):
        cantidad+=1
    x+=1

if (cantidad == 1):
    print('Tu mail esta VERIFICADO')
else:
    print('Favor revisar su mail')