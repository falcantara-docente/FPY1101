def validar_lista_numeros(lista_numeros):
    lista_numeros = lista_numeros.split()
    print(f'Validando... conversión...')
    print(f'{lista_numeros}')
    contador_letras = 0
    for numero in lista_numeros:
        try:
            if not numero.isdigit():
                contador_letras += 1
            elif not int(numero).is_integer():
                contador_letras += 1
        except:
            print('ERROR en FOR')
    
    return contador_letras

def par_impar(lista_numeros):
    lista_numeros = lista_numeros.split()
    print(f'Llegando..........')
    print(type(lista_numeros))
    print(lista_numeros)
    
    pares = []
    impares = []

    for numero in lista_numeros:
        if int(numero) % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    
    print(f' Impares {impares}')
    print(f' Pares {pares}')
    