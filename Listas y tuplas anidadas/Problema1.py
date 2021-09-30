# Definir una serie de listas y tuplas anidadas

empleados = ['Ignacio', 26, (18, 9, 2021)]
print(empleados)
empleados.append((19, 9, 2021))
print(empleados)

alumnos = ('Ignacio', [10, 8])
print(alumnos)

# La tupla no se puede modificar
# Pero podemos agregar elementos a la lista

alumnos[1].append(6)
print(alumnos)