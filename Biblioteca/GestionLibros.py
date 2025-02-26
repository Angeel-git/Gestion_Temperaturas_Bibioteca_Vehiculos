from Biblioteca.Electronicos import Electronicos
from Biblioteca.Fisicos import Fisicos


def imprimirMenu():
    print("""
    MENÚ: 
    0. SALIR DEL PROGRAMA
    1. Agregar un nuevo libro
    2. Mostrar todos los libros
    3. Actualizar un valor
    4. Eliminar un libro""")


def leerInt(mensaje):
    try:
        return int(input(mensaje))
    except:
        return -1

def datosLibro(formato):
    titulo = input("Introduzca el titulo de la obra: ")
    autor = input("Introduzca el autor de la obra: ")
    ano = leerInt("Introduzca el año de la obra: ")

    while ano == -1:    #En caso de que el user introduzca una letra
        print("El año no puede contener letras")
        ano = leerInt("Introduzca un año válido para la obra: ")

    if formato == 1:
        ubi = input("introduzca la ubicación del libro: ")
        Libro = Fisicos(titulo, autor, ano, ubi)
    else:
        form = input("introduzca el formato del libro: ")
        Libro = Electronicos(titulo, autor, ano, form)

    return Libro

def mostrarLibros():
    i = 0
    while i < len(listaLibros):
        libro = listaLibros[i]
        print(f"Libro {i}_ Título -> {libro.titulo}")
        i += 1

#MENÚ-------------------------------------------------------------------------------------------------------------------
listaLibros = []

while True:
    imprimirMenu()
    match(leerInt("Selecciona tu opcion: ")):
        case 0:
            print("SALIENDO DEL PROGRAMA...")
            exit(0)

        case 1:
            print("OPCIÓN SELECCIONADA -> AÑADIR NUEVO LIBRO A LA LISTA")

            while True:
                print("""Seleccione el tipo de libro que quiere guardar:
                    1_Libro Físico
                    2_Libro Electrónico""")

                formato = leerInt("Selecciona tu opcion: ")

                if formato == 1 or formato == 2:
                    listaLibros.append(datosLibro(formato))
                    print("Libro guardado con éxito!")
                    break
                else:
                    print("Opción no válida")

        case 2:
            print("OPCIÓN SELECCIONADA -> MOSTRAR TODOS LOS LIBROS CON SUS ATRIBUTOS")
            if len(listaLibros) == 0:
                print("No existe ningún libro registrado por el momento")
            else:
                i = 0
                while i < len(listaLibros):
                    libro = listaLibros[i]
                    print("Libro---------------------")
                    libro.mostrarInfo()
                    i += 1

        case 3:
            print("OPCIÓN SELECCIONADA -> ACTUALIZAR UN LIBRO")
            if len(listaLibros) == 0:
                print("No existe ningún libro registrado por el momento")
            else:
                mostrarLibros()
                libroActualizar = leerInt("Introduzca el libro que quiere actualizar: ")

                if libroActualizar == -1 or libroActualizar >= len(listaLibros):    #Comparamos si el valor introducido esta en la listaLibros
                    #El -1 es porque si la entrada no es válida, el metodo "leerInt()" devuelve -1
                    print("opción no válida")
                else:
                    fisico = False
                    if isinstance(listaLibros[libroActualizar], Fisicos):   #Si el libro es de tipo Fisico

                        while True:
                            fisicoElectronico = input(
                                "El libro esta guardado como un libro físico, quieres modificar este campo?"
                                "Introduzca si(Y) o no (N): ")
                            if fisicoElectronico.lower() == "y":
                                fisico = False
                                print("El libro se guardará como electrónico")

                                libro = datosLibro(2)
                                break
                            elif fisicoElectronico.lower() == "n":
                                fisico = True
                                print("El libro se guardará como físico")

                                libro = datosLibro(1)
                                break
                            else:
                                print("Debes introducir Y o N")

                        listaLibros[libroActualizar] = libro
                    else:       #Si no es Físico(es Electrónico)
                        while True:
                            fisicoElectronico = input(
                                "El libro esta guardado como un libro electrónico, quieres modificar este campo?"
                                "Introduzca si(Y) o no (N): ")
                            if fisicoElectronico.lower() == "n":
                                fisico = False
                                print("El libro se guardará como electrónico")

                                libro = datosLibro(2)
                                break
                            elif fisicoElectronico.lower() == "y":
                                fisico = True
                                print("El libro se guardará como físico")

                                libro = datosLibro(1)
                                break
                            else:
                                print("Debes introducir Y o N")

                        listaLibros[libroActualizar] = libro

                    print("Libro actualizado con éxito")
        case 4:
            print("OPCIÓN SELECCIONADA -> ELIMINAR UN LIBRO")
            if len(listaLibros) == 0:
                print("No existe ningún libro registrado por el momento")
            else:
                mostrarLibros()
                libroEliminar = leerInt("Introduzca el numero correspondiente al libro que quiere eliminar: ")
                if libroEliminar == -1 or libroEliminar >= len(listaLibros):
                    print("Opción no válida")
                else:
                    del listaLibros[libroEliminar]
                    print("LIBRO ELIMINADO CON EXITO")


        case _:
            print("Opcion no válida")