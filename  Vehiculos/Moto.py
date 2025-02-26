from  Vehiculo import Vehiculo

class Moto(Vehiculo):
    def __init__(self, id, marca, modelo, ano, tipoMotor):
        super().__init__(id, marca, modelo, ano)
        self.tipoMotor = tipoMotor

    def mostrarDatos(self):
        super().mostrarDatos()
        print(f"Tipo de motor -> {self.tipoMotor}")