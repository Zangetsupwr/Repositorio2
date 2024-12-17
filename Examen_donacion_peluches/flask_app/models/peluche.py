from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Peluche:
    db = 'donacion_peluches'  # nombre de la base de datos
    
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.descripcion = data['descripcion']
        self.estado = data['estado']
        self.usuario_id = data['usuario_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.visitas = data.get('visitas', 0) 

    @classmethod
    def save(cls, data):
        try:
            print("Intentando guardar peluche con datos:", data)
            
            query = """
                INSERT INTO peluche 
                (nombre, descripcion, estado, usuario_id) 
                VALUES 
                (%(nombre)s, %(descripcion)s, %(estado)s, %(usuario_id)s);
            """
            
            print("Query a ejecutar:", query)
            print("Datos para la query:", data)
            
            resultado = connectToMySQL(cls.db).query_db(query, data)
            print("Resultado de la inserción:", resultado)
            
            return resultado
            
        except Exception as e:
            print("Error específico en save peluche:", str(e))
            return False

    @classmethod
    def get_all(cls):
        try:
            query = """
                SELECT 
                    p.*,
                    u.nombre as donador_nombre,
                    a.usuario_id as adoptador_id
                FROM peluche p
                JOIN usuarios u ON p.usuario_id = u.id
                LEFT JOIN adopcion a ON p.id = a.peluche_id
                ORDER BY p.created_at DESC;
            """
            return connectToMySQL(cls.db).query_db(query)
        except Exception as e:
            print("Error en get_all:", str(e))
            return []

    @classmethod
    def get_by_id(cls, data):
        try:
            query = """
                SELECT 
                    p.*,
                    u.nombre as donador_nombre,
                    (SELECT COUNT(DISTINCT v.usuario_id) 
                     FROM adopcion v 
                     WHERE v.peluche_id = p.id) as visitas
                FROM peluche p
                JOIN usuarios u ON p.usuario_id = u.id
                WHERE p.id = %(id)s;
            """
            
            results = connectToMySQL(cls.db).query_db(query, data)
            
            if not results:
                return None
            
            return results[0]
            
        except Exception as e:
            print("Error en get_by_id:", str(e))
            return None

    @classmethod
    def incrementar_visitas(cls, peluche_id, usuario_id):
        try:
            # Verificar que no sea el dueño del peluche
            query_check = """
                SELECT usuario_id 
                FROM peluche 
                WHERE id = %(peluche_id)s;
            """
            result = connectToMySQL(cls.db).query_db(query_check, {'peluche_id': peluche_id})
            
            if not result or result[0]['usuario_id'] == usuario_id:
                print("No se cuenta la visita del dueño")
                return False
            
            # Registrar la visita
            query = """
                INSERT INTO adopcion (usuario_id, peluche_id)
                VALUES (%(usuario_id)s, %(peluche_id)s)
                ON DUPLICATE KEY UPDATE created_at = NOW();
            """
            
            data = {
                'usuario_id': usuario_id,
                'peluche_id': peluche_id
            }
            
            print("Registrando visita:", data)
            return connectToMySQL(cls.db).query_db(query, data)
            
        except Exception as e:
            print("Error al registrar visita:", str(e))
            return False

    @classmethod
    def get_visitas_count(cls, peluche_id):
        try:
            query = """
                SELECT COUNT(DISTINCT usuario_id) as total_visitas
                FROM adopcion
                WHERE peluche_id = %(peluche_id)s;
            """
            result = connectToMySQL(cls.db).query_db(query, {'peluche_id': peluche_id})
            return result[0]['total_visitas'] if result else 0
        except Exception as e:
            print("Error al contar visitas:", str(e))
            return 0

    @classmethod
    def update(cls, data):
        try:
            # Debug de los datos recibidos
            print("Datos recibidos para actualizar:", data)
            
            query = """
                UPDATE peluche 
                SET nombre = %(nombre)s,
                    descripcion = %(descripcion)s,
                    estado = %(estado)s
                WHERE id = %(id)s 
                AND usuario_id = %(usuario_id)s
            """
            
            print("Query a ejecutar:", query)
            print("Datos para la query:", data)
            
            # Verificar que todos los campos necesarios estén presentes
            required_fields = ['nombre', 'descripcion', 'estado', 'id', 'usuario_id']
            for field in required_fields:
                if field not in data:
                    print(f"Falta el campo {field} en los datos")
                    return False
                
            result = connectToMySQL(cls.db).query_db(query, data)
            print("Resultado de la query:", result)
            return result
            
        except Exception as e:
            print("Error específico en update:", str(e))
            import traceback
            print(traceback.format_exc())
            return False

    @classmethod
    def adoptar(cls, peluche_id, usuario_id):
        try:
            # Verificar que el peluche existe y no está adoptado
            query_check = """
                SELECT p.id, p.usuario_id 
                FROM peluche p 
                LEFT JOIN adopcion a ON p.id = a.peluche_id 
                WHERE p.id = %(peluche_id)s;
            """
            result = connectToMySQL(cls.db).query_db(query_check, {'peluche_id': peluche_id})
            
            if not result:
                print("Peluche no encontrado")
                return False
            
            # No permitir que el dueño adopte su propio peluche
            if result[0]['usuario_id'] == usuario_id:
                print("No puedes adoptar tu propio peluche")
                return False
            
            # Insertar en la tabla de adopción
            query = """
                INSERT INTO adopcion (usuario_id, peluche_id) 
                VALUES (%(usuario_id)s, %(peluche_id)s);
            """
            
            data = {
                'usuario_id': usuario_id,
                'peluche_id': peluche_id
            }
            
            print("Ejecutando adopción con datos:", data)
            return connectToMySQL(cls.db).query_db(query, data)
            
        except Exception as e:
            print("Error al adoptar peluche:", str(e))
            return False

    @classmethod
    def esta_adoptado(cls, peluche_id):
        try:
            query = """
                SELECT COUNT(*) as count 
                FROM adopcion 
                WHERE peluche_id = %(peluche_id)s;
            """
            result = connectToMySQL(cls.db).query_db(query, {'peluche_id': peluche_id})
            return result[0]['count'] > 0
        except Exception as e:
            print("Error al verificar adopción:", str(e))
            return False