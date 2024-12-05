from flask import flash, redirect, render_template, request, session
from flask_app import app
from flask_app.models import usuarios
from flask_bcrypt import bcrypt

@app.route('/')
def index():
    return render_template('root/index.html')

@app.route('/login', methods=['POST'])
def login():
    # 1. Validar que el usuario existe
    usuario = usuarios.Usuario.get_by_email(request.form['email'])  # Usar la clase de usuarios
    if not usuario:
        flash('Email/Contraseña inválidos')
        return redirect('/')
    
    # 2. Validar la contraseña
    if not bcrypt.check_password_hash(usuario.contraseña, request.form['contraseña']):
        flash('Email/Contraseña inválidos')
        return redirect('/')
    
    # 3. Si todo está bien, guardar en sesión y redirigir
    session['user_id'] = usuario.id
    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')