from flask import redirect, render_template, request, session
from flask_app import app
from flask_app.models import publicaciones

from flask_app.utils.auth import session_required

@app.route('/publicaciones/create', methods=['POST'])
@session_required("/")
def create_publicacion():
    # Copiar los datos del formulario para no modificar el original
    data = request.form.copy()
    data['owner_id'] = 1  # Cambiar por el id del usuario logueado
    if (not publicaciones.Publicacion.validate_2(data)):
        return redirect('/dashboard')

    # Crear la nueva publicación
    nueva_publicacion = publicaciones.Publicacion(data)
    publicaciones.Publicacion.save(nueva_publicacion.__dict__())
    return redirect('/dashboard')


@app.route('/publicaciones/<int:id>/edit')
@session_required("/")
def edit_publicacion(id):
    publicacion = publicaciones.Publicacion.find_by_id(id)
    if (publicacion.owner_id != session['user_id']):
        return redirect('/dashboard')
    return render_template('publicaciones/edit.html', publicacion=publicacion)


@app.route('/publicaciones/<int:id>/edit', methods=['POST'])
@session_required("/")
def update_publicacion(id):
    data = request.form.copy()
    data['id'] = id
    data['owner_id'] = session['user_id']
    if (not publicaciones.Publicacion.validate_2(data)):
        return redirect(f'/publicaciones/{id}/edit')
    update_publicacion = publicaciones.Publicacion(data)
    publicaciones.Publicacion.update(update_publicacion.__dict__())
    return redirect('/dashboard')


@app.route('/publicaciones/<int:id>/delete')
@session_required("/")
def delete_publicacion(id):
    publicaciones.Publicacion.delete_by_id(id)
    return redirect('/dashboard')


@app.route('/like', methods=['POST'])
@session_required("/")
def like():
    # Copiar los datos del formulario para no modificar el original
    data = request.form.copy()
    # Cambiar el usuario_id por el id del usuario logueado
    data['usuario_id'] = session['user_id']
    # Llamar al método like del modelo de publicaciones
    publicaciones.Publicacion.like(data)
    return redirect('/dashboard')