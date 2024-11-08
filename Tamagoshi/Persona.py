from Tamagoshi import Tamagoshi
class Persona:
    def __init__(self, nombre, apellido, tamagoshi):
        self.nombre = nombre
        self.apellido = apellido
        self.tamagoshi = tamagoshi

    def menu(self):
        while True:
            print(f"\n****** Bienvenido a Tamagoshi, {self.nombre} {self.apellido}! *******")
            print("Elije una opción:")
            print("1. Jugar")
            print("2. Comer")
            print("3. Curar")
            print("4. Salir")

            opcion = input("Elige una opción (1-4): ")
            if opcion == "1":
                self.tamagoshi.jugar()
            elif opcion == "2":
                self.tamagoshi.comer()
            elif opcion == "3":
                self.tamagoshi.curar()
            elif opcion == "4":
                print("¡Adiós! Gracias por cuidar a tu Tamagotchi!",self.nombre)
                break
            else:
                print("Opción inválida. Por favor, elige una opción válida.")

# Crear un objeto Tamagoshi
tamagoshi = Tamagoshi("Pollo", "Rojo", 100)

# Crear un objeto Persona, asociándolo con el Tamagoshi
persona = Persona("Juan", "Perez", tamagoshi)
persona = Persona("Mirsson", "Rosas", tamagoshi)
# Ejecutar el menú
persona.menu()

