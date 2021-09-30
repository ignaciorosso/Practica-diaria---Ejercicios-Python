# Definir una lista que almacene por asignación los nombres de 5 personas. 
# Contar cuantos de esos nombres tienen 5 o más caracteres.

nombres = ['Juan', 'Mario', 'Luna', 'Fransisco', 'Eduardo']
cont = 0

print(nombres)

for f in range(len(nombres)):
    if (len(nombres[f]) >= 5):
        cont+=1
        print(nombres[f])
    else:
        pass

print('Cantidad de nombres con 5 o mas letras'.format(cont))