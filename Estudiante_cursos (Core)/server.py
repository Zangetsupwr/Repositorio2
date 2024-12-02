from flask_app import app
from flask_app.controllers import curso_controller
from flask_app.models.estudiantes import estudiantes

if __name__ == '__main__':
    app.run(debug=True)