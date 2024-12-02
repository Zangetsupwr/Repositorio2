from datetime import date
import re
from flask import flash
from flask_app import bcrypt

# Función decoradora para crear el mensaje en una categoria especifica si se cumple un condicion


def error_message(if_condition: bool = False, message: str = "ERROR: Intentelo de nuevo", message_category: str = "error"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if (result == if_condition):
                flash(message, message_category)
            return result
        return wrapper
    return decorator


# Función que devuelve True si la contraseña a verificar (no hasheada) es igual a la contraseña hasheade guardada en DB
def contraseña_valida(hasheada_db: str, a_verificar: str) -> bool:
    es_valido = True
    if (bcrypt.check_password_hash(hasheada_db, a_verificar)) == False:
        es_valido = False
    return es_valido

# Función que devuelve True si el texto1 es igual a al texto2


def textos_iguales(texto1: str = None, texto2: str = None) -> bool:
    es_valido = True
    if not texto2 == texto1:
        es_valido = False
    return es_valido

# Función que devuelve True si el texto es igual a otro valor a comparar


def texto_igual_valor(texto: str = None, valor_comparar: str = None) -> bool:
    es_valido = True
    if texto == valor_comparar:
        es_valido = False

    return es_valido

# Función que devuelve True si el valor dado se encuentra en la lista


def valor_en_lista(valor: str, lista_objetos: list[object]) -> bool:
    valor_existe = False
    if valor in lista_objetos:
        valor_existe = True

    return valor_existe

# Función que devuelve True si el texto dado esta vacio ("") o es nulo (None)


def esta_vacio(texto: str) -> bool:
    esta_vacio = False
    if texto == None or texto == "":
        esta_vacio = True

    return esta_vacio

# Función que devuelve True si el texto cumple con un patron especifico


def patron_valido(texto: str, patron: str) -> bool:
    REGEX = re.compile(patron)
    es_valido = True
    if not REGEX.match(texto):
        es_valido = False
    return es_valido

# Función que devuelve True si la fecha de nacimiento dada es mayor la edad minima


def mayor_edad(fecha_nacimiento: date = None, edad_min: int = 18) -> bool:
    es_valido = True
    hoy = date.today()
    edad = hoy.year - fecha_nacimiento.year - \
        ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    if edad < edad_min:
        es_valido = False
    return es_valido

# Función que devuelve True si la fecha dada es menor a la fecha actual


def fecha_anterior(fecha: date = None) -> bool:
    es_valido = True
    hoy = date.today()
    if fecha > hoy:
        es_valido = False
    return es_valido

# Función que devuelve True si la fecha dada es mayor a la fecha actual


def fecha_posterior(fecha: date = None) -> bool:
    es_valido = True
    hoy = date.today()
    if fecha < hoy:
        es_valido = False
    return es_valido

# Función que devuelve True si el texto tiene un largo minimo de caracteres.


def cumple_largo_min(texto: str, largo_min: int) -> bool:
    resultado = True
    if len(texto) < largo_min:
        resultado = False
    return resultado

# Función que devuelve True si el texto contiene al menos una mayuscula


def tiene_mayusc(texto: str) -> bool:
    resultado = False

    for letra in texto:
        if letra.isupper():
            resultado = True
            break
    return resultado

# Función que devuelve True si el texto contiene al menos una minuscula


def tiene_minusc(texto: str) -> bool:
    resultado = False

    for letra in texto:
        if letra.islower():
            resultado = True
            break
    return resultado

# Función que devuelve True si el texto contiene al menos un numero


def tiene_numero(texto: str) -> bool:
    resultado = False

    for letra in texto:
        if letra.isdigit():
            resultado = True
            break
    return resultado

# Función que devuelve True si el texto contiene solo letras


def solo_letras(texto: str) -> bool:
    resultado = True

    if texto.isalpha() == False:
        resultado = False

    return resultado
