# Mostrar los múltiplos de 8 hasta el valor 500. Debe aparecer en pantalla 8 - 16 - 24, etc.
"""
mult = 0
i = 1
while (mult < 500):
    mult = i * 8
    i+=1
    if (mult <= 500):
        print(mult)
print('El programa ha finalizado')
"""

mult = 8
while (mult <= 500):
    print(mult)
    mult = mult + 8

print('El programa ha finalizado')
