# Confeccionar un programa que almacene en un diccionario como clave el nombre de un 
# contacto y como valor su número telefónico:
# 1) Carga de contactos y su número telefónico.
# 2) Pemitir modificar el número telefónico. Se ingresa el nombre del contacto 
# para su búsqueda.
# 3) Imprimir la lista completa de contactos con sus números telefónicos.

def cargarContacto():
    contactos = {}
    continuar = "s"
    while (continuar == "s"):
        nombre = input('Nombre del contacto: ')
        telefono = int(input('Numero de telefono: '))
        contactos[nombre] = telefono
        continuar = input('¿Desea cargar otro contacto? [s/n] ')
    return contactos

def modificarTelefono(contactos):
    nombre = input('Ingrese nombre del contacto: ')
    if nombre in contactos:
        opcion = input('¿Desea modificar el numero de telefono de {}? [s/n] '.format(nombre))
        while (opcion == "s"):
            contactos[nombre] = int(input('Nuevo numero: '))
            break
    else:
        print('El contacto no se encuenta almacenado en la agenda')

def imprimir(contactos):
    for nombre in contactos :
        print(nombre,': ', contactos[nombre], sep="")

# Bloque principal del programa

conta = cargarContacto()
imprimir(conta)
print('-BUSCAR CONTACTO-')
modificarTelefono(conta)
imprimir(conta)