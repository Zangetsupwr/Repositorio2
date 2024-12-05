from flask import jsonify, request
from flask_app import app


@app.route('/api/login', methods=['POST'])
def login():
    # LOGICA PARA EL LOGIN
    data = request.form
    print(data)

    # VALIDACION DEL LOGIN
    if data.get('password') != 'hola1234':
        return jsonify({"errors": {"password":"Wrong Password"}}), 401

    return jsonify({"status": "login ok"}), 200
