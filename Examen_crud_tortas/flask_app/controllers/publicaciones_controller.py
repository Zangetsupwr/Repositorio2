from flask import flash, redirect, request, session,render_template
from flask_app import app
from flask_app.models import publicaciones
from flask_app.models import usuarios
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.utils.auth import session_required

@app.route('/publicaciones/create', methods=['POST'])
def crear_publicacion():
    if 'user_id' not in session:
        return redirect('/')
        
    data = {
        'nombre': request.form['nombre'],
        'ingredientes': request.form['ingredientes'],
        'complementos': request.form['complementos'],
        'usuario_id': session['user_id']
    }
    
    publicaciones.Publicacion.save(data)
    return redirect('/dashboard')


@app.route('/publicaciones/<int:id>/editar',methods=['POST'])
def edit_publicacion(id):
    if 'user_id' not in session:
        return redirect('/')
    
    data = {'id': id}
    publicacion = publicaciones.Publicacion.get_by_id(data)
    
    return render_template('publicaciones/editar.html', publicacion=publicacion)


@app.route('/publicaciones/update/<int:id>', methods=['POST'])
def update_publicacion(id):
    if 'user_id' not in session:
        return redirect('/')
    
    data = {
        'id': id,
        'nombre': request.form['nombre'],
        'ingredientes': request.form['ingredientes'],
        'complementos': request.form['complementos']
    }
    
    if not publicaciones.Publicacion.validate_2(data):
        return redirect(f'/publicaciones/{id}/editar')

    publicaciones.Publicacion.update(data)
    return redirect('/dashboard')


@app.route('/publicaciones/delete/<int:id>', methods=['POST'])
def delete_publicacion(id):
    if 'user_id' not in session:
        return redirect('/')
    print(f"Intentando eliminar publicación {id}")
    data = {'id': id}
    publicaciones.Publicacion.delete_by_id(data)
    return redirect('/dashboard')

@app.route('/like', methods=['POST'])
def like():
    if 'user_id' not in session:
        return redirect('/')
    # Agregar print para debug
    print("Form data:", request.form)
    try:
        data = {
            'publicacion_id': request.form['publicacion_id'],
            'usuario_id': session['user_id']
        }
        publicaciones.Publicacion.like(data)
        return redirect(f'/publicaciones/ver/{data["publicacion_id"]}')
    except KeyError as e:
        print("Error:", e)
        return redirect('/dashboard')

# Método para obtener una publicación por ID en el modelo
@classmethod
def get_by_id(cls, data):
    query = "SELECT * FROM publicaciones WHERE id = %(id)s;"
    results = connectToMySQL('recetas').query_db(query, data)
    if results:
        return cls(results[0])
    return None  

@app.route('/publicaciones/listado')
def listado_tortas():
    todas_publicaciones = publicaciones.Publicacion.get_all()
    return render_template('publicaciones/Tortas.html', publicaciones=todas_publicaciones)

@app.route('/publicaciones/ver/<int:id>')
def ver_publicacion(id):
    if 'user_id' not in session:
        return redirect('/')
    
    data = {'id': id}
    publicacion = publicaciones.Publicacion.get_by_id(data)
    
    if not publicacion:
        flash("Publicación no encontrada")
        return redirect('/dashboard')
    
    # Obtener el autor de la publicación
    from flask_app.models.usuarios import Usuario
    autor = Usuario.get_by_id({'id': publicacion.usuario_id})
    
    has_liked = publicaciones.Publicacion.user_has_liked(id, session['user_id'])
    
    return render_template('publicaciones/ver.html', 
                         publicacion=publicacion, 
                         has_liked=has_liked,
                         autor=autor)