from flask_jwt_extended import get_jwt_identity
from flask import jsonify

def get_current_user():
    """
    Recupera a identidade do usuário a partir do token JWT.
    """
    user_identity = get_jwt_identity()
    if not user_identity:
        return jsonify({"error": "No user identity found in token"}), 401
    return user_identity
