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

def agregar(lista_usuarios):

    while True:
        nombre = input("Ingrese nombre: ")
        clave = input("Ingrese clave: ")
        fonos = input("Ingrese fonos: ")

        if validar_largo(nombre, 6):

            result = {
                        "usuario": nombre,
                        "clave" : clave,
                        "fonos": fonos,
                        "activo": False
                    }
            lista_usuarios.append(result)

            break
        else:
            print('No cumples condiciones')

    return lista_usuarios
    

def actualizar():
    pass

def eliminar(lista_usuarios, nombre_eliminar):
    controlador = True
    for indice, usuario in enumerate(lista_usuarios):
  
        if usuario['usuario'] == nombre_eliminar:
            del lista_usuarios[indice]
            controlador = True
            break
        else:
            controlador = False

    if controlador:
        print('ELIMINADO')
    else:
        print('usuario no existe')

    return lista_usuarios
    

def listar(lista):
    contador = 1 
    print(f'----Lista de usuarios----')
    for usuario in lista:
        print(f'Usuario {contador}: {usuario['usuario']}')
        contador += 1

def salir():
    print(f'Adiós administrador')

def validar_largo(cadena, largo_minimo):

    return len(cadena) >= largo_minimo
    
lista_usuarios = [{
    "usuario": "chuispe",
    "clave" : "123456",
	"fonos": [
                988778882, 
                988877776,
                877666333
             ],
	"activo": True},
    {
    "usuario": "falcantara",
    "clave" : "789789",
	"fonos": [
                999999999, 
                666666666
             ],
	"activo": False},
    {
    "usuario": "anthonyl",
    "clave" : "789789",
	"fonos": [
                999999999, 
                666666666
             ],
	"activo": False}]

while True:
    opt = opciones_menu()   
    
    if opt == 1:
        agregar(lista_usuarios)
    elif opt == 2:
        actualizar()
    elif opt == 3:
        nombre_eliminar = input('Indique el nombre de usuario a eliminar: ')

        eliminar(lista_usuarios, nombre_eliminar)
    elif opt == 4: 
        listar(lista_usuarios)
    elif opt == 5:
        salir()
        break
    else:
        print(f"{opt} es una opción incorrecta...")   