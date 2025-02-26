class Vehiculo:
    def __init__(self, id, marca, modelo, ano):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def mostrarDatos(self):
        print(f"Id -> {self.id}, Marca -> {self.marca}, Modelo -> {self.modelo}, Año -> {self.ano}")

