from flask_app import app, bcrypt
from flask import render_template, redirect, request, session, url_for
from flask_app.models.viaje import Viaje
""" from flask_app.models.usuarios import Usuario * """

# Ruta para la página de inicio de sesión/registro
@app.route('/')
def login_registro():
    return render_template('login_registro.html')

# Ruta para el dashboard
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    
    usuario = Usuario.get_by_id({'id': session['user_id']})
    todos_viajes = Viaje.get_all()
    
    # Debug
    print("Session user_id:", session['user_id'])
    print("Viajes:", todos_viajes)
    
    return render_template('root/dashboard.html', 
                         usuario=usuario, 
                         viajes=todos_viajes)

# Ruta para editar un viaje
@app.route('/editar/<int:viaje_id>')
def editar_viaje(viaje_id):
    # Verificar si el usuario ha iniciado sesión
    if 'user_id' not in session:
        return redirect(url_for('login_registro'))

    # Obtener los datos del viaje desde la base de datos
    viaje = Viaje.get_by_id(viaje_id)
    if not viaje:
        return "Viaje no encontrado", 404

    return render_template('editar_viaje.html', viaje=viaje)

# Ruta para agregar un nuevo viaje
@app.route('/nuevo_viaje')
def nuevo_viaje():
    # Verificar si el usuario ha iniciado sesión
    if 'user_id' not in session:
        return redirect(url_for('login_registro'))

    return render_template('nuevo_viaje.html')

# Ruta para cerrar sesión
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login_registro'))
