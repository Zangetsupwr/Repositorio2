
from Producto import Producto
from dataclasses import dataclass
from datetime import date


@dataclass
class Alimentos(Producto):

    perecible:bool
    fecha_caducidad:date

    #Sobreescribimos el metodo comprar para ver si el producto esta vencido
    def comprar(self,cantidad:int):
        # Si es peresible y la fehca de caducidad ya pasó no se puede comprar
        if self.perecible and self.fecha_caducidad < date.today():
            print(f"El producto {self.nombre} esta vencido")
            return False
        else:
            return super().comprar(cantidad)


# Se ejecuta el programa solo si es el archivo principal
if __name__ == "__main__":
    # Creamos un producto nuevo
    leche = Alimentos("Leche",2.75,(15,5,5),450,"LEC-001",100,True,date(2024,11,5))
    print(leche)
    leche.comprar(15)
    print(leche)
    leche.comprar(90)
    print(leche)
    leche.reabastecer(10)
    print(leche)
    leche.comprar(90)
    print(leche)

    # Creamos un producto rancio
    yogurt = Alimentos("Yogurt",1.75,(15,5,5),450,"YOG-001",100,True,date(2024,11,2))
    print(yogurt)
    yogurt.comprar(15)
    print(yogurt)
