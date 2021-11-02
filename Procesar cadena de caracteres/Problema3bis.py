# Una forma de recorrer la cadena de caracteres en busca de '@'
miEmail = input('Ingrese su email: ')
email = False

for i in miEmail:
    if (i == '@'):
        email = True

if (email == True): # Esto se puede simplificar escribiendo: if email  ---Esto automaticamente es lo mismo (email == True)
    print('El mail el correcto')
else:
    print('El mail es incorrecto')