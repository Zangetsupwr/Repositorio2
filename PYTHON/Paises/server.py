import os
from flask import Flask ,render_template
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('APP_SECRET_KEY')

@app.route('/')
def principal():
    paises = [

   {'pais': 'Argentina' , 'capital': 'Buenos Aires'},

   {'pais': 'Brasil' , 'capital': 'Brasilia'},

   {'pais': 'Chile' , 'capital': 'Santiago de Chile'},

   {'pais': 'Colombia' , 'capital': 'Bogotá'},

   {'pais': 'Costa Rica' , 'capital': 'San José'},

   {'pais': 'Paraguay' , 'capital': 'Asunción'},

   {'pais': 'Perú' , 'capital': 'Lima'}

]
    return render_template('index.html',paises=paises)

if __name__ == '__main__':
    app.run(debug=True)