# Confeccionar una función que reciba un string como parámetro y 
# en forma opcional un segundo string con un caracter. La función 
# debe mostrar el string subrayado con el caracter que indica el 
# segundo parámetro

def texto_subrayado(texto, caracter = "-"):
    print(texto)
    print(caracter*len(texto))

# Bloque principal del programa 

texto = input('Ingrese un texto: ')
texto_subrayado(texto)

texto_subrayado("Informatica avanzada")

texto_subrayado("Analisis matematico 3", "*")