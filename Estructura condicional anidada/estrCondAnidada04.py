# Un postulante a un empleo, realiza un test de capacitación, se obtuvo la siguiente información: 
# cantidad total de preguntas que se le realizaron y la cantidad de preguntas que contestó correctamente. 
# Se pide confeccionar un programa que ingrese los dos datos por teclado e informe el nivel del mismo según 
# el porcentaje de respuestas correctas que ha obtenido, y sabiendo que:

'''
Nivel máximo:	Porcentaje>=90%.
Nivel medio:	Porcentaje>=75% y <90%.
Nivel regular:	Porcentaje>=50% y <75%.
Fuera de nivel:	Porcentaje<50%.

'''

total_preguntas = int(input('Ingrese el total de preguntas: '))
respondidas_bien = int(input('Ingrese la cantidad de preguntas que fueron bien respondidas: '))

porcentaje = (respondidas_bien * 100)/total_preguntas

if (porcentaje < 90):
    if(porcentaje < 75):
        if (porcentaje < 50):
            print('Fuera de NIVEL')
        else:
            print('Nivel Regular')
    else: 
        print('Nivel MEDIO')
else:
    print('Nivel MAXIMO')        
