

from dataclasses import InitVar, dataclass
import re
from typing import ClassVar

from flask import app, flash
from flask_app.models.default_model import default_model
from flask_bcrypt import Bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

bcrypt = Bcrypt(app)

@dataclass(init=False)
class Usuarios(default_model):

    # Nombre de la tabla
    table_name: ClassVar[str] = "usuarios"

    # Atributos de la clase
    email: str
    contraseña: str
    nombre: str
    apellido: str

    # Campos virtuales para las relaciones
    equipo: InitVar[object]
    equipos_favoritos: InitVar[list[object]]


    @staticmethod
    def validate(data):
    # Variable para determinar si los datos son válidos
      is_valid = True
    # Validar email
      if not data.get('email'):  # Verifica si el campo está vacío
        flash('Ingrese un email válido', 'email')
        is_valid = False
      elif not EMAIL_REGEX.match(data.get('email')):  # Si no coincide con el patrón
        flash('Ingrese un email con formato válido', 'email')
        is_valid = False

    # Validar contraseña
      if not data.get('contraseña') or len(data.get('contraseña')) < 8:
        flash('La contraseña debe ser mayor a 8 caracteres', 'contraseña')
        is_valid = False

    # Validar nombre
      if not data.get('nombre') or len(data.get('nombre')) < 2:
        flash('El nombre debe ser mayor a 2 caracteres', 'nombre')
        is_valid = False

    # Validar apellido
      if not data.get('apellido') or len(data.get('apellido')) < 2:
        flash('El apellido debe ser mayor a 2 caracteres', 'apellido')
        is_valid = False

      return is_valid

#encriptar contraseña
@staticmethod
def encrypt_password(password):
    return bcrypt.generate_password_hash(password).decode('utf-8')