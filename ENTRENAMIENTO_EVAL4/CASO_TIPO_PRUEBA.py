# Esta función permite mostrar el menú.
def opcionesMenu():
    print(f'========== MENÚ PRINCIPAL ==========')
    print(f'1. Agregar libro')
    print(f'2. Buscar libro')
    print(f'3. Eliminar libro')
    print(f'4. Actualizar destacados')
    print(f'5. Mostrar libros')
    print(f'6. Salir')

# Esta función permite solicitar y registrar la opt del menú.
def optMenu():
    try:    
        opcion = int(input("Ingrese una opción... "))
        if opcion < 1 or opcion > 6:
            print(f'Error en lo ingresado... ')
        else:      
            return opcion
    except ValueError:
        print('Opción no valida...')
#función para listar Libros
def listarLibros(biblioteca):
    if len(biblioteca) > 0:
        for libro in biblioteca:
            print(libro)
    else:
        print(f"No tenemos libros disponibles...")

def validarTitulo(titulo):
    
    if len(titulo) == 0:
        return False
    else:
        return True

def cantidadPaginas(cantidadPaginas):
    return (cantidadPaginas > 0)

def puntuacion(puntuacion):
    return puntuacion > 0 and puntuacion <= 10

def agregarLibro(listaLibros):
    while True:
        nombre = input("Ingrese nombre... ").strip().upper()
        validacion = validarTitulo(nombre)
        if validacion:
            if buscarLibro(listaLibros, nombre) >= 0:
                print(f'Libro existe....')
            else:
                break
        else: 
            print('Ingrese nuevamente el nombre')
    
    while True:
        try:
            cantidad = int(input("Ingrese cantidad de páginas: "))

            validacion = cantidadPaginas(cantidad)
            if validacion:
                
                break
            else: 
                
                print('Ingrese nuevamente la cantidad de páginas')
        except ValueError:
            print("Solo debes ingresar datos numéricos.")
    
    while True:
        try:
            puntuacionLibro = int(input("Ingrese puntuacion: "))
            validacion = puntuacion(puntuacionLibro)
            if validacion:
                break
            else: 
                print('Ingrese nuevamente la puntuación')
        except ValueError:
            print("Solo debes ingresar datos numéricos.")

    estructuraLibro = {
        'titulo': nombre,
        'cantidad_paginas': cantidad,
        'puntuacion': puntuacionLibro,
        'destacado': False
        }
    
    listaLibros.append(estructuraLibro)

def buscarLibro(listaLibros, tituloBuscar):
    if len(listaLibros) == 0:
        controlador = -1 
    else:
        for indice, libro in enumerate(listaLibros):
            if libro['titulo'] == tituloBuscar:
                controlador = indice
                break
            else:
                controlador = -1
    return controlador

def updateLibros(biblioteca):
    contador = 0
    for libro in biblioteca:
        if libro['puntuacion'] >= 8: 
            libro['destacado'] = True
            contador += 1
    return contador

# Ejecución del programa
def ejecutar_software():
    biblioteca = []

    while True: 
        opcionesMenu()
        opcion_seleccionada = optMenu()

        if opcion_seleccionada == 1:
            agregarLibro(biblioteca)
        elif opcion_seleccionada == 2:
            if len(biblioteca) == 0:
                print(f'Debe ingresar libros ya que no tenemos...')
            else:
                nombreTitulo = input("Ingrese nombre a buscar: ").strip().upper()
                posicionLibro = buscarLibro(biblioteca, nombreTitulo)
                if posicionLibro >= 0:
                    print(biblioteca[posicionLibro])
                else: 
                    print(f'Libro no existe.')



        elif opcion_seleccionada == 3:
            if len(biblioteca) == 0:
                print(f'Debe ingresar libros ya que no tenemos...')
            else:
                nombreTitulo = input("Ingrese nombre a eliminar: ").strip().upper()
                posicionLibro = buscarLibro(biblioteca, nombreTitulo)
                if posicionLibro >= 0:
                    del biblioteca[posicionLibro]
                else: 
                    print(f"El libro '{nombreTitulo}' no se encuentra registrado.")
        elif opcion_seleccionada == 4:
            if len(biblioteca) == 0:
                print(f'Debe ingresar libros ya que no tenemos...')
            else:
                librosActualizados = updateLibros(biblioteca)
                print(f'Libros actualizados: {librosActualizados}')
        elif opcion_seleccionada == 5:
            listarLibros(biblioteca)
        elif opcion_seleccionada == 6:
            print("Gracias por usar el sistema de la biblioteca. Vuelva Pronto")
            break

if __name__ == "__main__":
    ejecutar_software()