from datetime import date
from dataclasses import dataclass
from mascota import Mascota
@dataclass
class Humano:

    dni: str
    nombres: str
    apellidos: str
    fecha_nacimiento: date
    nacionalidad: str
    genero: bool  # True: Masculino, False: Femenino
    estado_civil: bool  # True: Casado, False: Soltero
    estatura: int
    peso: int
    tipo_sangre: str
    profesion: str
    alergias: list[str]
    grupo_familiar: int
    donante: bool
    etnia: str
    discapacidad: bool  # True: Si, False: No
    apto_mascota: bool  # True: Si, False: No
    # RELACION CON MASCOTA
    mascotas: list[Mascota]