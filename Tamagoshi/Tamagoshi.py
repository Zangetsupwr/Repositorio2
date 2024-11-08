
class Tamagoshi:

    def __init__(self, nombre, color, salud):
        self.nombre = nombre
        self.color = color
        self.salud = salud
        self.felicidad = 50  # Valor inicial de felicidad

    def jugar(self):
        self.felicidad += 10  # Incrementa la felicidad en 10
        self.salud -= 5       # Disminuye la salud en 5
        print("Jugar: Felicidad +10, Salud -5")
        print(f"{self.nombre} ({self.color}) - Felicidad: {self.felicidad}, Salud: {self.salud}")

    def comer(self):
        self.felicidad += 5   # Incrementa la felicidad en 5
        self.salud += 10      # Aumenta la salud en 10
        print("Comer: Felicidad +5, Salud +10")
        print(f"{self.nombre} ({self.color}) - Felicidad: {self.felicidad}, Salud: {self.salud}")

    def curar(self):
        self.salud += 20      # Incrementa la salud en 20
        self.felicidad -= 5   # Disminuye la felicidad en 5
        print("Curar: Salud +20, Felicidad -5")
        print(f"{self.nombre} ({self.color}) - Felicidad: {self.felicidad}, Salud: {self.salud}")
