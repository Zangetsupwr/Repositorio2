
from Producto import Producto
from dataclasses import dataclass


@dataclass
class Electronicos(Producto):

    voltaje_operacion:float




# Se ejecuta el programa solo si es el archivo principal
if __name__ == "__main__":
    # Creamos un producto nuevo
    cargadores = Electronicos("Cargador 12v",5.75,(5,5,2),100,"CARG-12V",100,12.0)

    print(cargadores)
    cargadores.comprar(15)
    print(cargadores)
    cargadores.comprar(90)
    print(cargadores)
    cargadores.reabastecer(10)
    print(cargadores)
    cargadores.comprar(90)
    print(cargadores)