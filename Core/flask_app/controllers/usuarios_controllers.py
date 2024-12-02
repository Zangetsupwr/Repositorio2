from dataclasses import InitVar, dataclass
from typing import ClassVar

from flask import redirect, request, session
from flask_app import app
from flask_app.controllers import default_controller as DC
from flask_app.models import usuarios

from flask_app.config.security import session_required


@dataclass(init=False)
class UsuarioCreate(DC.ModelCreate):

    on_error_redirect: ClassVar[str] = '/usuarios/register'

    def post(self):
        # validaciones de los datos
        if not self.model.validate(request.form):
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
    '/usuarios/register',
    view_func=UsuarioCreate.as_view(
        'register',
        model=usuarios.Usuarios,
        template_folder='usuarios',
        on_create_redirect='/usuarios/register'
    )
)


app.add_url_rule(
    '/usuarios/edit/<int:id>',
    view_func=session_required(DC.ModelEdit.as_view(
        'edit',
        model=usuarios.Usuarios,
        template_folder='usuarios',
        on_update_redirect='/usuarios/register'
    ))
)
