from dataclasses import dataclass, fields
from datetime import datetime
from typing import ClassVar
from flask_app.config.mysqlconnection import connectToMySQL

from dotenv import load_dotenv
import os

load_dotenv()

@dataclass
class DefaultModel:
    table_name: ClassVar[str] = None

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
        query = f'SELECT * FROM {cls.table_name}'
        results = connectToMySQL(os.getenv('DB_NAME')).query_db(query)
        instances = []
        for result in results:
            instances.append(cls(result))
        return instances
    
    # Método para obtener todos los registros de la tabla con un query parametrizado
    @classmethod
    def all_by_query(cls,query):
        results = connectToMySQL(os.getenv('DB_NAME')).query_db(query)
        instances = []
        for result in results:
            instances.append(cls(result))
        return instances
  

    # Método para obtener el registros de la tabla segun el id
    @classmethod
    def find_by_id(cls, id:int):
        try:
            query = f'SELECT * from {cls.table_name} WHERE id={id}'
            result = connectToMySQL(os.getenv('DB_NAME')).query_db(query)
            return cls(result[0])
        except Exception as e:
            print(e)
            return None
        
    # Método para insertar registros en la tabla
    @classmethod
    def save(cls, data):
        query = f'INSERT INTO {cls.table_name} ({cls.get_fields()}) VALUES ({cls.get_data_values()})'
        return connectToMySQL(os.getenv('DB_NAME')).query_db(query, data)
    
    # Método para actualizar registros en la tabla por id
    @classmethod
    def update_by_id(cls,data):
        query = f'UPDATE {cls.table_name} SET {cls.string_update()} WHERE id = %(id)s'
        return connectToMySQL(os.getenv('DB_NAME')).query_db(query, data)
    
    # Método para actualizar registros en la tabla 
    @classmethod
    def update(cls, data):
        query = f'UPDATE {cls.table_name} ({cls.get_fields()}) VALUES ({cls.get_data_values()})'
        return connectToMySQL(os.getenv('DB_NAME')).query_db(query, data)

    # Método para eliminar un registro de la tabla
    @classmethod
    def delete_by_id(cls, id:int):
        # Crea el query
        query = f'DELETE FROM {cls.table_name} WHERE id = {id}'
        return connectToMySQL(os.getenv('DB_NAME')).query_db(query)

    # Método para ver todos los campos
    @classmethod
    def data_fields(cls):
        class_data_fields = []
        for field in fields(cls):
            if (field.name != 'id' and field.name != 'created_at' and field.name != 'updated_at'):
                class_data_fields.append(field.name)
        return class_data_fields
    # Método para obtener todos los campos separados por coma
    @classmethod
    def get_fields(cls):
        return ', '.join(cls.data_fields())
    # Método para ver los valores de  todos los campos separados por coma
    @classmethod
    def get_data_values(cls):
        return ', '.join([f'%({field})s' for field in cls.data_fields()])
    # Método para ver los campos y sus valores en formato 'campo=valor' separados por coma
    @classmethod
    def string_update(cls):
        return ', '.join([f'{field} = %({field})s' for field in cls.data_fields()])
    
    # Método para correr y retornar una query parametrizada
    @staticmethod
    def run_query(query, data):
        return connectToMySQL(os.getenv('DB_NAME')).query_db(query, data)