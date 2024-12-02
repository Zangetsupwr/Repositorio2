from dataclasses import dataclass, fields
from datetime import datetime
from typing import ClassVar
from default_model import default_model

@dataclass(init=False)
class species(default_model):
    name: str
    table_name : ClassVar[str] = "species"

# Pruebas de la clase
if __name__ == '__main__':
    roedor = {
        'id': 1,
        'created_at': datetime.now(),
        'updated_at':  datetime.now(),
        'name': 'Roedor'
    }
   
    roedor_instance = species(roedor)
    print(roedor_instance)