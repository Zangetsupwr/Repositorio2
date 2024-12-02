import os
from flask import Flask, render_template
from dotenv import load_dotenv


# CONFIGURACIÓN DE LA APLICACIÓN
load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv('APP_SECRET_KEY')