from Tarjeta_credito import TarjetaCredito 

class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = 30000
        self.saldo_pagar = 0
        self.tarjetas = {}  # Ahora tarjetas es un atributo de instancia

    def agregar_tarjeta(self, numero, saldo_inicial=0):
        if numero not in self.tarjetas:
            self.tarjetas[numero] = TarjetaCredito(numero, saldo_inicial)
            print(f"Tarjeta {numero} agregada al usuario {self.nombre}.")
        else:
            print(f"El usuario {self.nombre} ya tiene una tarjeta con el número {numero}.")
    
    def hacer_compra(self, numero_tarjeta, monto):  # Recibe como argumento el monto de la compra
        tarjeta = self.tarjetas.get(numero_tarjeta)
        if tarjeta:
            tarjeta.compra(monto)
        else:
            print(f"La tarjeta {numero_tarjeta} no existe para el usuario {self.nombre}.")

    def realizar_pago(self, numero_tarjeta, monto):
        tarjeta = self.tarjetas.get(numero_tarjeta)
        if tarjeta:
            tarjeta.realizar_pago(monto)
        else:
            print(f"La tarjeta {numero_tarjeta} no existe para el usuario {self.nombre}.")

    def mostrar_saldo_usuario(self):  # Método para mostrar el saldo del usuario
        print(f"\nSaldos de las tarjetas del usuario {self.nombre}:")
        for numero, tarjeta in self.tarjetas.items():
            print(f"\nTarjeta {numero}: ${tarjeta.saldo_pagar}")

usuario = Usuario("Juan", "Perez", "juanperez@gmail.com")
usuario = Usuario("Pancho", "Villa", "panchovilla@gmail.com")
usuario.agregar_tarjeta("1111-1111-1111-1111",1000)
usuario.agregar_tarjeta("2222-2222-2222-2222",2000)
usuario.hacer_compra("2222-2222-2222-2222",100)

