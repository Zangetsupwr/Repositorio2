from flask import redirect, render_template, request, session, flash
from flask_app import app
from flask_app.models import usuarios
from flask_app.models import publicaciones
from flask_app import bcrypt
from datetime import timedelta

from flask_app.utils.auth import session_required

# En la configuración de la app
app.permanent_session_lifetime = timedelta(minutes=30)


@app.route('/')
def index():
    return render_template('root/index.html')


@app.route('/register', methods=['POST'])
def register():
    # Validación inicial
    if (not usuarios.Usuario.validate(request.form)):
        return redirect('/')
    try:
        # Create user dict first, then encrypt password
        data = request.form.copy()
        # Validación adicional de contraseña
        if len(data['contraseña']) < 8:
            flash("La contraseña debe tener al menos 8 caracteres")
            return redirect('/')
            
        data['contraseña'] = bcrypt.generate_password_hash(request.form['contraseña'])
        nuevo_usuario = usuarios.Usuario(data)
        user_id = usuarios.Usuario.save(nuevo_usuario.__dict__())
        session['user_id'] = user_id
        return redirect('/dashboard')
    except Exception as e:
        flash("Error al registrar usuario")
        return redirect('/')


@app.route('/login', methods=['POST'])
def login():
    # 1. Validar que el usuario existe
    usuario = usuarios.Usuario.get_by_email(request.form['email'])
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
@session_required("/")
def logout():
    session.clear()
    return redirect('/')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    
    # Para debug
    print("Obteniendo publicaciones...")
    
    usuario = usuarios.Usuario.get_by_id(session['user_id'])
    todas_publicaciones = publicaciones.Publicacion.get_all()  # Asegúrate de que este método existe
    
    # Para debug
    print("Publicaciones encontradas:", todas_publicaciones)
    
    return render_template('root/dashboard.html',  # Asegúrate que la ruta del template sea correcta
                         usuario=usuario, 
                         publicaciones=todas_publicaciones)

@app.route('/publicaciones/create', methods=['POST'])
def create_publicacion():
    if 'user_id' not in session:
        return redirect('/')
        
    # Crear el diccionario de datos
    data = {
        'nombre': request.form['nombre'],
        'ingredientes': request.form['ingredientes'],
        'complementos': request.form['complementos'],
        'usuario_id': session['user_id']  # Importante: asociar con el usuario actual
    }
    
    # Validar los datos si es necesario
    if len(data['nombre']) < 1:
        flash('El nombre es requerido', 'nombre')
        return redirect('/dashboard')
        
    # Guardar en la base de datos
    publicaciones.Publicacion.save(data)
    return redirect('/dashboard')
