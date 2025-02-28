# Importamos la clase Ciudad
from Temps.Ciudad import Ciudad


def imprimirMenu():
    print("""
    MENU:
    0_Salir programa
    1_Agregar/Actualizar ciudad y temperaturas
    2_Mostrar temperaturas de 1 ciudad
    3_Calcular media de temperaturas de 1 ciudad
    4_Obtener max y min de temperatura de 1 ciudad
    5_Eliminar Ciudad""")


def leerOpcion():
    try:
        return int(input("Selecciona tu opcion: "))
    except:
        return -1


# Lista de tuplas para almacenar ciudades y sus objetos Ciudad
listaCiudades = []

while True:
    imprimirMenu()
    opcion = leerOpcion()

    if opcion == 0:
        exit(0)

    elif opcion == 1:
        print("Opcion 1: Agregar/Actualizar ciudad y temperaturas")
        nombreCiudad = input("Introduzca el nombre de la ciudad: ")

        # Buscar la ciudad en la lista de tuplas
        ciudad = None
        for i, (nombre, obj) in enumerate(listaCiudades):
            if nombre == nombreCiudad:
                ciudad = obj
                print("La ciudad ya está registrada, los datos se actualizarán.")
                break

        if ciudad is None:
            ciudad = Ciudad(nombreCiudad)
            listaCiudades.append((nombreCiudad, ciudad))  # Agregar como tupla

        for j in range(12):  # 12 meses
            temperaturas = []
            try:
                n = int(input(f"Introduzca el numero de temperaturas que quiere añadir al mes {j + 1}: "))
                for i in range(n):
                    while True:
                        try:
                            temperaturas.append(float(input(f"Introduzca la temperatura {i + 1}: ")))
                            break
                        except:
                            print("Tienes que introducir un número")

                ciudad.agregarTemperaturas(tuple(temperaturas), j)  # Guardamos las temperaturas como tupla
            except ValueError:
                print("Número no válido")

    elif opcion == 2:
        print("Opcion 2: Mostrar temperaturas de una ciudad")
        nombreCiudad = input("Introduzca el nombre de la ciudad: ")

        for nombre, obj in listaCiudades:
            if nombre == nombreCiudad:
                obj.mostrarTemperatura()
                break
        else:
            print("Ciudad no registrada")

    elif opcion == 3:
        print("Opción 3: Calcular media de temperaturas de un mes")
        nombreCiudad = input("Introduzca el nombre de la ciudad: ")

        for nombre, obj in listaCiudades:
            if nombre == nombreCiudad:
                try:
                    mes = int(input("Ingrese el número del mes (1-12): ")) - 1
                    if 0 <= mes < 12:
                        media = obj.calcularMedia(mes)
                        if media is not None:
                            print(f"La temperatura media en {nombreCiudad} en el mes {mes + 1} es: {media:.2f}°C")
                        else:
                            print("No hay temperaturas registradas para este mes.")
                    else:
                        print("Mes inválido.")
                except ValueError:
                    print("Debe ingresar un número válido.")
                break
        else:
            print("Ciudad no registrada.")

    elif opcion == 4:
        print("Opción 4: Obtener máxima y mínima temperatura de un mes")
        nombreCiudad = input("Introduzca el nombre de la ciudad: ")

        for nombre, obj in listaCiudades:
            if nombre == nombreCiudad:
                try:
                    mes = int(input("Ingrese el número del mes (1-12): ")) - 1
                    if 0 <= mes < 12:
                        maxTemp, minTemp = obj.obtenerMaxMin(mes)  # Se devuelve como tupla
                        if maxTemp is not None:
                            print(
                                f"En {nombreCiudad}, en el mes {mes + 1}, la temperatura máxima es {maxTemp}°C y la mínima es {minTemp}°C.")
                        else:
                            print("No hay temperaturas registradas para este mes.")
                    else:
                        print("Mes inválido.")
                except ValueError:
                    print("Debe ingresar un número válido.")
                break
        else:
            print("Ciudad no registrada.")

    elif opcion == 5:
        print("Opción 5: Eliminar una ciudad")
        nombreCiudad = input("Introduzca el nombre de la ciudad a eliminar: ")

        for i, (nombre, _) in enumerate(listaCiudades):
            if nombre == nombreCiudad:
                listaCiudades.pop(i)
                print(f"La ciudad {nombreCiudad} ha sido eliminada correctamente.")
                break
        else:
            print("La ciudad no está registrada.")

    else:
        print("Opción no válida")
