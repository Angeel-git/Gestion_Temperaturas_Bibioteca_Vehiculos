class Ciudad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.temperaturas = {}

        # Llenamos el diccionario con listas vacías para cada mes (j = 0 a 11)
        for j in range(12):
            self.temperaturas[j] = []

    def agregarTemperaturas(self, temperaturasMes, j):
        self.temperaturas[j].extend(temperaturasMes)

    def mostrarTemperatura(self):
        print(f"{self.nombre}: {self.temperaturas}")

    def calcularMedia(self, j):
        if self.temperaturas[j]:
            return sum(self.temperaturas[j]) / len(self.temperaturas[j])
        else:
            return None  # Si no hay temperaturas, devuelve None

    def obtenerMaxMin(self, j):
        if self.temperaturas[j]:
            return max(self.temperaturas[j]), min(self.temperaturas[j])
        else:
            return None, None  # Si no hay temperaturas, devuelve (None, None)