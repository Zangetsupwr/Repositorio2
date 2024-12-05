from flask import render_template
from flask_app import app


@app.route('/')
def index():
    return render_template('person.html')

@app.route('/login')
def login_page():
    return render_template('login.html')