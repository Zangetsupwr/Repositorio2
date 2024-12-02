from flask_app import app
from flask import redirect, render_template, request
from flask_app.models.cursos import cursos
from flask_app.models.estudiantes import estudiantes


# RUTA PARA VER TODOS LOS USUARIOS
@app.route('/cursos')
def view():
    curso_list = cursos.all()
    return render_template('index.html', cursos=curso_list)

# RUTA DEL FORMULARIO DE CREACIÓN DE USUARIOS
@app.route('/cursos/create',methods=['GET'])
def create():
    return render_template('/cursos')

# RUTA PARA CREAR UN USUARIO QUE RECIBE LOS DATOS DEL FORMULARIO
@app.route('/cursos/create', methods=['POST'])
def create_post():
    #request.form es un diccionario que contiene los datos del formulario
    new_curso = cursos(request.form)
    cursos.save(new_curso.__dict__())
    return redirect('/cursos')


@app.route('/cursos/<int:id>', methods=['GET'])
def view_cursos_estudiantes(id):
    curso = cursos.find_by_id(id)
    estudiantes_list = estudiantes.all_curso_estudiante(id)
    return render_template('nuevo.html', curso=curso, estudiantes=estudiantes_list)