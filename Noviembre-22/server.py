from flask_app import app

from flask_app.controllers import usuarios_controllers


# Correr el servidor
if __name__ == '__main__':
    app.run(debug=True)
