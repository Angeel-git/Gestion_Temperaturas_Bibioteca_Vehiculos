from Coche import Coche
from Moto import Moto
from Ficheros import *
import os

def imprimirMenu():
    print("""MENÚ:
    0. SALIR DEL PROGRAMA
    1. Agregar un nuevo vehiculo al fichero
    2. Mostrar todos los vehículos del fichero
    3. Actualizar un vehículo
    4. Eliminar un vehículo existente
    5. Recuento de vehículos""")

def datosNuevoVehiculo():
    print("Seleccione el tipo de vehículo que quiere registrar")
    try:
        tipo = int(input("Introduzca Coche(0) o Moto(1):"))
        while tipo != 0 and tipo != 1:
            tipo = int(input("Tienes que introducir Coche(0) o Moto(1):"))

        if len(vehiculos) == 0:
            id = 1
        else:
            id = vehiculos[-1].id + 1

        marca = input("Introduzca la marca del vehículo que desea registrar: ")
        modelo = input("Introduzca el modelo del vehículo que desea registrar: ")
        ano = int(input("Introduzca el año de la fecha de fabricación del vehículo: "))

        if tipo == 0:
            numPuertas = int(input("Introdzca el número de puertas del coche: "))
            vehiculo = Coche(id, marca, modelo, ano, numPuertas)
        else:
            tipoMotor = input("Introduzca el tipo de motor que tiene la moto: ")
            vehiculo = Moto(id, marca, modelo, ano, tipoMotor)

        return vehiculo
    except:
        print("Tienes que introducir un número")


def modificarVehiculo(id):

    print("El vehículo que va a actualizar es: ")
    vehiculos[id - 1].mostrarDatos()


    marca = input("Introduzca la marca del vehículo que desea registrar: ")
    modelo = input("Introduzca el modelo del vehículo que desea registrar: ")
    ano = int(input("Introduzca el año de la fecha de fabricación del vehículo: "))

    coche = modificarTipoVehiculo(vehiculos[id - 1])      #Preguntamos si quiere cambiar el tipo del Vehículo

    if coche:
        numPuertas = int(input("Introdzca el número de puertas del coche: "))
        vehiculos[id - 1] = Coche(id, marca, modelo, ano, numPuertas)
    else:
        tipoMotor = input("Introduzca el tipo de motor que tiene la moto: ")
        vehiculos[id - 1] = Moto(id, marca, modelo, ano, tipoMotor)



def modificarTipoVehiculo(v):     #El metodo devuelve false si el vehículo final va a ser moto, True si va a ser coche
    if isinstance(v, Coche):  # Si el vehículo es un coche
        print("El vehículo es un coche, quiere modificar este campo?")
        modificarTipo = input("Si(Y) o No(N): ").strip().lower()
        if modificarTipo == "y":
            return False
        else:
            return True
    else:
        print("El vehículo es una moto, quiere modificar este campo?")
        modificarTipo = input("Si(Y) o No(N): ").strip().lower()
        if modificarTipo == "y":
            return True
        else:
            return False

#-----------------------------------------------------------------------------------------------------------------------
print("obteniendo los datos del fichero...")
vehiculos = []

if os.path.exists("Vehiculos.csv"): #Si el archivo existe
    vehiculos = leerFicheroCSV("Vehiculos.csv")
    if len(vehiculos) == 0:         #Si existe pero está vacio no hace nada
        print("El archivo esta vacio por el momento")
    else:                           #Si existe, y tiene datos guardados, los carga en la lista
        print("Vehículos obtenidos correctamente")

else:   #Si el archivo no existe, lo creamos en blanco
    nombreFichero = "Vehiculos.csv"
    with open(nombreFichero, "w") as fichero:
        pass
    print(f"Fichero creado en ruta: {os.path.abspath(nombreFichero)}")

while True:
    imprimirMenu()
    try:
        opcion = int(input("Selecciona tu opción: "))

        match opcion:
            case 0:
                print("Saliendo del programa...")
                exit(0)

            case 1:
                print("Guardar un nuevo vehículo en el fichero")
                vehiculo = datosNuevoVehiculo()
                vehiculos.append(vehiculo)
                guardarVehiculos("Vehiculos.csv", vehiculos)

            case 2:
                print("Mostrar los vehículos del fichero")
                for vehiculo in vehiculos:
                    vehiculo.mostrarDatos()

            case 3:
                print("Actualizar un vehículos del fichero")
                for Vehiculo in vehiculos:
                    print(f"Vehiculo {Vehiculo.id}: {Vehiculo.marca}, {Vehiculo.modelo}")
                vModificar = int(input("Introduzca el id del Vehículo que desea actualizar: "))
                modificarVehiculo(vModificar)

                guardarVehiculos("Vehiculos.csv", vehiculos)    #Actualizamos el contenido del fichero

            case 4:
                print("Eliminar un vehículos del fichero")
                for Vehiculo in vehiculos:
                    print(f"Vehiculo {Vehiculo.id}: {Vehiculo.marca}, {Vehiculo.modelo}")
                idEliminar = int(input("Introduzca el id del Vehículo que desea eliminar: "))
                vEliminar = vehiculos[idEliminar - 1]
                vehiculos.remove(vEliminar)

                guardarVehiculos("Vehiculos.csv", vehiculos)  # Actualizamos el contenido del fichero

            case 5:
                print("Recuento de vehículos")
                print(f"Total de vehículos registrados: {len(vehiculos)}")

            case _:
                print("OPCIÓN NO VÁLIDA")
    except:
        break