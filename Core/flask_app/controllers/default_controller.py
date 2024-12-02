from dataclasses import dataclass
from flask import redirect, render_template, request
from flask.views import MethodView

#UTILIZAMOS METHODVIEW PARA PODER MANEJAR DIFERENTES METODOS EN UNA SOLA CLASE

#CLASE PARA LISTAR LOS MODELOS
@dataclass
class ModelList(MethodView):
    model: object
    template_folder: str

    def get(self):
        items = self.model.all()
        return render_template(f"{self.template_folder}/view.html", items=items)

#CLASE PARA DETALLAR UN MODELO
@dataclass
class ModelDetail(MethodView):
    model: object
    template_folder: str
    #METODO GET PARA MOSTRAR LOS DETALLES DE UN MODELO
    def get(self, id):
        item = self.model.find_by_id(id)
        return render_template(f"{self.template_folder}/detail.html", item=item)

#CLASE PARA CREAR UN MODELO
@dataclass
class ModelCreate(MethodView):
    model: object
    template_folder: str
    on_create_redirect: str
    #METODO GET PARA MOSTRAR EL FORMULARIO DE CREACION
    def get(self):
        return render_template(f"{self.template_folder}/create.html")
    #METODO POST PARA GUARDAR LOS DATOS DEL FORMULARIO
    def post(self):
        new_item = self.model(request.form)
        self.new_item=self.model.save(new_item.__dict__())
        return redirect(f"{self.on_create_redirect}")
    
#CLASE PARA EDITAR UN MODELO
@dataclass
class ModelEdit(MethodView):
    model: object
    template_folder: str
    on_update_redirect: str
    #METODO GET PARA MOSTRAR EL FORMULARIO DE EDICION
    def get(self, id):
        item = self.model.find_by_id(id)
        return render_template(f"{self.template_folder}/edit.html", item=item)
    #METODO POST PARA GUARDAR LOS DATOS DEL FORMULARIO
    def post(self, id):
        updated_item = self.model(request.form)
        updated_item.id = id
        self.model.update(updated_item.__dict__())
        return redirect(f"/{self.on_update_redirect}")    
    
#CLASE PARA ELIMINAR UN MODELO
@dataclass
class ModelDelete(MethodView):
    model: object
    on_delete_redirect: str
    #METODO GET PARA MOSTRAR EL FORMULARIO DE ELIMINACION
    def get(self, id):
        self.model.delete_by_id(id)
        return redirect(f"/{self.on_delete_redirect}")
