from dataclasses import InitVar, dataclass
from datetime import date
from typing import ClassVar
from flask_app.models.default_model import default_model
from flask_app.config.mysqlconnection import connectToMySQL

@dataclass(init=False)
class estudiantes(default_model):
    table_name: ClassVar[str] = 'estudiante'

    nombre: str
    apellido: str
    edad: str

    @classmethod
    def all_curso_estudiante(cls,id):
        query = f'SELECT * FROM {cls.table_name} WHERE curso_id = {id}'
        #Obtener los resultados
        results = connectToMySQL('red_social').query_db(query)
        #Crear una lista de objetos de la clase
        instances = []
        #Crear una instancia de la clase por cada resultado
        for result in results:
            instances.append(cls(result))
        #Retornar la lista de instancias
        return instances

# PRUEBAS DE LA CLASE
if __name__ == '__main__':
    pass
