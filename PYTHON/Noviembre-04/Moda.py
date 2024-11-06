

from Producto import Producto
from dataclasses import dataclass


@dataclass
class Moda(Producto):

    talla:str
    color:str
    material:str



# Se ejecuta el programa solo si es el archivo principal
if __name__ == "__main__":
    # Creamos un producto nuevo
    camisa = Moda("Cubavera",15.75,(5,5,2),100,"CUV-001",100,"M","Azul","Lino")
    print(camisa)
