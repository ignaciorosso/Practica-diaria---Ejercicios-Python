# En el módulo principal importar solo la función que retorne el mayor,
# luego cargar dos enteros y mostrar el mayor de ellos

from mayormenor import mayor

print('Cargar dos enteros para determinar cual es mayor')
entero1 = int(input('Primer valor: '))
entero2 = int(input('Segundo valor: '))

mayor = mayor(entero1, entero2)
print('El valor mayor es: {}'.format(mayor))
