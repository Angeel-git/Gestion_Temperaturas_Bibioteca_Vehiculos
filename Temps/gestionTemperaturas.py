#Sistema de Gestión de Temperaturas por Ciudad
#(Uso de una Única Clase y Almacenamiento en Listas, Tuplas y Diccionarios)
from Temps.Ciudad import Ciudad

ciudadTemperaturas ={}

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


#MAIN-------------------------------------------------------------------------------------------------------------------

diccionarioCiudades = {}

while True:
    imprimirMenu()
    match(leerOpcion()):
        case 0:
            exit(0)

        case 1:
            print("Opcion 1")
            nombreCiudad = input("Introduzca el nombre de la ciudad: ")

            if nombreCiudad in diccionarioCiudades:
                ciudad = diccionarioCiudades[nombreCiudad]
                print("La ciudad ya está registrada, los datos se actualizarán")
            else:
                ciudad = Ciudad(nombreCiudad)
                diccionarioCiudades[nombreCiudad] = ciudad

            for j in range(12):  # Hay 12 meses en el año
                temperaturas = []

                try:
                    n = int(input(
                        f"Introduzca el numero de temperaturas que quiere añadir al mes {j + 1}: "))  # numero de temperaturas que quiere guardar de un mes

                    for i in range(n):
                        while True:
                            try:
                                temperaturas.append(float(input(f"Introduzca la temperatura {i + 1}: ")))
                                break
                            except:
                                print("Tienes que introducir un número")

                    ciudad.agregarTemperaturas(temperaturas, j)
                except ValueError:
                    print("Numero no válido")


        case 2:
            print("Opcion 2")
            nombreCiudad = input("Introduzca el nombre de la ciudad que quiere imprimir: ")

            if nombreCiudad in diccionarioCiudades:
                diccionarioCiudades[nombreCiudad].mostrarTemperatura()
            else:
                print("Ciudad no registrada")

        case 3:
            print("Opción 3: Calcular media de temperaturas de un mes")
            nombreCiudad = input("Introduzca el nombre de la ciudad: ")

            if nombreCiudad in diccionarioCiudades:
                try:
                    mes = int(input("Ingrese el número del mes (1-12): ")) - 1
                    if 0 <= mes < 12:
                        media = diccionarioCiudades[nombreCiudad].calcularMedia(mes)
                        if media is not None:
                            print(f"La temperatura media en {nombreCiudad} en el mes {mes + 1} es: {media:.2f}°C")
                        else:
                            print("No hay temperaturas registradas para este mes.")
                    else:
                        print("Mes inválido.")
                except ValueError:
                    print("Debe ingresar un número válido.")
            else:
                print("Ciudad no registrada.")

        case 4:
            print("Opción 4: Obtener máxima y mínima temperatura de un mes")
            nombreCiudad = input("Introduzca el nombre de la ciudad: ")

            if nombreCiudad in diccionarioCiudades:
                try:
                    mes = int(input("Ingrese el número del mes (1-12): ")) - 1
                    if 0 <= mes < 12:
                        maxTemp, minTemp = diccionarioCiudades[nombreCiudad].obtenerMaxMin(mes)
                        if maxTemp is not None:
                            print(f"En {nombreCiudad}, en el mes {mes+1}, la temperatura máxima es {maxTemp}°C y la mínima es {minTemp}°C.")
                        else:
                            print("No hay temperaturas registradas para este mes.")
                    else:
                        print("Mes inválido.")
                except ValueError:
                    print("Debe ingresar un número válido.")
            else:
                print("Ciudad no registrada.")

        case 5:

            print("Opción 5: Eliminar una ciudad")
            nombreCiudad = input("Introduzca el nombre de la ciudad a eliminar: ")

            if nombreCiudad in diccionarioCiudades:
                del diccionarioCiudades[nombreCiudad]
                print(f"La ciudad {nombreCiudad} ha sido eliminada correctamente.")
            else:
                print("La ciudad no está registrada.")


        case _:
            print("Opción no válida")