class Libros:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def mostrarInfo(self):
        print(f"Tituo obra: {self.titulo}, Autor: {self.autor}, año: {self.ano}")

