class TarjetaCredito:
    
    def __init__(self, saldo_pagar=0, limite_credito=3000, intereses=0.02):
        self.saldo_pagar = saldo_pagar             
        self.limite_credito = limite_credito      
        self.intereses = intereses    

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
        print(f"Intereses cobrados: {intereses_cobrados}. Saldo a pagar: {self.saldo_pagar}")