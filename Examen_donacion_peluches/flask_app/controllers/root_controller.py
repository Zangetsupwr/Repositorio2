from flask import redirect, render_template, request, session, flash
from flask_app import app
from flask_app.models.usuarios import Usuario
from flask_app import bcrypt
from flask_app.models.peluche import Peluche

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
        
        # Debug: imprimir datos antes de guardar
        print("Datos a guardar:", {k:v for k,v in data.items() if k != 'password'})
        
        # Guardar usuario
        usuario_id = Usuario.save(data)
        
        # Debug: imprimir ID generado
        print("ID de usuario generado:", usuario_id)
        
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
        # Debug: imprimir datos recibidos
        print("Datos de login recibidos:", request.form)
        
        # Verificar que el usuario existe
        usuario = Usuario.get_by_email(request.form['email'])
        
        # Debug: imprimir usuario encontrado
        print("Usuario encontrado:", usuario.__dict__ if usuario else None)
        
        if not usuario:
            flash('Email/Contraseña inválidos', 'login')
            return redirect('/')
        
        # Verificar que la contraseña coincide
        if not bcrypt.check_password_hash(usuario.contraseña, request.form['password']):
            flash('Email/Contraseña inválidos', 'login')
            return redirect('/')
        
        # Guardar id en sesión
        session['user_id'] = usuario.id
        print("ID guardado en sesión:", session['user_id'])
        
        return redirect('/dashboard')
        
    except Exception as e:
        print("Error en login:", str(e))
        flash('Error al iniciar sesión', 'login')
        return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/dashboard')
def dashboard():
    # Debug: imprimir sesión
    print("Sesión actual:", session)
    
    if 'user_id' not in session:
        print("No hay usuario en sesión")
        return redirect('/')
    
    try:
        usuario = Usuario.get_by_id({'id': session['user_id']})
        
        # Debug: imprimir usuario
        print("Usuario del dashboard:", usuario.__dict__ if usuario else None)
        
        todos_peluches = Peluche.get_all()
        
        # Debug: imprimir peluches
        print("Peluches encontrados:", todos_peluches)
        
        return render_template('root/dashboard.html', 
                             usuario=usuario, 
                             todos_peluches=todos_peluches)
    except Exception as e:
        print("Error en dashboard:", str(e))
        session.clear()
        return redirect('/')
