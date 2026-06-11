import funciones as f

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
    opt = f.opciones_menu()   
    
    if opt == 1:
        f.agregar(lista_usuarios)
    elif opt == 2:
        f.actualizar()
    elif opt == 3:
        nombre_eliminar = input('Indique el nombre de usuario a eliminar: ')

        f.eliminar(lista_usuarios, nombre_eliminar)
    elif opt == 4: 
        f.listar(lista_usuarios)
    elif opt == 5:
        f.salir()
        break
    else:
        print(f"{opt} es una opción incorrecta...")