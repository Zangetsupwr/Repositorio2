from dataclasses import dataclass
from typing import ClassVar
from default_model import default_model

@dataclass(init=False)
class breeds(default_model):
    # Nombre de la tabla como atributo de la clase
    table_name: ClassVar[str] = 'breeds'

    # Atributos de la clase
    name: str
    specie_id: int



# Pruebas de la clase
if __name__ == '__main__':

    razas= breeds.all()
    print(razas)

    buscar_raza = breeds.find_by_id(102)
    print(buscar_raza)

    print(breeds.data_fields())
    data={
        'name': 'Pitbull',
        'specie_id': 1
    }
    breeds.save(data)