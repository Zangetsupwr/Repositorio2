from dataclasses import InitVar, dataclass
from typing import ClassVar

from flask import redirect, request, session
from flask_app import app
from flask_app.controllers import default_controller as DC
from flask_app.models.usuarios import Usuario

from flask_app.config.security import session_required


@dataclass(init=False)
class UsuarioCreate(DC.ModelCreate):

    on_error_redirect: ClassVar[str] = 'usuarios/registro'

    def post(self):
        # validaciones de los datos
        print(request.form)
        if not Usuario.validate(request.form):
            # si no pasa la validacion redirigir a la ruta de error
            return redirect(f"{self.on_error_redirect}")
        response = super().post()
        print(self.new_item)
        session['usuario'] = self.new_item
        return response


@dataclass(init=False)
class UsuarioEdit(DC.ModelEdit):

    def get(self, id):
        return super().get(id)

    def post(self, id):
        return super().post(id)


# RUTA PARA REGISTRAR UN USUARIO
app.add_url_rule(
    '/usuarios/registro',
    view_func=UsuarioCreate.as_view(
        'registro',
        model=Usuario,  #acá estaba el error Mi
        template_folder='usuarios',
        on_create_redirect='/usuarios/registro'
    )
)

