from flask import render_template
from flask_app import app


@app.route('/')
def index():
    return render_template('Github_API/index.html')
