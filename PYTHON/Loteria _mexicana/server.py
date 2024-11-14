import os
from flask import Flask ,render_template,redirect
from dotenv import load_dotenv
import random

load_dotenv()

# Crear la aplicación
app = Flask(__name__)
app.secret_key = os.getenv('APP_SECRET_KEY')

# Cuando el usuario visite http://127.0.0.1:5000/loteria, 
# se debería mostrar un tablero de juego de 4 por 4;

@app.route('/')
def index():
    return redirect('/loteria')

@app.route('/loteria')
def root():
    cartas = ["1  El Gallo","2  El Diablito","3 La Dama",
"4  El catrín","5  El paraguas","6  La sirena","7  La escalera","8  La botella",
"9  El barril","10 El árbol","11 El melón","12 El valiente","13 El gorrito",
"14 La muerte","15 La pera","16 La bandera","17 El bandolón","18 El violoncello",
"19 La garza", "20 El pájaro","21 La mano","22 La bota","23 La luna",
"24 El cotorro", "25 El borracho","26 El negrito","27 El corazón","28 La sandía","29 El tambor",
"30 El camarón","31 Las jaras","32 El músico","33 La araña","34 El soldado",
"35 La estrella","36 El cazo","37 El mundo","38 El apache","39 El nopal","40 El alacrán",
"41 La rosa","42 La calavera","43 La campana","44 El cantarito","45 El venado",
"46 El sol","47 La corona","48 La chalupa","49 El pino","50 El pescado","51 La palma",
"52 La maceta","53 El arpa","54 La rana"]
    
    colores = ['square-pink', 'square-blue', 'square-yellow']
    cartas_seleccionadas = random.sample(cartas, 12)
    cartas_con_datos = [{
        'numero': random.randint(1, 54),  
        'nombre': carta,
        'color': random.choice(colores)   
    } for carta in cartas_seleccionadas]
    return render_template('index.html',cartas=cartas_con_datos,colores=colores)

#---------------------------------------------------------

#si la URL es http://127.0.0.1:5000/5 
# debería mostrarse un tablero de 4 columnas y 5 filas.
@app.route('/<int:rows>')
def tablero(rows):
    columns = 4
    return render_template('tablero.html',rows=rows,columns=columns)


@app.route('/<int:rows>/<int:columns>')
def tablero2(rows,columns):
    return render_template('tablero2.html',rows=rows,columns=columns)

if __name__ == '__main__':
    app.run(debug=True)