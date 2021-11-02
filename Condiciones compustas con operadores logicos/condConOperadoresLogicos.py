# Realizar un programa que pida cargar una fecha cualquiera, luego verificar si 
# dicha fecha corresponde a Navidad.


dd = int(input('Ingrese el dia: '))
mm = int(input('Ingrese el mes: '))
aaaa = int(input('Ingrese el año: '))

if (dd == 25 and mm == 12):
    print('Esta fecha corresponde a navidad del año {}'.format(aaaa))
else:
    print('Esta fecha {}/{}/{} corresponde a un dia cualquiera del año'.format(dd,mm,aaaa))
