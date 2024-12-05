from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from datetime import datetime

class Viajes:
    def __init__(self, data):
        self.id = data['id']
        self.destino = data['destino']
        self.fecha_inicio = data['fecha_inicio']
        self.fecha_fin = data['fecha_fin']
        self.itinerario = data['itinerario']
        self.usuario_id = data['usuario_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO viajes 
            (destino, fecha_inicio, fecha_fin, itinerario, usuario_id) 
            VALUES 
            (%(destino)s, %(fecha_inicio)s, %(fecha_fin)s, %(itinerario)s, %(usuario_id)s);
        """
        return connectToMySQL('viajes').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = """
            SELECT viajes.*, usuarios.nombre as creador_nombre 
            FROM viajes 
            JOIN usuarios ON viajes.usuario_id = usuarios.id 
            ORDER BY viajes.created_at DESC;
        """
        return connectToMySQL('viajes').query_db(query)

    @classmethod
    def get_by_id(cls, data):
        query = """
            SELECT viajes.*, usuarios.nombre as creador_nombre 
            FROM viajes 
            JOIN usuarios ON viajes.usuario_id = usuarios.id 
            WHERE viajes.id = %(id)s;
        """
        results = connectToMySQL('viajes').query_db(query, data)
        if results:
            return results[0]
        return None

    @classmethod
    def update(cls, data):
        query = """
            UPDATE viajes 
            SET destino = %(destino)s,
                fecha_inicio = %(fecha_inicio)s,
                fecha_fin = %(fecha_fin)s,
                itinerario = %(itinerario)s
            WHERE id = %(id)s AND usuario_id = %(usuario_id)s;
        """
        return connectToMySQL('viajes').query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM viajes WHERE id = %(id)s AND usuario_id = %(usuario_id)s;"
        return connectToMySQL('viajes').query_db(query, data)

    @staticmethod
    def validate_viaje(viaje):
        is_valid = True
        
        if len(viaje['destino']) < 3:
            flash("El destino debe tener al menos 3 caracteres")
            is_valid = False
            
        if not viaje['fecha_inicio']:
            flash("La fecha de inicio es requerida")
            is_valid = False
            
        if not viaje['fecha_fin']:
            flash("La fecha de fin es requerida")
            is_valid = False
            
        if viaje['fecha_inicio'] > viaje['fecha_fin']:
            flash("La fecha de inicio debe ser anterior a la fecha de fin")
            is_valid = False
            
        if len(viaje['itinerario']) < 10:
            flash("El plan debe tener al menos 10 caracteres")
            is_valid = False
            
        return is_valid

    @classmethod
    def get_viajeros(cls, viaje_id):
        query = """
            SELECT usuarios.* 
            FROM usuarios 
            JOIN participantes ON usuarios.id = participantes.usuario_id 
            WHERE participantes.viaje_id = %(viaje_id)s;
        """
        return connectToMySQL('viajes').query_db(query, {'viaje_id': viaje_id})

    @classmethod
    def unirse_viaje(cls, data):
        query = """
            INSERT INTO participantes (usuario_id, viaje_id) 
            VALUES (%(usuario_id)s, %(viaje_id)s);
        """
        return connectToMySQL('viajes').query_db(query, data)

    @classmethod
    def cancelar_viaje(cls, data):
        query = """
            DELETE FROM participantes 
            WHERE usuario_id = %(usuario_id)s AND viaje_id = %(viaje_id)s;
        """
        return connectToMySQL('viajes').query_db(query, data)

    @classmethod
    def is_viajero(cls, data):
        query = """
            SELECT COUNT(*) as count FROM participantes 
            WHERE usuario_id = %(usuario_id)s AND viaje_id = %(viaje_id)s;
        """
        result = connectToMySQL('viajes').query_db(query, data)
        return result[0]['count'] > 0 if result else False