import os
from dotenv import load_dotenv
from flask_app.config.mysqlconnection import connectToMySQL

# Cargar variables del archivo .env
load_dotenv()

class Viaje:
    def __init__(self, data):
        self.id = data['id']
        self.destino = data['destino']
        self.fecha_inicio = data['fecha_inicio']
        self.fecha_fin = data['fecha_fin']
        self.itinerario = data['itinerario']
        self.usuario_id = data['usuario_id']
    
    # Método para obtener un viaje por ID
    @classmethod
    def get_by_id(cls, viaje_id):
        query = "SELECT * FROM viajes WHERE id = %s;"
        results = connectToMySQL(os.getenv('DB_NAME')).query_db(query, (viaje_id,))
        if len(results) > 0:
            return cls(results[0])
        return None

    # Método para obtener todos los viajes
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM viajes;"
        results = connectToMySQL(os.getenv('DB_NAME')).query_db(query)
        viajes = []
        for row in results:
            viajes.append(cls(row))
        return viajes

    # Método para guardar un nuevo viaje
    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO viajes (destino, fecha_inicio, fecha_fin, itinerario, usuario_id)
        VALUES (%(destino)s, %(fecha_inicio)s, %(fecha_fin)s, %(itinerario)s, %(usuario_id)s);
        """
        return connectToMySQL(os.getenv('DB_NAME')).query_db(query, data)

    # Método para actualizar un viaje
    @classmethod
    def update(cls, data):
        query = """
        UPDATE viajes 
        SET destino = %(destino)s, fecha_inicio = %(fecha_inicio)s, fecha_fin = %(fecha_fin)s, itinerario = %(itinerario)s
        WHERE id = %(id)s;
        """
        return connectToMySQL(os.getenv('DB_NAME')).query_db(query, data)

    # Método para eliminar un viaje
    @classmethod
    def delete(cls, viaje_id):
        query = "DELETE FROM viajes WHERE id = %s;"
        return connectToMySQL(os.getenv('DB_NAME')).query_db(query, (viaje_id,))
