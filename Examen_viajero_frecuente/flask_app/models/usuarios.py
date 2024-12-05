from dataclasses import dataclass
import re
from typing import ClassVar
from flask import flash
from flask_app.models.default_model import default_model
from flask_app import bcrypt
from flask_app.config.mysqlconnection import connectToMySQL

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


@dataclass(init=False)
class Usuario(default_model):

    # Nombre de la tabla
    table_name: ClassVar[str] = "usuarios"

    # Atributos de la clase
    nombre: str
    apellido: str
    email: str
    contraseña: str

    @staticmethod
    def validate(user):
        is_valid = True
        
        try:
            # Verificar si el email ya existe
            query = "SELECT * FROM usuarios WHERE email = %(email)s;"
            result = connectToMySQL('viajes').query_db(query, {'email': user['email']})
            
            print("Resultado de la consulta:", result)  # Debug
            
            # Validar el resultado de la consulta
            if result is not None and result is not False:
                if isinstance(result, list) and len(result) > 0:
                    flash('Email ya está registrado', 'registro')
                    is_valid = False
            
            # Validaciones de campos
            if not user['email'] or not EMAIL_REGEX.match(user['email']):
                flash('Email inválido', 'registro')
                is_valid = False
            
            if not user['nombre'] or len(user['nombre']) < 2:
                flash('Nombre debe tener al menos 2 caracteres', 'registro')
                is_valid = False
            
            if not user['apellido'] or len(user['apellido']) < 2:
                flash('Apellido debe tener al menos 2 caracteres', 'registro')
                is_valid = False
            
            if not user['password'] or len(user['password']) < 6:
                flash('Password debe tener al menos 6 caracteres', 'registro')
                is_valid = False
            
            if user['password'] != user['confirm_password']:
                flash('Passwords no coinciden', 'registro')
                is_valid = False
                
        except Exception as e:
            print("Error en validación:", e)
            is_valid = False
            flash('Error en la validación', 'registro')
        
        return is_valid

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

    @classmethod
    def get_by_email(cls, email):
        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        data = {'email': email}
        results = connectToMySQL('viajes').query_db(query, data)
        
        if len(results) < 1:
            return None
            
        return cls(results[0])

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        results = connectToMySQL('viajes').query_db(query, data)
        
        # Verificar si results es None o está vacío
        if not results:
            return None
        
        # Si hay resultados, crear y retornar una instancia de Usuario
        return cls(results[0])

    @classmethod
    def save(cls, data):
        try:
            # Imprimir para debug
            print("Datos a guardar:", data)
            
            query = """
                INSERT INTO usuarios 
                (nombre, apellido, email, contraseña, created_at, updated_at) 
                VALUES 
                (%(nombre)s, %(apellido)s, %(email)s, %(contraseña)s, NOW(), NOW());
            """
            
            # Imprimir para debug
            print("Query a ejecutar:", query)
            
            return connectToMySQL('viajes').query_db(query, data)
            
        except Exception as e:
            print("Error en save:", e)
            return False
