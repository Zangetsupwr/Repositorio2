
from datetime import date
from Producto import Producto
from Electronicos import Electronicos
from Moda import Moda
from Alimentos import Alimentos
from dataclasses import dataclass


@dataclass
class Tienda:

    nombre: str
    inventario: list[Producto]


# Se ejecuta el programa solo si es el archivo principal
if __name__ == "__main__":

    # Creamos una tienda
    pricesmart = Tienda("PriceSmart", [])
    print(pricesmart)

    # Creamos un producto nuevo
    cargadores = Electronicos("Cargador 12v", 5.75,
                              (5, 5, 2), 100, "CARG-12V", 100, 12.0)
    pricesmart.inventario.append(cargadores)
    print(pricesmart.inventario)
    # Creamos un producto nuevo
    yogurt = Alimentos("Yogurt", 1.75, (15, 5, 5), 450,
                       "YOG-001", 100, True, date(2024, 11, 2))
    pricesmart.inventario.append(yogurt)
    print(pricesmart.inventario)

    #Vender 5 cargadores
    pricesmart.inventario[0].comprar(5)
    print(pricesmart.inventario)

    #Vender 10 yogures
    pricesmart.inventario[1].comprar(10)
    print(pricesmart.inventario)