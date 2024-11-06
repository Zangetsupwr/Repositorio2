class TarjetaCredito:
    tarjetas = []

    def __init__(self, saldo_pagar=0, limite_credito=3000, intereses=0.02):
        self.saldo_pagar = saldo_pagar             
        self.limite_credito = limite_credito      
        self.intereses = intereses    
        TarjetaCredito.tarjetas.append(self)

    def compra(self, monto):
        if self.saldo_pagar + monto <= self.limite_credito:
            self.saldo_pagar += monto
            print(f"Compra de {monto} realizada. Saldo a pagar: {self.saldo_pagar}")
        else:
            print("Tarjeta Rechazada, has alcanzado tu límite de crédito")

    def pago(self, monto):
        self.saldo_pagar -= monto
        if self.saldo_pagar < 0:
            self.saldo_pagar = 0
        print(f"Pago de {monto} realizado. Saldo a pagar: {self.saldo_pagar}")

    def mostrar_info_tarjeta(self):   # Aqui se solamente se muestra la informacion de la tarjeta con los datos requeridos
        print("\n")
        print("----- Informacionn de la tarjeta de credito------")
        print(f"Información de la tarjeta:\n"
              f"Límite de crédito: {self.limite_credito}\n"
              f"Saldo a pagar: {self.saldo_pagar}\n"
              f"Tasa de interés: {self.intereses * 100}%")
        print("-------------------------------------------------")

    def cobrar_interes(self):
        intereses_cobrados = self.saldo_pagar * self.intereses # Se Calcula el monto de los intereses sobre el saldo actual
        self.saldo_pagar += intereses_cobrados # Se suma el monto de los intereses al saldo actual
        print(f"Intereses cobrados: {intereses_cobrados}. Saldo a pagar: {self.saldo_pagar}") # Se imprime el los intereses cobrados

    @classmethod
    def mostrar_todas_las_tarjetas(cls):
        # Método de clase para mostrar la información de todas las tarjetas creadas
        print("Información de todas las tarjetas:")
        for index, tarjetas in enumerate(cls.tarjetas):
            print(f"\nTarjeta {index + 1}:")
            tarjetas.mostrar_info_tarjeta()


# Para la primera tarjeta, haz 2 compras y un pago. 
# Luego cobra los intereses y muestra la información de la tarjeta; 
# todo esto en una sola línea a través de la encadenación.
tarjeta = TarjetaCredito()
tarjeta.compra(300)
tarjeta.pago(200)
tarjeta.cobrar_interes()
tarjeta.mostrar_info_tarjeta()


# Para la segunda tarjeta, haz 3 compras y 2 pagos. 
# Luego cobra los intereses y muestra la información de la tarjeta; 
# todo esto en una sola línea a través de la encadenación
tarjeta2 = TarjetaCredito()
tarjeta2.compra(250)
tarjeta2.compra(250)
tarjeta2.compra(500)
tarjeta2.pago(100)
tarjeta2.pago(200)
tarjeta2.mostrar_info_tarjeta

# Para la tercera tarjeta, haz 5 compras y excede su límite de crédito. 
# Luego muestra la información de la tarjeta; 
# todo esto en una sola línea a través de la encadenación.
tarjeta3 = TarjetaCredito(limite_credito=1000)
tarjeta3.compra(500)
tarjeta3.compra(500)
tarjeta3.compra(400)
tarjeta3.compra(300)
tarjeta3.compra(200)
tarjeta3.mostrar_info_tarjeta()

tarjeta.mostrar_todas_las_tarjetas()


