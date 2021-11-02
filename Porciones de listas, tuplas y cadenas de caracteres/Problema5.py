# Cargar una cadena por teclado luego:
# 1) Imprimir los dos primeros caracteres.
# 2) Imprimir los dos últimos
# 3) Imprimir todos menos el primero y el último caracter.

cadena = input('Ingrese un texto: ')

# LOS DOS PRIMEROS CARACTERES:
print(cadena[:2])

# LOS DOS ULTIMOS
print(cadena[(len(cadena)-2):])

# SIN EL PRIMERO Y SIN EL ULTIMO
print(cadena[1:(len(cadena)-1)])
