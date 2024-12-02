from flask_app import app
from flask import render_template,redirect
from flask_app.models.breeds import breeds

@app.route('/')
def index():
    return redirect('/breeds')
# RUTAS DE LA APLICACIÓN
@app.route('/breeds')
def show_breeds():
    breed_list = breeds.all()
    return render_template('breeds.html', breeds=breed_list)