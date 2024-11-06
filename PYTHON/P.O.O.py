"POO: Programación Orientada a Objetos"

#clases: Es una forma de crear objetos que tienen propiedades y métodos
#Objetos: Son entidades que tienen propiedades y métodos 

class Automovil:
#Constructor
 def __init__(self, ruedas: int, carroceria: str, marca:str, puertas: int, motor:float, año: int):
  #Atributos
    self.ruedas = ruedas
    self.carroceria = carroceria
    self.marca = marca
    self.puertas = puertas
    self.motor = motor
    self.año = año

volkswagen_amarok = Automovil(4, "Carroceria", "Volkswagen", 4, 1.5, 2021)
audi_q7 = Automovil(4, "Carroceria", "Audi", 4, 1.5, 2021)
tuktuk = Automovil(4, "Carroceria", "tuktuk", 4, 1.6, 2020)

print(volkswagen_amarok.ruedas)
print(audi_q7.motor)
audi_q7.acelerar(100)

#Metodos de instancia 
def acelerar(self,cantidad: int =1) -> int:
  self.velocidad += cantidad 


# Diccionarios
estudiante = {"nombre": "Gonzalo", "curso": "Python"} #Notación Literal

paises = {} #Diccionario vacío

paises["MEX"] = "México" #Agregando valores

paises["COL"] = "Colombia"

paises["CHL"] = "Chile"