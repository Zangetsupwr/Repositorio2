from flask import Flask , render_template
app2 = Flask(__name__)

@app2.route('/')
def root():
    return 'Hello World!'

@app2.route('/Saludo')
def saludo():
    return 'Hola como estas bro :D!'

#Rutas Dinamicas
""" @app2.route('Saludo/<nombre>')
     def saludo_nombre(nombre):
    return 'Hola como estas ' + nombre + ' :D!' """

@app2.route('/Plantillas') 
def index(): 
    estudiantes = [{'nombre': 'Ana', 'edad': 20, 'curso': 'Matemáticas'}, 
               {'nombre': 'Carlos', 'edad': 22, 'curso': 'Historia'}, 
               {'nombre': 'Elena', 'edad': 21, 'curso': 'Biología'}, 
               {'nombre': 'Luis', 'edad': 23, 'curso': 'Ingeniería'},
               {'nombre': 'Mirsson', 'edad': 32, 'curso': 'Ingeniería'},]
    return render_template('index.html', estudiantes=estudiantes)


if __name__ == '__main__':
    app2.run(debug=True)
