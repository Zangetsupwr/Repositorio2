
from functools import wraps

from flask import redirect, session


def session_required(redirect_to_url="/"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if 'user_id' not in session:
                return redirect(redirect_to_url)
            return func(*args, **kwargs)
        return wrapper
    return decorator