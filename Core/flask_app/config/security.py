from functools import wraps

from flask import redirect, session


def session_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'usuarios' not in session:
            return redirect('/')
        return f(*args, **kwargs)
    return decorated_function
