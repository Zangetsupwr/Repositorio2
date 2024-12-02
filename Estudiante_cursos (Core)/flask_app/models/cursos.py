from dataclasses import dataclass
from datetime import date, datetime
from typing import ClassVar
from flask_app.models.default_model import default_model

@dataclass(init=False)
class cursos(default_model):
    table_name: ClassVar[str] = 'cursos'
    
    nombre: str


# PRUEBAS DE LA CLASE
if __name__ == '__main__':
    pass