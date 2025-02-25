from Biblioteca.Libros import Libros

class Electronicos(Libros):
    def __init__(self, titulo, autor, ano, formato):
        super().__init__(titulo, autor, ano)
        self.formato = formato

    def mostrarInfo(self):
        super().mostrarInfo()
        print(f"Formato del libro: {self.formato}")