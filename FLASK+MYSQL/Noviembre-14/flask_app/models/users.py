from dataclasses import dataclass
from datetime import date
from typing import ClassVar
from flask_app.models.default_model import default_model

@dataclass(init=False)
class Users(default_model):
    table_name: ClassVar[str] = 'users'


    firstname: str
    lastname: str
    email: str
    username: str
    password: str
    address: str

    referral_id: int


# PRUEBAS DE LA CLASE
if __name__ == '__main__':
    pass