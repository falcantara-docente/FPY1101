diccionario = [{
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

for nombres in diccionario:
    print(f'User: {nombres['usuario']}')

new_user = {
    "usuario": "f.guajardo",
    "clave" : "asdfgh",
	"fonos": [],
	"activo": False}

diccionario.append(new_user)

print(f'-----------------------------------')

for nombres in diccionario:
    print(f'User: {nombres['usuario']}')
print(f'-----------------------------------')

nombre = input("Ingrese nombre: ")
clave = input("Ingrese clave: ")
fonos = input("Ingrese fonos: ")


new_user2 = {
    "usuario": nombre,
    "clave" : clave,
	"fonos": fonos,
	"activo": False}

diccionario.append(new_user2)

print(f'-----------------------------------')

for nombres in diccionario:
    print(f'User: {nombres['usuario']}')
