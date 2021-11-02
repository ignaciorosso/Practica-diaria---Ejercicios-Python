# Se carga una fecha (día, mes y año) por teclado. Mostrar un mensaje si corresponde al primer trimestre del año
# (enero, febrero o marzo) Cargar por teclado el valor numérico del día, mes y año.
# Ejemplo: dia:10 mes:2 año:2018


dd = int(input('Ingrese el dia: '))
mm = int(input('Ingrese el mes: '))
aaaa = int(input('Ingrese el año: '))

if (mm == 1 or mm == 2 or mm == 3):
    print('La fecha {} del {} de {} corresponde al primer trimestre'.format(dd,mm,aaaa))
else:
    print('La fecha no corresponde al primer trimestre del año')