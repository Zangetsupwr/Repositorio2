from config.mysqlconnection import connectToMySQL

class Curso:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
    
    @classmethod
    def obtener_todos(cls):
        query = "SELECT * FROM cursos;"
        results = connectToMySQL('esquema_estudiantes_cursos').query_db(query)
        return [cls(row) for row in results]

    @classmethod
    def guardar(cls, data):
        query = "INSERT INTO cursos (nombre) VALUES (%(nombre)s);"
        return connectToMySQL('esquema_estudiantes_cursos').query_db(query, data)
    
    @classmethod
    def obtener_con_estudiantes(cls, id):
        query = """
        SELECT * FROM cursos
        LEFT JOIN estudiantes ON cursos.id = estudiantes.curso_id
        WHERE cursos.id = %(id)s;
        """
        results = connectToMySQL('esquema_estudiantes_cursos').query_db(query, {'id': id})
        curso = cls(results[0])
        curso.estudiantes = results if results else []
        return curso
