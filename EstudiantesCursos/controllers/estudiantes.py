from flask import render_template, redirect, request
from models.curso import Curso
from models.estudiante import Estudiante
from flask import app

@app.route('/estudiantes/nuevo')
def nuevo_estudiante():
    cursos = Curso.obtener_todos()
    return render_template('estudiantes/nuevo.html', cursos=cursos)

@app.route('/estudiantes/crear', methods=['POST'])
def crear_estudiante():
    data = {
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'],
        'edad': request.form['edad'],
        'curso_id': request.form['curso_id']
    }
    Estudiante.guardar(data)
    return redirect('/cursos')
