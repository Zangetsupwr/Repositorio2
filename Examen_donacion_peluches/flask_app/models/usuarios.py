from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Usuario:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.contraseña = data['contraseña']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

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
            
            return connectToMySQL('donacion_peluches').query_db(query, data)
            
        except Exception as e:
            print("Error en save:", e)
            return False

    @classmethod
    def get_by_email(cls, email):
        try:
            query = "SELECT * FROM usuarios WHERE email = %(email)s;"
            data = {'email': email}
            
            # Debug: imprimir query y datos
            print("Query get_by_email:", query)
            print("Datos para get_by_email:", data)
            
            results = connectToMySQL('donacion_peluches').query_db(query, data)
            
            # Debug: imprimir resultados
            print("Resultados get_by_email:", results)
            
            if not results:
                return None
            
            return cls(results[0])
            
        except Exception as e:
            print("Error en get_by_email:", str(e))
            return None

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        result = connectToMySQL('donacion_peluches').query_db(query, data)
        return cls(result[0]) if result else None

    @staticmethod
    def validate(data):
        is_valid = True

        if len(data['nombre']) < 2:
            flash('El nombre debe tener al menos 2 caracteres', 'registro')
            is_valid = False

        if len(data['apellido']) < 2:
            flash('El apellido debe tener al menos 2 caracteres', 'registro')
            is_valid = False

        if not EMAIL_REGEX.match(data['email']):
            flash('Email inválido', 'registro')
            is_valid = False

        if len(data['password']) < 6:
            flash('La contraseña debe tener al menos 6 caracteres', 'registro')
            is_valid = False

        if data['password'] != data['confirm_password']:
            flash('Las contraseñas no coinciden', 'registro')
            is_valid = False

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
        results = connectToMySQL('donacion_peluches').query_db(query, data)
        
        if len(results) < 1:
            return None
            
        return cls(results[0])

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        results = connectToMySQL('donacion_peluches').query_db(query, data)
        
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
            
            return connectToMySQL('donacion_peluches').query_db(query, data)
            
        except Exception as e:
            print("Error en save:", e)
            return False

