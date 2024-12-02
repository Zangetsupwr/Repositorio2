from flask import redirect, render_template, request, session
from flask_app import app
from flask_app.models import usuarios
from flask_app.models import publicaciones
from flask_app import bcrypt

from flask_app.utils.auth import session_required

@app.route('/')
def index():
    return render_template('root/index.html')


@app.route('/register', methods=['POST'])
def register():
    if (not usuarios.Usuario.validate(request.form)):
        return redirect('/')
    # Encriptar la contraseña
    nuevo_usuario = usuarios.Usuario(request.form)
    nuevo_usuario.contraseña = bcrypt.generate_password_hash(request.form['contraseña'])
    user_id = usuarios.Usuario.save(nuevo_usuario.__dict__())
    session['user_id'] = user_id
    return redirect('/dashboard')


@app.route('/login', methods=['POST'])
def login():
    user_id = usuarios.Usuario.validate_login(request.form)
    if (not user_id):
        return redirect('/')
    session['user_id'] = user_id
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    user = usuarios.Usuario.find_by_id(session['user_id'])
    recetas_list = publicaciones.Publicacion.all()
    return render_template('root/dashboard.html', usuario=user, publicaciones=recetas_list)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')