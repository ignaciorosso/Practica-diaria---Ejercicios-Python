# Confeccionar una función que reciba el nombre de un operario, 
# el pago por hora y la cantidad de horas trabajadas. 
# Debe mostrar su sueldo y el nombre. Hacer la llamada de 
# la función mediante argumentos nombrados.

def trabajador(nombre, pagoHora, cantidadHoras):
    sueldo = cantidadHoras * pagoHora

    print('{} trabajó {}hs y cobra un sueldo de ${}'.format(nombre, pagoHora, sueldo))

# Bloque principal del programa

trabajador("Ignacio", 250, 160)
trabajador(pagoHora = 400, nombre = "Alberto", cantidadHoras = 180)
trabajador(cantidadHoras = 190, pagoHora = 270, nombre = "Ricardo")