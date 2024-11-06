class Usuario:

    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = 30000
        self.saldo_pagar = 0

    def hacer_compra(self, monto):  # recibe como argumento el monto de la compra
        self.saldo_pagar += monto

    def mostrar_saldo_usuario(self):  # método para mostrar el saldo del usuario
        print(f"Cliente: {self.nombre} {self.apellido}, Saldo a Pagar: ${self.saldo_pagar}")

# Crear un objeto Usuario y realizar operaciones
cliente = Usuario("Nariyoshi", "Miyagi", "nariyoshi@gmail.com")
cliente.hacer_compra(50)  # Hacer una compra de 50
cliente.mostrar_saldo_usuario()  # Mostrar el saldo del usuario

#transferir_deuda(self, otro_usuario, monto): crea un método que reduzca la deuda (saldo_pagar) del usuario por el monto, 
# y agrega esa cantidad al saldo_pagar de otro_usuario

def transferir_deuda(self, otro_usuario, monto):
        if monto <= self.saldo_pagar:
            self.saldo_pagar -= monto
            otro_usuario.saldo_pagar += monto
            print(f"Se ha transferido una deuda de ${monto} a {otro_usuario.nombre} {otro_usuario.apellido}.")
        else:
            print("El monto excede el saldo a pagar. No se puede transferir la deuda.")

usuario1= Usuario("Nariyoshi", "Miyagi", "nariyoshi@gmail.com")
usuario2= Usuario("Larusso", "Daniel", "daniel@gmail.com")

usuario1.hacer_compra(100)  # Usuario1 hace una compra de $100
usuario1.mostrar_saldo_usuario()  # Muestra el saldo de Usuario1
usuario2.mostrar_saldo_usuario()  # Muestra el saldo de Usuario2


usuario1.transferir_deuda(usuario2, 50)  # Transfiere $50 de deuda de Usuario1 a Usuario2

usuario1.mostrar_saldo_usuario()  # Muestra el saldo actualizado de Usuario1
usuario2.mostrar_saldo_usuario()  # Muestra el saldo actualizado de Usuario2
