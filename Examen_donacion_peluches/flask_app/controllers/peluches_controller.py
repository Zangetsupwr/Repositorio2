from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.peluche import Peluche

@app.route('/peluches/nuevo')
def nuevo_peluche():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('peluches/nuevo.html')

@app.route('/peluches/create', methods=['POST'])
def create_peluche():
    if 'user_id' not in session:
        return redirect('/')
        
    try:
        # Debug: imprimir todos los datos
        print("Formulario completo:", request.form)
        print("Usuario en sesión:", session['user_id'])
        
        # Verificar que todos los campos requeridos estén presentes
        required_fields = ['nombre', 'descripcion', 'estado']
        for field in required_fields:
            if field not in request.form or not request.form[field].strip():
                flash(f'El campo {field} es requerido')
                print(f"Falta el campo: {field}")
                return redirect('/peluches/nuevo')
        
        # Preparar datos para la base de datos
        data = {
            'nombre': request.form['nombre'].strip(),
            'descripcion': request.form['descripcion'].strip(),
            'estado': request.form['estado'],
            'usuario_id': session['user_id']
        }
        
        # Debug: imprimir data procesada
        print("Data a insertar:", data)
        
        # Intentar guardar
        peluche_id = Peluche.save(data)
        
        # Debug: imprimir resultado
        print("Resultado de save:", peluche_id)
        
        if not peluche_id:
            flash('Error al guardar el peluche')
            return redirect('/peluches/nuevo')
            
        flash('¡Peluche donado exitosamente!', 'success')
        return redirect('/dashboard')
        
    except Exception as e:
        print("Error al crear peluche:", str(e))
        flash('Error al crear el peluche')
        return redirect('/peluches/nuevo')

@app.route('/peluches/editar/<int:id>')
def editar_peluche(id):
    if 'user_id' not in session:
        return redirect('/')
        
    try:
        print(f"Intentando editar peluche {id}")
        peluche = Peluche.get_by_id({'id': id})
        
        if not peluche:
            print("Peluche no encontrado")
            flash('Peluche no encontrado')
            return redirect('/dashboard')
            
        if peluche['usuario_id'] != session['user_id']:
            print("Usuario no autorizado")
            flash('No tienes permiso para editar este peluche')
            return redirect('/dashboard')
            
        return render_template('peluches/editar.html', peluche=peluche)
        
    except Exception as e:
        print("Error al cargar edición:", str(e))
        flash('Error al cargar el peluche')
        return redirect('/dashboard')

@app.route('/peluches/actualizar/<int:id>', methods=['POST'])
def actualizar_peluche(id):
    if 'user_id' not in session:
        return redirect('/')
        
    try:
        # Debug: imprimir todos los datos recibidos
        print("Formulario completo:", request.form)
        print("ID del peluche:", id)
        print("Usuario en sesión:", session['user_id'])
        
        # Verificar propiedad del peluche
        peluche = Peluche.get_by_id({'id': id})
        if not peluche or peluche['usuario_id'] != session['user_id']:
            flash('No tienes permiso para editar este peluche')
            return redirect('/dashboard')
        
        # Validar que todos los campos estén presentes
        if not all(field in request.form and request.form[field].strip() 
                  for field in ['nombre', 'descripcion', 'estado']):
            flash('Todos los campos son requeridos')
            return redirect(f'/peluches/editar/{id}')
        
        # Preparar datos para actualización
        data = {
            'id': id,
            'nombre': request.form['nombre'].strip(),
            'descripcion': request.form['descripcion'].strip(),
            'estado': request.form['estado'],
            'usuario_id': session['user_id']
        }
        
        # Debug: imprimir data procesada
        print("Datos a actualizar:", data)
        
        # Intentar actualizar
        resultado = Peluche.update(data)
        print("Resultado de la actualización:", resultado)
        
        if resultado:
            flash('Peluche actualizado exitosamente')
            return redirect('/dashboard')
        else:
            flash('Error al actualizar el peluche')
            return redirect(f'/peluches/editar/{id}')
            
    except Exception as e:
        print("Error al actualizar:", str(e))
        import traceback
        print(traceback.format_exc())
        flash('Error al actualizar el peluche')
        return redirect(f'/peluches/editar/{id}')

@app.route('/peluches/eliminar/<int:id>')
def eliminar_peluche(id):
    if 'user_id' not in session:
        return redirect('/')
        
    try:
        data = {
            'id': id,
            'usuario_id': session['user_id']
        }
        Peluche.delete(data)
        return redirect('/dashboard')
        
    except Exception as e:
        print("Error al eliminar viaje:", e)
        flash('Error al eliminar el viaje')
        return redirect('/dashboard')

@app.route('/peluches/ver/<int:id>')
def ver_peluche(id):
    if 'user_id' not in session:
        print("No hay usuario en sesión")
        return redirect('/')
        
    try:
        print(f"Intentando ver peluche {id} por usuario {session['user_id']}")
        
        # Obtener el peluche primero
        peluche = Peluche.get_by_id({'id': id})
        
        if not peluche:
            print("Peluche no encontrado")
            flash('Peluche no encontrado')
            return redirect('/dashboard')
            
        print("Peluche encontrado:", peluche)
        
        # Incrementar contador solo si el visitante no es el dueño
        if peluche['usuario_id'] != session['user_id']:
            print("Incrementando visitas")
            Peluche.incrementar_visitas(id, session['user_id'])
            # Recargar el peluche para obtener el contador actualizado
            peluche = Peluche.get_by_id({'id': id})
        else:
            print("El usuario es el dueño, no se incrementan visitas")
            
        return render_template('peluches/ver.html', peluche=peluche)
        
    except Exception as e:
        print("Error al ver peluche:", str(e))
        import traceback
        print(traceback.format_exc())
        flash('Error al cargar el peluche')
        return redirect('/dashboard')

@app.route('/adoptar/<int:id>')
def adoptar_peluche(id):
    if 'user_id' not in session:
        return redirect('/')
        
    try:
        # Debug: imprimir información
        print(f"Intentando adoptar peluche {id} por usuario {session['user_id']}")
        
        # Verificar que el peluche existe y no está adoptado
        peluche = Peluche.get_by_id({'id': id})
        
        if not peluche:
            print("Peluche no encontrado")
            flash('Peluche no encontrado')
            return redirect('/dashboard')
            
        # Verificar que no es el dueño
        if peluche['usuario_id'] == session['user_id']:
            print("Usuario intenta adoptar su propio peluche")
            flash('No puedes adoptar tu propio peluche')
            return redirect('/dashboard')
            
        # Verificar que no está adoptado
        if Peluche.esta_adoptado(id):
            print("Peluche ya está adoptado")
            flash('Este peluche ya ha sido adoptado')
            return redirect('/dashboard')
            
        # Intentar adoptar
        resultado = Peluche.adoptar(id, session['user_id'])
        
        if resultado:
            print("Adopción exitosa")
            flash('¡Has adoptado el peluche exitosamente!', 'success')
        else:
            print("Error en la adopción")
            flash('No se pudo completar la adopción')
            
        return redirect('/dashboard')
        
    except Exception as e:
        print("Error al adoptar:", str(e))
        import traceback
        print(traceback.format_exc())
        flash('Error al procesar la adopción')
        return redirect('/dashboard')
    
