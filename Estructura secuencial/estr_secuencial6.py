# Calcular el sueldo mensual de un operario conociendo la cantidad de horas trabajadas y el valor por hora.

horas_trabajadas = int(input('Ingrese la cantidad de horas trabajadas: '))
valor_hora = float(input('Valor por hora: '))

salario_mensual = horas_trabajadas * valor_hora

print('Su salario mensual es: ${} con {}hs trabajadas en el mes20'.format(salario_mensual, horas_trabajadas))