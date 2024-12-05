from flask import redirect, render_template, request, session, flash
from flask_app import app
from flask_app.models.usuarios import Usuario
from flask_app import bcrypt
from flask_app.models.viajes import Viajes

@app.route('/')
def index():
    return render_template('root/index.html')

@app.route('/registro', methods=['POST'])
def registrar_usuario():
    try:
        # Obtener datos del formulario
        data = {
            'nombre': request.form.get('nombre'),
            'apellido': request.form.get('apellido'),
            'email': request.form.get('email'),
            'password': request.form.get('password'),
            'confirm_password': request.form.get('confirm_password')
        }

        # Debug: imprimir los datos recibidos
        print("Datos recibidos:", data)

        # Validar datos
        if not Usuario.validate(data):
            return redirect('/')

        # Crear usuario con contraseña hasheada
        data['contraseña'] = bcrypt.generate_password_hash(data['password'])
        
        # Guardar usuario
        usuario_id = Usuario.save(data)
        
        # Guardar id en sesión
        session['user_id'] = usuario_id
        
        return redirect('/dashboard')
        
    except Exception as e:
        print("Error en registro:", e)
        flash("Error al procesar el registro", "registro")
        return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    try:
        # Verificar que el usuario existe
        usuario = Usuario.get_by_email(request.form['email'])
        
        if not usuario:
            flash('Email/Contraseña inválidos', 'login')
            return redirect('/')
        
        # Verificar que la contraseña coincide
        if not bcrypt.check_password_hash(usuario.contraseña, request.form.get('contraseña')):
            flash('Email/Contraseña inválidos', 'login')
            return redirect('/')
        
        # Guardar id en sesión
        session['user_id'] = usuario.id
        return redirect('/dashboard')
        
    except Exception as e:
        print("Error en login:", e)
        flash('Error al iniciar sesión', 'login')
        return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    
    usuario = Usuario.get_by_id({'id': session['user_id']})
    todos_viajes = Viajes.get_all()
    
    # Debug
    print("Session user_id:", session['user_id'])
    print("Viajes:", todos_viajes)
    
    return render_template('root/dashboard.html', 
                         usuario=usuario, 
                         viajes=todos_viajes)
