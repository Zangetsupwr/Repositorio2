import os
from flask import Flask ,render_template,session,redirect,url_for,request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('APP_SECRET_KEY')

@app.route('/') 
def index():
 if 'visitas' in session:
    session['visitas'] = session.get('visitas') + 1
 else:
    session['visitas'] = 0
 if 'resets' not in session:
   session['resets'] = 0
 return render_template('index.html', visitas=session['visitas'],resets=session['resets'])
 
@app.route('/destruir_sesion')
def destruir_sesion():
   session.clear()
   session.pop('visitas',None)
   session.pop('resets', None)
   return redirect('/')


@app.route('/') 
def btn_visitas(): 
   session['visitas'] += 1 
   return redirect(url_for('index'))

@app.route('/reset_visits', methods=['POST']) 
def reset_visits(): 
   session['visitas'] = -1 
   return redirect(url_for('index'))

#Agregar un formulario que permita ingresar un numero
#y que aumente esa cantidad de visitas
@app.route('/incrementar_visitas', methods=['POST'])
def incrementar_visitas():
  incremento = int(request.form.get('incremento',0))
  session['visitas'] += incremento-1
  return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)