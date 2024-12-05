from flask import Flask
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

# Inicialización de la aplicación Flask
app = Flask(__name__)

# Configuración de la clave secreta para las sesiones
app.secret_key = os.getenv('APP_SECRET_KEY', 'default_secret_key')

# Inicialización de Bcrypt para encriptación
bcrypt = Bcrypt(app)

# Importar los controladores después de inicializar la aplicación
from flask_app.controllers import user_controller, viaje_controller
