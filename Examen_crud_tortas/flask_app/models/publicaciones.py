from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

class Publicacion:
    def __init__(self, data):
        self.id = data.get('id', 0)
        self.nombre = data['nombre']
        self.ingredientes = data['ingredientes']
        self.complementos = data['complementos']
        self.usuario_id = data['usuario_id']
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')
        self.likes = {'count': 0}

    @staticmethod
    def validate_2(data):
        is_valid = True
        
        # Validación del nombre
        if not data['nombre']:
            flash("El nombre es requerido", "error_nombre")
            is_valid = False
        elif len(data['nombre']) < 3:
            flash("El nombre debe tener al menos 3 caracteres", "error_nombre")
            is_valid = False
            
        # Validación de ingredientes
        if not data['ingredientes']:
            flash("Los ingredientes son requeridos", "error_ingredientes")
            is_valid = False
        elif len(data['ingredientes']) < 3:
            flash("Los ingredientes deben tener al menos 3 caracteres", "error_ingredientes")
            is_valid = False
            
        # Validación de complementos
        if not data['complementos']:
            flash("Los complementos son requeridos", "error_complementos")
            is_valid = False
        elif len(data['complementos']) < 3:
            flash("Los complementos deben tener al menos 3 caracteres", "error_complementos")
            is_valid = False
            
        return is_valid
   

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM publicaciones ORDER BY created_at DESC;"
        results = connectToMySQL('recetas').query_db(query)
        publicaciones = []
        if results:
            for row in results:
                publicaciones.append(cls(row))
        return publicaciones
    
    @classmethod
    def update(cls, data):
        query = """
            UPDATE publicaciones 
            SET nombre = %(nombre)s, 
                ingredientes = %(ingredientes)s, 
                complementos = %(complementos)s 
            WHERE id = %(id)s;
        """
        return connectToMySQL('recetas').query_db(query, data)

    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO publicaciones (nombre, ingredientes, complementos, usuario_id) 
            VALUES (%(nombre)s, %(ingredientes)s, %(complementos)s, %(usuario_id)s);
        """
        return connectToMySQL('recetas').query_db(query, data)

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM publicaciones WHERE id = %(id)s;"
        results = connectToMySQL('recetas').query_db(query, data)
        if results:
            return cls(results[0])
        return None

    @classmethod
    def delete_by_id(cls, data):
        query = "DELETE FROM publicaciones WHERE id = %(id)s;"
        return connectToMySQL('recetas').query_db(query, data)

    @classmethod
    def like(cls, data):
        # Primero verificamos si ya existe el like
        check_query = """
            SELECT * FROM likes 
            WHERE publicacion_id = %(publicacion_id)s 
            AND usuario_id = %(usuario_id)s;
        """
        existing_like = connectToMySQL('recetas').query_db(check_query, data)
        if not existing_like:
            # Si no existe, insertamos el nuevo like
            query = """
                INSERT INTO likes (publicacion_id, usuario_id) 
                VALUES (%(publicacion_id)s, %(usuario_id)s);
            """
            return connectToMySQL('recetas').query_db(query, data)
        return None

    @classmethod
    def get_likes_count(cls, publicacion_id):
        query = """
            SELECT COUNT(*) as count 
            FROM likes 
            WHERE publicacion_id = %(id)s;
        """
        result = connectToMySQL('recetas').query_db(query, {'id': publicacion_id})
        return result[0]['count'] if result else 0

    @classmethod
    def user_has_liked(cls, publicacion_id, usuario_id):
        query = """
            SELECT * FROM likes 
            WHERE publicacion_id = %(publicacion_id)s 
            AND usuario_id = %(usuario_id)s;
        """
        data = {
            'publicacion_id': publicacion_id,
            'usuario_id': usuario_id
        }
        result = connectToMySQL('recetas').query_db(query, data)
        return True if result else False