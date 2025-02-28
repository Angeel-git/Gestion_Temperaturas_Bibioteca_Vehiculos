from Coche import Coche
from Moto import Moto

def imprimirMenu():
    print("""
    MENÚ:
    0. SALIR DEL PROGRAMA
    1. Agregar un nuevo vehiculo
    2. Mostrar todos los vehículos registrados
    3. Actualizar un vehículo
    4. Eliminar un vehículo existente
    5. Recuento de vehículos""")

def leerInt(mensaje):
    try:
        return int(input(mensaje))
    except:
        return -1

def datosVehiculo(tipo):
    if len(listaVehiculos) == 0:
        id = 1
    else:
        id = listaVehiculos[-1].id + 1

    marca = input("Introduzca la marca del vehículo que desea registrar: ")
    modelo = input("Introduzca el modelo del vehículo que desea registrar: ")
    ano = leerInt("Introduzca el año de la fecha de fabricación del vehículo: ")

    while ano == -1:  # En caso de que el user introduzca una letra
        print("El año no puede contener letras")
        ano = leerInt("Introduzca un año válido para la fecha de fabricación: ")

    if tipo == 0:
        try:
            numPuertas = int(input("Introdzca el número de puertas del coche: "))
            vehiculo = Coche(id, marca, modelo, ano, numPuertas)
        except:
            print("Las puertas tienen que ser un número válido")

    else:
        tipoMotor = input("Introduzca el tipo de motor que tiene la moto: ")
        vehiculo = Moto(id, marca, modelo, ano, tipoMotor)

    return vehiculo

def datosVehiculoConID(id, tipo):
    marca = input("Introduzca la marca del vehículo que desea registrar: ")
    modelo = input("Introduzca el modelo del vehículo que desea registrar: ")
    ano = leerInt("Introduzca el año de la fecha de fabricación del vehículo: ")

    while ano == -1:  # En caso de que el user introduzca una letra
        print("El año no puede contener letras")
        ano = leerInt("Introduzca un año válido para la fecha de fabricación: ")

    if tipo == 0:
        try:
            numPuertas = int(input("Introdzca el número de puertas del coche: "))
            vehiculo = Coche(id, marca, modelo, ano, numPuertas)
        except:
            print("Las puertas tienen que ser un número válido")

    else:
        tipoMotor = input("Introduzca el tipo de motor que tiene la moto: ")
        vehiculo = Moto(id, marca, modelo, ano, tipoMotor)

    return vehiculo

def actualizarVehiculo(vehiculo):
    coche = vehiculoCoche(vehiculo)
    if coche:
        print("El vehículo se guardará como coche")
        # Pasar el ID original al crear el nuevo objeto Coche
        v = datosVehiculoConID(vehiculo.id, 0)
        return v
    else:
        print("El vehículo se guardará como moto")
        # Pasar el ID original al crear el nuevo objeto Moto
        v = datosVehiculoConID(vehiculo.id, 1)
        return v

def vehiculoCoche(vehiculo):
    if isinstance(vehiculo, Coche): #Si el vehiculo es un coche
        modificacion = input("El vehiculo es de tipo Coche, quieres modificar este campo?\n"
                             "Introduzca si(Y) o no (N): ").strip().lower()

        if modificacion == "y":
            return False
        else:
            return True
    else:
        modificacion = input("El vehiculo es de tipo Moto, quieres modificar este campo?\n"
                             "Introduzca si(Y) o no (N): ").strip().lower()

        if modificacion == "y":
            return True
        else:
            return False

def mostrarVehiculos():
    for vehiculo in listaVehiculos:
        vehiculo.mostrarDatos()

def recuentoVehiculos():
    coches = 0
    motos = 0

    for vehiculo in listaVehiculos:
        if(isinstance(vehiculo, Coche)):
            coches += 1
        else:
            motos += 1

    print(f"Coches: {coches}\nMotos: {motos}\nTotal: {coches + motos}")

#MAIN-------------------------------------------------------------------------------------------------------------------

listaVehiculos = []

while True:
    imprimirMenu()
    op = leerInt("Selecciona tu opcion: ")
    match op:
        case 0:
            print("SALIENDO DEL PROGRAMA...")
            exit(0)
        case 1:
            print("OPCIÓN SELECCIONADA -> Guardar un nuevo vehículo")
            try:
                tipoVehiculo = int(
                    input("Introduzca el tipo de vehículo que desea registrar (0 para coche, 1 para moto): "))
                if tipoVehiculo == 0 or tipoVehiculo == 1:
                    vehiculo = datosVehiculo(tipoVehiculo)
                    listaVehiculos.append(vehiculo)
                    print("Vehículo guardado!")
            except:
                print("Opción no válida")

        case 2:
            print("OPCIÓN SELECCIONADA -> Mostrar todos los vehículos")
            if len(listaVehiculos) == 0:
                print("La lista de los vehículos está vacia")
            else:
                mostrarVehiculos()

        case 3:
            print("OPCIÓN SELECCIONADA -> Actualizar vehículo")
            if len(listaVehiculos) == 0:
                print("No hay vehículos registrados para actualizar.")
            else:
                # Mostrar los vehículos disponibles
                for vehiculo in listaVehiculos:
                    print(f"{vehiculo.id} -> {vehiculo.marca}, {vehiculo.modelo}")

                # Solicitar el ID del vehículo a actualizar
                vehiculoActualizar = leerInt("Introduzca el ID del vehículo que desea actualizar: ")
                vEncontrado = None
                indiceEncontrado = None  #Posicion del vehiculo en la lista

                # Buscar el vehículo por ID y obtener su índice
                for indice, vehiculo in enumerate(listaVehiculos):   #Enumerate devuelve el indice de cada objeto de la lista
                    if vehiculo.id == vehiculoActualizar:
                        vEncontrado = vehiculo
                        indiceEncontrado = indice
                        break

                # Si se encuentra el vehículo, actualizarlo
                if vEncontrado is not None:
                    print("Vehículo encontrado")
                    v = actualizarVehiculo(vEncontrado)
                    listaVehiculos[indiceEncontrado] = v  # Actualizar el vehículo en la lista
                    print("Vehículo actualizado con éxito.")
                else:
                    print("No se encontró ningún vehículo con ese ID.")

        case 4:
            if len(listaVehiculos) == 0:
                print("No existe vehículo registrado por el momento")
            else:
                mostrarVehiculos()
                vEliminar = leerInt("Introduzca el id del vehiculo que quiere eliminar: ")
                if vEliminar == -1 or vEliminar > len(listaVehiculos):
                    print("Opción no válida")
                else:
                    for vehiculo in listaVehiculos:
                        if vEliminar == vehiculo.id:
                            vEncontrado = vehiculo
                            break
                    listaVehiculos.remove(vEncontrado)
                    print("Vehiculo eliminado")

        case 5:
            print("OPCIÓN SELECCIONADA -> Recuento de vehículos")
            recuentoVehiculos()

        case _:
            print("La opción no existe en el menú")
