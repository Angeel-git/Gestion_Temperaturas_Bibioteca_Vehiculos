from  Vehiculo import Vehiculo

class Coche(Vehiculo):
    def __init__(self,id, marca, modelo, ano, numPuertas):
        super().__init__(id, marca, modelo, ano)
        self.numPuertas = numPuertas

    def mostrarDatos(self):
        super().mostrarDatos()
        print(f"Numero de puertas -> {self.numPuertas}")