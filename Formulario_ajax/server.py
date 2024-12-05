from flask import Flask, request, jsonify, render_template
import pymysql
import re
from contextlib import contextmanager

app = Flask(__name__)

# Configuración de conexión a la base de datos
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'formulario_ajax'
}

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

@contextmanager
def get_db_connection():
    connection = pymysql.connect(**db_config)
    try:
        yield connection
    finally:
        connection.close()

# Ruta principal
@app.route('/')
def index():
    with get_db_connection() as connection:
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM usuarios")
        usuarios = cursor.fetchall()
    return render_template('index.html', usuarios=usuarios)

# Ruta para agregar un nuevo usuario
@app.route('/add_user', methods=['POST'])
def add_user():
    try:
        data = request.json
        nombre = data.get('nombre')
        email = data.get('email')
        
        if not nombre or not email:
            return jsonify({'error': 'Faltan campos requeridos'}), 400
        
        connection = pymysql.connect(**db_config)
        cursor = connection.cursor()
        try:
            query = "INSERT INTO usuarios (nombre, email) VALUES (%s, %s)"
            cursor.execute(query, (nombre, email))
            connection.commit()
            new_id = cursor.lastrowid
            return jsonify({'id': new_id, 'nombre': nombre, 'email': email})
        except Exception as e:
            return jsonify({'error': f'Error de base de datos: {str(e)}'}), 500
        finally:
            connection.close()
            
    except Exception as e:
        return jsonify({'error': f'Error del servidor: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
