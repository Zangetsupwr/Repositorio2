from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.viajes import Viajes

@app.route('/viajes/nuevo')
def nuevo_viaje():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('viajes/nuevo.html')

@app.route('/viajes/create', methods=['POST'])
def create_viaje():
    if 'user_id' not in session:
        return redirect('/')
        
    try:
        data = {
            'destino': request.form['destino'],
            'fecha_inicio': request.form['fecha_inicio'],
            'fecha_fin': request.form['fecha_fin'],
            'itinerario': request.form['itinerario'],
            'usuario_id': session['user_id']
        }
        
        if len(data['destino']) < 1:
            flash('El destino es requerido')
            return redirect('/viajes/nuevo')
            
        if data['fecha_inicio'] > data['fecha_fin']:
            flash('La fecha de inicio debe ser anterior a la fecha de fin')
            return redirect('/viajes/nuevo')
        
        Viajes.save(data)
        return redirect('/dashboard')
        
    except Exception as e:
        print("Error al crear viaje:", e)
        flash('Error al crear el viaje')
        return redirect('/viajes/nuevo')

@app.route('/viajes/editar/<int:id>')
def editar_viaje(id):
    if 'user_id' not in session:
        return redirect('/')
    
    try:
        # Obtener el viaje
        data = {'id': id}
        viaje = Viajes.get_by_id(data)
        
        # Verificar si el viaje existe
        if not viaje:
            flash('Viaje no encontrado')
            return redirect('/dashboard')
            
        # Verificar si el usuario es el propietario
        if viaje['usuario_id'] != session['user_id']:
            flash('No tienes permiso para editar este viaje')
            return redirect('/dashboard')
            
        return render_template('viajes/editar.html', viaje=viaje)
        
    except Exception as e:
        print("Error al editar viaje:", e)
        flash('Error al cargar el viaje')
        return redirect('/dashboard')

@app.route('/viajes/actualizar/<int:id>', methods=['POST'])
def actualizar_viaje(id):
    if 'user_id' not in session:
        return redirect('/')
        
    try:
        data = {
            'id': id,
            'destino': request.form['destino'],
            'fecha_inicio': request.form['fecha_inicio'],
            'fecha_fin': request.form['fecha_fin'],
            'itinerario': request.form['itinerario'],
            'usuario_id': session['user_id']
        }
        
        if len(data['destino']) < 1:
            flash('El destino es requerido')
            return redirect(f'/viajes/editar/{id}')
            
        if data['fecha_inicio'] > data['fecha_fin']:
            flash('La fecha de inicio debe ser anterior a la fecha de fin')
            return redirect(f'/viajes/editar/{id}')
        
        Viajes.update(data)
        return redirect('/dashboard')
        
    except Exception as e:
        print("Error al actualizar viaje:", e)
        flash('Error al actualizar el viaje')
        return redirect(f'/viajes/editar/{id}')

@app.route('/viajes/eliminar/<int:id>')
def eliminar_viaje(id):
    if 'user_id' not in session:
        return redirect('/')
        
    try:
        data = {
            'id': id,
            'usuario_id': session['user_id']
        }
        Viajes.delete(data)
        return redirect('/dashboard')
        
    except Exception as e:
        print("Error al eliminar viaje:", e)
        flash('Error al eliminar el viaje')
        return redirect('/dashboard')

@app.route('/viajes/ver/<int:id>')
def ver_viaje(id):
    if 'user_id' not in session:
        return redirect('/')
        
    try:
        data = {
            'id': id,
            'usuario_id': session['user_id']
        }
        viaje = Viajes.get_by_id(data)
        viajeros = Viajes.get_viajeros(id)
        is_viajero = Viajes.is_viajero({
            'viaje_id': id,
            'usuario_id': session['user_id']
        })
        
        return render_template('viajes/ver.html', 
                             viaje=viaje, 
                             viajeros=viajeros,
                             is_viajero=is_viajero)
        
    except Exception as e:
        print("Error al ver viaje:", e)
        flash('Error al cargar el viaje')
        return redirect('/dashboard')

@app.route('/viajes/unirse/<int:id>')
def unirse_viaje(id):
    if 'user_id' not in session:
        return redirect('/')
        
    try:
        data = {
            'viaje_id': id,
            'usuario_id': session['user_id']
        }
        Viajes.unirse_viaje(data)
        return redirect(f'/viajes/ver/{id}')
        
    except Exception as e:
        print("Error al unirse al viaje:", e)
        flash('Error al unirse al viaje')
        return redirect(f'/viajes/ver/{id}')

@app.route('/viajes/cancelar/<int:id>')
def cancelar_viaje(id):
    if 'user_id' not in session:
        return redirect('/')
        
    try:
        data = {
            'viaje_id': id,
            'usuario_id': session['user_id']
        }
        Viajes.cancelar_viaje(data)
        return redirect(f'/viajes/ver/{id}')
        
    except Exception as e:
        print("Error al cancelar viaje:", e)
        flash('Error al cancelar el viaje')
        return redirect(f'/viajes/ver/{id}')