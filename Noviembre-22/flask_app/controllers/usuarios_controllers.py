from dataclasses import InitVar, dataclass
from typing import ClassVar
from urllib import response
from flask import redirect, request, session
from flask_app import app
from flask_app.controllers import default_controller as DC
from flask_app.models import usuarios


@dataclass(init=False)
class UsuarioCreate(DC.ModelCreate):

    on_error_redirect: ClassVar[str]='/usuarios/register'

    def post(self):
        # validaciones de los datos
        if not self.model.validate(request.form):
            # si no pasa la validacion redirigir a la ruta de error
            return redirect(f"{self.on_error_redirect}")
        response =super().post()
        session['usuario'] = response
        return response


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
