from flask import flash, redirect, render_template, request, session
from flask_app import app
from flask_app.config.security import session_required

from flask_app.models.usuarios import Usuarios
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


@app.route('/home')
def home():
    if 'usuario_id' not in session:
        return redirect('/')
    
    # Obtener el usuario actual usando el ID guardado en sesión
    usuario = Usuarios.get_by_id(session['usuario_id'])
    return render_template('/home/home.html', usuario=usuario)


@app.route('/')
def root():
    return render_template('/home/login.html')


@app.route('/login', methods=['POST'])
def login():
    # Buscar el usuario en la base de datos
    email = request.form.get('email')
    user = Usuarios.find_by_email(email)
    
    if not user:
        flash('Email/Contraseña inválidos', 'login')
        return redirect('/')
        
    if not bcrypt.check_password_hash(user.contraseña, request.form.get('contraseña')):
        flash('Email/Contraseña inválidos', 'login')
        return redirect('/')
    
    # Guardar solo el ID del usuario en la sesión (no el objeto completo)
    session['usuario_id'] = user.id
    return redirect('/home')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
