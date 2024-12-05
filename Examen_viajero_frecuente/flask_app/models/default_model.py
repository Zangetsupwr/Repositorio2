
import os
from dotenv import load_dotenv
from dataclasses import dataclass, fields
from datetime import datetime
from typing import ClassVar
# Cambiar por la línea anterior si se usa el archivo mysqlconnection.py
from flask_app.config.mysqlconnection import connectToMySQL

load_dotenv()
db_name = os.getenv('DB_NAME')
# Clase que define el modelo por defecto de las tablas de la base de datos


@dataclass(init=False)
class default_model:
    # Nombre de la tabla como atributo de la clase
    table_name: ClassVar[str] = None

    # Atributos de la clase
    id: int
    created_at: datetime
    updated_at: datetime

    # Constructor
    def __init__(self, data):
        # Asignar los valores de los atributos a partir de los datos recibidos en el constructor de la clase
        for field in fields(self):
            # si el campo es de tipo int entonces colocamos None cuando esté vacío
            if field.type == int and data.get(field.name) == '':
                setattr(self, field.name, None)
            else:
                setattr(self, field.name, data.get(field.name))

    def __dict__(self):
        # Crear un diccionario con los atributos de la clase
        data = {}
        for field in fields(self):
            data[field.name] = getattr(self, field.name)
        return data

    # Métodos CRUD

    # Método para obtener todos los registros de la tabla

    @classmethod
    def all(cls):
        # Crear el query
        query = f'SELECT * FROM {cls.table_name}'
        # Obtener los resultados
        results = connectToMySQL(db_name).query_db(query)
        # Crear una lista de objetos de la clase
        instances = []
        # Crear una instancia de la clase por cada resultado
        for result in results:
            instances.append(cls(result))
        # Retornar la lista de instanciasF
        return instances

    # Método para obtener un registro de la tabla por su id
    @classmethod
    def find_by_id(cls, id):
        try:
            # Crea el query
            query = f'SELECT * FROM {cls.table_name} WHERE id = {id}'
            # Obtiene el resultado
            result = connectToMySQL(db_name).query_db(query)
            # Retorna una instancia de la clase con el resultado obtenido en la posición 0
            return cls(result[0])
        except:
            return None

    # Método para guardar un registro en la tabla
    @classmethod
    def save(cls, data):
        # Crea el query
        query = f'INSERT INTO {cls.table_name} ({cls.string_fields()}) VALUES ({
            cls.string_values()})'
        # Retorna el id del nuevo registro
        return connectToMySQL(db_name).query_db(query, data)

    # Método para actualizar un registro de la tabla
    @classmethod
    def update(cls, data):
        # Crea el query
        query = f'UPDATE {cls.table_name} SET {
            cls.string_update()} WHERE id = %(id)s'
        # Retorna el id del registro editado
        return connectToMySQL(db_name).query_db(query, data)

    # Método para eliminar un registro de la tabla
    @classmethod
    def delete_by_id(cls, id):
        # Crea el query
        query = f'DELETE FROM {cls.table_name} WHERE id = {id}'
        return connectToMySQL(db_name).query_db(query)

    @classmethod
    # Método para ver todos los campos
    def data_fields(cls):
        class_data_fields = []
        for field in fields(cls):
            if (field.name != 'id' and field.name != 'created_at' and field.name != 'updated_at'):
                class_data_fields.append(field.name)
        return class_data_fields

    @classmethod
    def string_fields(cls):
        return ', '.join(cls.data_fields())

    @classmethod
    def string_values(cls):
        return ', '.join([f'%({field})s' for field in cls.data_fields()])

    @classmethod
    def string_update(cls):
        return ', '.join([f'{field} = %({field})s' for field in cls.data_fields()])

    @staticmethod
    def run_query(query, data):
        return connectToMySQL(db_name).query_db(query, data)


# PRUEBAS
if __name__ == '__main__':
    pass
