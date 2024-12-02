from flask import Flask
app = Flask(__name__)
app.secret_key = "APP_SECRET_KEY"  # Cambia esto por una clave segura