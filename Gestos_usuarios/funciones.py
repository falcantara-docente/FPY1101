def opciones_menu():
    print('---- MENU CRUD----')
    print('1.- Agregar')
    print('2.- Actualizar')
    print('3.- Eliminar')
    print('4.- Listar')
    print('5.- Salir')
    print('------------------')
    try:
        opt = int(input('Ingrese una opción: '))

        return opt
    except ValueError:
        print("Error en el tipo de dato ingresado")

def agregar(nombre, clave, fonos):

    #validar_usuario(nombre)
    result = {
                "usuario": nombre,
                "clave" : clave,
                "fonos": fonos,
                "activo": False
            }
    
    return result
    

def actualizar():
    pass

def eliminar():
    pass

def listar(lista):
    contador = 1 
    print(f'----Lista de usuarios----')
    for usuario in lista:
        print(f'Usuario {contador}: {usuario['usuario']}')
        contador += 1

def salir():
    print(f'Adiós administrador')

def validar_usuario():
    pass
