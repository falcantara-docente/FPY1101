def menu():
    print('========== MENÚ PRINCIPAL ==========')
    print('1. Agregar videojuego')
    print('2. Buscar videojuego')
    print('3. Eliminar videojuego')
    print('4. Actualizar disponibilidad')
    print('5. Mostrar videojuegos')
    print('6. Salir')
    print('====================================')

def opcionMenu():
    try:
        opcion = int(input('Seleccione una opción del menú: '))

        if opcion < 1 or opcion > 6:
            print(f'Error, debes indicar una opción de 1 a 6')
        else: 
            return opcion
    except ValueError:
        print('SOLO ACEPTO NUMEROS ENTEROS')

def agregarJuego(bibliotecaJuegos):
    while True: 
        nombre = input('Ingrese el nombre: ').strip().upper() #THE LAST OF US = 14
        if len(nombre) == 0:
            print('Nombre debe contener texto... no puede ser vacío.')
        else: 
            break
    while True: 
        try: 
            stock = int(input('Ingrese el stock '))
            if stock < 0:
                print(f'El stock debe ser mayor o igual que 0')
            else: 
                break
        except ValueError:
            print('Solo aceptamos numeros')

    while True: 
        try: 
            precio = float(input('Ingrese precio '))
            if precio < 0: 
                print(f'El precio no puede ser menor que 0')
            else: 
                break
        except ValueError:
            print('Solo acepto números.')
    
    estructura_dic = {
                        "titulo": nombre,
                        "precio": precio,
                        "stock": stock,
                        "disponible": False
                     }
    
    bibliotecaJuegos.append(estructura_dic)

def listarBiblioteca(biblioteca):
    if len(biblioteca) == 0:
        print('No tengo juegos en la biblioteca, debes ir a la opción de añadir (1)')
    else:
        print(f'=== LISTA DE VideoJuegos ===')
        for juego in biblioteca:
            print(f"Nombre: {juego['titulo']}")
            print(f"Stock: {juego['stock']}")
            print(f"Precio: {juego['precio']}")
            if juego['disponible']:
                print(f"Estado: DISPONIBLE")
            else:
                print(f"Estado: NO DISPONIBLE")
            print("*" * 50)

def buscarJuego(biblioteca, titulo):
    if len(biblioteca) == 0:
        print(f'No tengo juegos para buscar....')
    else:
        for posicion, juego in enumerate(biblioteca):
            if juego['titulo'] == titulo:
                controlador = posicion
                break
            else:
                controlador = -1
    return controlador

def eliminarJuego(biblioteca):

    # considere generar la validación de si existen o no registros... podría aplicar una función que valide el largo de las listas... 
    tituloEliminar = input('Ingrese el titulo que quiere eliminar: ').strip().upper()
    posicionEliminar = buscarJuego(biblioteca, tituloEliminar) 

    if posicionEliminar == -1:
        print(f"El VideoJuego {tituloEliminar} no se encuentra registrado.")
    else:
        del biblioteca[posicionEliminar]
        print(f"{tituloEliminar} eliminado de la biblioteca... ")

def updateMasivo(biblioteca):
    contador = 0

    for juego in biblioteca:
        if juego['stock'] > 0: 
            juego['disponible'] = True
            contador += 1
        else: 
            juego['disponible'] = False

    print(f"Se han actualizado {contador} juegos...")

def iniciarSoftware():

    # Esto es solo para probar... debe quedar la lista vacía al entregar el software el día de su prueba. 
    listaJuegos = [{
                        "titulo": 'THE LAST OF US',
                        "precio": 5.0,
                        "stock": 5,
                        "disponible": False
                     }]
    print(f'{listaJuegos}')

    while True:
        menu()
        opcion = opcionMenu()  

        if opcion == 1: 
            agregarJuego(listaJuegos)
        elif opcion == 2: 
            tituloBusqueda = input('Ingrese un titulo a buscar: ').strip().upper()
            posicion = buscarJuego(listaJuegos, tituloBusqueda)

            if posicion == -1: 
                print(f'No encontrado')
            else:
                print(f"{listaJuegos[posicion]}")

        elif opcion == 3: 
           eliminarJuego(listaJuegos)
        elif opcion == 4: 
            updateMasivo(listaJuegos)
        elif opcion == 5: 
            listarBiblioteca(listaJuegos)
        elif opcion == 6: 
            print('Gracias por usar el sistema. Vuelva Pronto')
            break
        
if __name__ == "__main__":
    iniciarSoftware()  