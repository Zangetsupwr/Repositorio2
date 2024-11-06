
from dataclasses import dataclass


@dataclass
class Producto:

    nombre:str
    precio:float
    dimensiones:tuple
    peso:float
    sku:str
    stock:int


    def comprar(self, cantidad:int):
        # Verificar si hay suficiente stock
        if self.stock >= cantidad:
            self.stock -= cantidad
            print(f"Compra de {cantidad} {self.nombre} exitosa")
            return True
        # Si no hay suficiente stock
        else:
            print(f"No hay suficiente stock de {self.nombre}")
            return False
        
    def reabastecer(self, cantidad:int):
        self.stock += cantidad
        return self.stock
    

# Se ejecuta el programa solo si es el archivo principal
if __name__ == "__main__":

    # Creamos un producto nuevo
    cargadores = Producto("Cargador 12v",5.75,(5,5,2),100,"CARG-12V",100)
    
    print(cargadores)
    cargadores.comprar(15)
    print(cargadores)
    cargadores.comprar(90)
    print(cargadores)
    cargadores.reabastecer(10)
    print(cargadores)
    cargadores.comprar(90)
    print(cargadores)


