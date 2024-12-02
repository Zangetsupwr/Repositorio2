from config.mysqlconnection import connectToMySQL

class Estudiante:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.edad = data['edad']
        self.curso_id = data['curso_id']
    
    @classmethod
    def guardar(cls, data):
        query = "INSERT INTO estudiantes (nombre, apellido, edad, curso_id) VALUES (%(nombre)s, %(apellido)s, %(edad)s, %(curso_id)s);"
        return connectToMySQL('esquema_estudiantes_cursos').query_db(query, data)
