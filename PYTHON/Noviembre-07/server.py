import os
from flask import Flask, redirect, render_template, request, session
from dotenv import load_dotenv

load_dotenv()

# Crear la aplicación
app = Flask(__name__)
app.secret_key = os.getenv('APP_SECRET_KEY')

# Ruta principal

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    usuario = request.form.get('username')
    role = request.form.get('role')
    session['username'] = usuario
    session['role'] = role
    return redirect('/dashboard')

# Ruta Secundaria

@app.route('/dashboard')
def dashboard():
    usuario = session.get('username')
    role = session.get('role')
    return render_template('dashboard.html', username=usuario, role=role)


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None)
    session.pop('role', None)
    return redirect('/dashboard')

# Iniciar la aplicación
if __name__ == '__main__':
    app.run(debug=True)