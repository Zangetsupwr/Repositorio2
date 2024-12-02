from dataclasses import dataclass
import re
from typing import ClassVar
from flask import flash
from flask_app.models.default_model import default_model
from flask_app import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@dataclass(init=False)
class Usuario(default_model):

  table_name: ClassVar[str] ='usuarios'

  nombre: str
  apellido: str
  email: str
  contraseña: str


@staticmethod
def validate(data):
        # Variable que indica si los datos son válidos
        is_valid = True
        if (data.get('nombre') == None or len(data.get('nombre')) < 2):
            is_valid = False
            flash("El nombre debe tener al menos 2 caracteres", "nombre")
        if (data.get('apellido') == None or len(data.get('apellido')) < 2):
            is_valid = False
            flash("El apellido debe tener al menos 2 caracteres", "apellido")
        if (data.get('email') == None or not EMAIL_REGEX.match(data.get('email'))):
            is_valid = False
            flash("El email no es válido", "email")
        else:
            # Si el email es válido, verificar si ya existe en la base de datos
            query = f"SELECT * FROM {
                Usuario.table_name} WHERE email = %(email)s"
            result = Usuario.run_query(query, data)
            # Si hay algún resultado, entonces el email ya está registrado
            if len(result) > 0:
                is_valid = False
                flash("El email ya está registrado", "email")
        if (data.get('contraseña') == None or len(data.get('contraseña')) < 8):
            is_valid = False
            flash("La contraseña debe tener al menos 8 caracteres", "contraseña")
        elif (data.get('confirmar_contraseña') == None or data.get('contraseña') != data.get('confirmar_contraseña')):
            # Verificar si la contraseña y la confirmación de la contraseña son iguales
            is_valid = False
            flash("Las contraseñas no coinciden", "confirmar_contraseña")


@staticmethod
def validate_login(data):
        query = f"SELECT * FROM {Usuario.table_name} WHERE email = %(email)s"
        result = Usuario.run_query(query, data)
        # Si hay algún resultado, entonces el email ya está registrado
        if len(result) > 0:
            # Verificar si la contraseña es correcta contraseña hash vs contraseña ingresada
            if bcrypt.check_password_hash(result[0]['contraseña'], data['contraseña']):
                return result[0].get('id')
        flash("Email o contraseña incorrectos", "login")
        return False