# Definir una tupla con tres valores enteros. Convertir el contenido 
# de la tupla a tipo lista. Modificar la lista y luego convertir la 
# lista en tupla.

# Crear una tupla a partir de tres variables independientes el dia,
# mes y año (empaquetamiento), luego desempaquetar la tupla a otras
# tres variables independientes


fecha = (25, 6, 1995)
print('Imprimimos la tupla')
print(fecha)

# Convertimos la tupla a lista

lista_fecha = list(fecha)
print('Imprimimos la lista')
print(lista_fecha)

# Modificamos la lista
lista_fecha[2] = 2021
print('Imprimimos la lista modificada')
print(lista_fecha)

# Convertimos la lista a una tupla(Usando la primera variable declarada)
fecha = tuple(lista_fecha)
print('Imprimimos la tupla')
print(fecha)


dd = 18
mm = 9
aa = 2021

fechaActual = dd, mm, aa
print('Imprimimos la nueva tupla:')
print(fechaActual)

d, m, a = fechaActual
#Esta vez la desempaquetamos en otras variables para hacerlo mas intuitivo

print('Imprimimos la tupla desempaquetada')
print(d, m, a, sep = "/")