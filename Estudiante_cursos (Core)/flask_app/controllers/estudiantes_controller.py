from flask_app import app
from flask import redirect, render_template, request
from flask_app.models.estudiantes import estudiantes


# RUTA PARA VER TODOS LOS USUARIOS
@app.route('/estudiantes')
def view():
    estudiantes_list = estudiantes.all()
    return render_template('nuevo.html', estudiantes=estudiantes_list)

# RUTA DEL FORMULARIO DE CREACIÓN DE USUARIOS
@app.route('/estudiantes/create',methods=['GET'])
def create():
    return render_template('/estudiantes')

# RUTA PARA CREAR UN ESTUDIANTE QUE RECIBE LOS DATOS DEL FORMULARIO
@app.route('/estudiantes/create', methods=['POST'])
def create_post():
    #request.form es un diccionario que contiene los datos del formulario
    new_estudiante = estudiantes(request.form)
    estudiantes.save(new_estudiante.__dict__())
    return redirect('/estudiantes')

# RUTA PARA VER LOS DETALLES DE UN USUARIO
@app.route('/estudiantes/<int:id>')
def detail(id):
    # Buscamos al usuario por su id
    estudiante = estudiantes.find_by_id(id)
    return render_template('estudiantes/detail.html', estudiante=estudiantes)

# RUTA PARA EDITAR UN USUARIO
@app.route('/estudiantes/<int:id>/edit')
def edit(id):
    # Buscamos al usuario por su id
    estudiante = estudiantes.find_by_id(id)
    return render_template('estudiantes/edit.html', estudiante=estudiantes)

# RUTA PARA ACTUALIZAR LOS DATOS DE UN USUARIO
@app.route('/estudiantes/<int:id>/edit', methods=['POST'])
def edit_post(id):
    # Creamos un objeto de la clase Users con los datos del formulario
    updated_estudiante = estudiantes(request.form)
    # Asignamos el id al objeto
    updated_estudiante.id = id
    # Actualizamos los datos del usuario
    estudiantes.update(updated_estudiante.__dict__())
    return redirect('/')

# RUTA PARA ELIMINAR UN USUARIO
@app.route('/estudiantes/<int:id>/delete')
def delete(id):
    estudiantes.delete_by_id(id)
    return redirect('/')