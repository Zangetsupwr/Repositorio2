from flask_app import app
from flask_app.controllers import root_controller,publicaciones_controller


if __name__ == '__main__':
  app.run(debug=True)