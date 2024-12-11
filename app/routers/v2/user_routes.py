from flask import Blueprint, jsonify, request
from app.services.user_service import get_all_users, create_user
from app.schemas.user_schema import user_schema, users_schema

user_bp = Blueprint('v2_user', __name__)

@user_bp.route('/', methods=['GET'])
def list_users():
    users = get_all_users()
    return jsonify({
        "count": len(users),
        "users": users_schema.dump(users)
    })

@user_bp.route('/', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data.get("email").endswith("@example.com"):
        return jsonify({"error": "Email must be from @example.com"}), 400
    user = create_user(data)
    return jsonify(user_schema.dump(user)), 201
