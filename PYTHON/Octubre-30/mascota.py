from dataclasses import dataclass
from Humano import Humano
@dataclass
class Mascota:

    #atributos de  instancia 
    especie: str
    raza: str
    nombre: str
    color: list[str]
    sonido: str 
    medio: str
    esterilizado: bool
    vacunado: bool 

    #relacion con la persona
    dueños:list[Humano]

    #Probar la clase si el archivo es principal
    if __name__ == "__main__":

        from mascota import Mascota
        firulais = Mascota("Perro","Firulais",["Cafe"],"wow","Tierra",False,False)

        gandolfo = Mascota("Chinchilla","Pradera","Gandolfo",["gris","Blanca"],"TITI","Tierra",True,True)