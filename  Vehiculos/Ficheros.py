import csv
from Coche import Coche
from Moto import Moto

def leerFicheroCSV(nombreFichero):
    vehiculos = []  # Lista para almacenar los vehículos

    with open(nombreFichero, 'r') as ficheroCSV:
        lector = csv.reader(ficheroCSV, delimiter=';')
        i = 0
        for linea in lector:
            id, marca, modelo, ano = int(i), linea[1], linea[2], linea[3]

            if linea[4].isdigit():  # Si el campo 4 de la línea es un dígito, es un coche
                numPuertas = int(linea[4])
                vehiculo = Coche(id, marca, modelo, ano, numPuertas)
            else:  # Si no, es una moto
                tipoMotor = linea[4]
                vehiculo = Moto(id, marca, modelo, ano, tipoMotor)

            vehiculos.append(vehiculo)  # Añadir el vehículo a la lista
            i = i +1
    return vehiculos

def guardarVehiculos(nombreFichero, listaVehiculos):
    with open(nombreFichero, 'w', newline='') as ficheroCSV:
        escritor = csv.writer(ficheroCSV, delimiter=';')
        for vehiculo in listaVehiculos:
            if isinstance(vehiculo, Coche):
                escritor.writerow([vehiculo.id, vehiculo.marca, vehiculo.modelo, vehiculo.ano, vehiculo.numPuertas])
            else:
                escritor.writerow([vehiculo.id, vehiculo.marca, vehiculo.modelo, vehiculo.ano, vehiculo.tipoMotor])
