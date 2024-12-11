from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request

def jwt_required_middleware():
    """
    Middleware para verificar JWT em cada requisição autenticada.
    """
    def wrapper(fn):
        def decorated_function(*args, **kwargs):
            try:
                verify_jwt_in_request()
                return fn(*args, **kwargs)
            except Exception as e:
                return jsonify({"error": str(e)}), 401
        return decorated_function
    return wrapper
