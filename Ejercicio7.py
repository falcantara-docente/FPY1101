import math as m

while True: 
    try: 
        print("1.- Perimetro")
        print("2.- Area")
        print("3.- Salir")

        menu_principal = int(input("Ingrese una opción: "))

        if menu_principal == 1:
            print("Calculo de perimetro")

            while True:
                print("1.- Círculo")
                print("2.- Rectángulo")
                print("3.- Cuadrado")
                print("4.- Volver al menú principal")
                menu_interno = int(input("Ingrese una opción: "))

                if menu_interno == 1: 
                    radio = float(input("ingrese el radio... "))
                    perimetro = 2*m.pi*radio
                    #print(f'El resultado es: {perimetro:.2f}')
                    print(f'El resultado es: {round(perimetro,4)}')

                elif menu_interno == 2: 
                    base = float(input("ingrese base... "))
                    altura = float(input("ingrese la altura... "))
                    perimetro = 2*(base+altura)
                    print(f'El resultado es: {round(perimetro,4)}')
                elif menu_interno == 3: 
                    largo = float(input("Ingrese el valor de uno de los lados... "))
                    perimetro = 4*largo
                    print(f'El resultado es: {round(perimetro,4)}')
                elif menu_interno == 4: 
                    break
                else:
                    print("Error, intente nuevamente....")
        elif menu_principal == 2: 
            print("Calculo del area")
            while True:
                print("1.- Círculo")
                print("2.- Rectángulo")
                print("3.- Cuadrado")
                print("4.- Volver al menú principal")
                menu_interno = int(input("Ingrese una opción: "))

                if menu_interno == 1: 
                    while True:
                        radio = float(input("ingrese el radio... "))
                        if radio > 0:
                            area = m.pi*radio**2
                            #print(f'El resultado es: {perimetro:.2f}')
                            print(f'El resultado es: {round(area,4)}')
                            break
                        else: 
                            print("Ingres nuevamente un valor, pero positivo")
                    
                elif menu_interno == 2: 
                    base = float(input("ingrese base... "))
                    altura = float(input("ingrese la altura... "))
                    area = base*altura
                    print(f'El resultado es: {round(area,4)}')
                elif menu_interno == 3: 
                    largo = float(input("Ingrese el valor de uno de los lados... "))
                    area = largo**2
                    print(f'El resultado es: {round(area,4)}')
                elif menu_interno == 4: 
                    break
                else:
                    print("Error, intente nuevamente....")
        elif menu_principal == 3: 
            print("Saliendo...")
            break
        else:
            print("Opción no valida...intente nuevamente")
    except ValueError:
        print("Error en el tipo de dato")