from flask_app import app
from flask import redirect, render_template, request
from flask_app.models.usuario import usuarios


# RUTA PARA VER TODOS LOS USUARIOS
@app.route('/usuarios')
def view():
    usuario_list = usuarios.all()
    return render_template('view.html', usuarios=usuario_list)

# RUTA DEL FORMULARIO DE CREACIÓN DE USUARIOS
@app.route('/usuarios/create',methods=['GET'])
def create():
    return render_template('create.html')

# RUTA PARA CREAR UN USUARIO QUE RECIBE LOS DATOS DEL FORMULARIO
@app.route('/usuarios/create', methods=['POST'])
def create_post():
    #request.form es un diccionario que contiene los datos del formulario
    new_usuario = usuarios(request.form)
    usuarios.save(new_usuario.__dict__())
    return redirect('/usuarios')

# RUTA PARA VER LOS DETALLES DE UN USUARIO
@app.route('/usuarios/<int:id>')
def detail(id):
    # Buscamos al usuario por su id
    usuario = usuarios.find_by_id(id)
    return render_template('usuarios/detail.html', usuarios=usuarios)

# RUTA PARA EDITAR UN USUARIO
@app.route('/usuarios/editar/<int:id>')
def editar(id):
    # Buscamos al usuario por su id
    usuario = usuarios.find_by_id(id)
    return render_template('usuarios/editar.html', usuario=usuario)

# RUTA PARA ACTUALIZAR LOS DATOS DE UN USUARIO
@app.route('/usuarios/editar/<int:id>', methods=['POST'])
def edit_post(id):
    # Creamos un objeto de la clase Users con los datos del formulario
    updated_usuario = usuarios(request.form)
    # Asignamos el id al objeto
    updated_usuario.id = id
    # Actualizamos los datos del usuario
    usuarios.update(updated_usuario.__dict__())
    return redirect('/usuarios')

# RUTA PARA ELIMINAR UN USUARIO
@app.route('/usuarios/<int:id>/delete')
def delete(id):
    usuarios.delete_by_id(id)
    return redirect('/usuarios')