diccionario = [{
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
	"activo": False}]

controlador = True
for i in diccionario:
    print(i)

for indice, usuario in enumerate(diccionario):
    #print(f'indice {indice} || usuario {usuario}')
    if usuario['usuario'] == 'falcantara':
        del diccionario[indice]
        controlador = True
        break
    else:
        controlador = False

if controlador:
    print('Encontrado')
else:
    print('No encontrado')


for i in diccionario:
    print(i)


