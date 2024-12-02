from flask import Flask
from dotenv import load_dotenv 
import os 
from flask_bcrypt import Bcrypt
load_dotenv() 

app = Flask(__name__)
app.secret_key = os.getenv('APP_SECRET_KEY')
bcrypt = Bcrypt(app)

