from Biblioteca.Libros import Libros

class Fisicos(Libros):
    def __init__(self, titulo, autor, ano, ubicacion):
        super().__init__(titulo, autor, ano)  # Llamada al constructor de la clase base
        self.ubicacion = ubicacion

    def mostrarInfo(self):
        super().mostrarInfo()
        print(f"Ubicación: {self.ubicacion}")