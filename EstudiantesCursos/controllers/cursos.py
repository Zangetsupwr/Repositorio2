from flask import render_template, redirect, request
from models.curso import Curso
from flask import app

@app.route('/')
def index_cursos():
    cursos = Curso.obtener_todos()
    return render_template('index.html', cursos=cursos)

@app.route('/cursos/crear', methods=['POST'])
def crear_curso():
    data = {'nombre': request.form['nombre']}
    Curso.guardar(data)
    return redirect('/cursos')

@app.route('/cursos/<int:id>')
def mostrar_curso(id):
    curso = Curso.obtener_con_estudiantes(id)
    return render_template('cursos/mostrar.html', curso=curso)
