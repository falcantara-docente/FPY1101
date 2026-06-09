import funciones as f

lista_usuarios = [{
    "usuario": "Cesar Huispe",
    "clave" : "123456",
	"fonos": [
                988778882, 
                988877776,
                877666333
             ],
	"activo": True},
    {
    "usuario": "Fabián A.",
    "clave" : "789789",
	"fonos": [
                999999999, 
                666666666
             ],
	"activo": False}]

while True:
    opt = f.opciones_menu()   
    
    if opt == 1:
        nombre = input("Ingrese nombre: ")
        clave = input("Ingrese clave: ")
        fonos = input("Ingrese fonos: ")

        nuevo_usuario = f.agregar(nombre, clave, fonos)
        lista_usuarios.append(nuevo_usuario)
        print(f'Usuario agregado')

    elif opt == 2:
        f.actualizar()
    elif opt == 3:
        f.eliminar()
    elif opt == 4: 
        f.listar(lista_usuarios)
    elif opt == 5:
        f.salir()
        break
    else:
        print(f"{opt} es una opción incorrecta...")