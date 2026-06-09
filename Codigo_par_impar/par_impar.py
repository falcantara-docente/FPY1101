import funciones as f

while True: 
    numeros = input("Ingrese numeros separados por espacio...: ")
    respuesta = f.validar_lista_numeros(numeros) 

    if respuesta == 0:
        print(f'----LISTA COMPLETA DE NUMEROS-----')
        print(numeros)
        print(f'----LISTA DE SEPARADOS-----')
        f.par_impar(numeros)

        break
    else:
        print(f'se han detectado {respuesta} registros invaliados')







