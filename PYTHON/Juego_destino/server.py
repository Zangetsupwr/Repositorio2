import os
from flask import Flask ,render_template,redirect,request,url_for,session
import random
from dotenv import load_dotenv

app = Flask(__name__)
app.secret_key = os.getenv('APP_SECRET_KEY')

load_dotenv()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    nombre = request.form.get('nombre')
    lugar =request.form.get('lugar')
    numero = request.form.get('numero')
    comida = request.form.get('comida')
    profesion = request.form.get('profesion')
   
    session['datos'] = {
        'nombre': nombre,
        'lugar': lugar,
        'numero': numero,
        'comida': comida,
        'profesion': profesion
    }
    return redirect(url_for('futuro')) 

@app.route('/futuro')
def futuro():
    datos = session.get('datos')
    return render_template('futuro.html', datos=datos)

@app.route('/mensaje', methods=['POST']) 
def mensaje(): 
    nombre = request.form.get('nombre') 
    comida = request.form.get('comida') 
    numero = request.form.get('numero') 
    lugar = request.form.get('lugar') 
    mensajes = [ f"Soy el adivino del Dojo, {nombre} tendrá {numero} años de mala suerte, nunca conocerá {lugar} y jamás volvió a comer {comida}.", "¡Has tenido mala suerte JAJAJAJA!" , "No te ama ella XD"] 
    # Elige aleatoriamente un mensaje 
    mensaje = random.choice(mensajes) 
    return redirect(url_for('resultado', mensaje=mensaje)) 

@app.route('/resultado') 
def resultado(): 
   mensaje = request.args.get('mensaje', '')
   return render_template('mensaje.html',mensaje=mensaje)


if __name__ == '__main__':
    app.run(debug=True)