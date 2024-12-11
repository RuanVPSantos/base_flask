from flask import Blueprint, jsonify, request
from app.services.user_service import get_all_users, create_user, login_user
from app.schemas.user_schema import user_schema, users_schema
from app.middlewares.auth_middleware import jwt_required_middleware
from app.utils.jwt_helpers import get_current_user
from flask_jwt_extended import create_access_token

user_bp = Blueprint('v1_user', __name__)

@user_bp.route('/', methods=['GET'])
def list_users():
    users = get_all_users()
    return jsonify(users_schema.dump(users))

@user_bp.route('/', methods=['POST'])
def add_user():
    try:
        data = request.get_json()
        if not data.get("email") or not data.get("password") or not data.get("username"):
            return jsonify({"error": "Missing email, password or username"}), 400
        user = create_user(data)
        return jsonify(user_schema.dump(user)), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@user_bp.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json()
        if not data.get("email") or not data.get("password"):
            return jsonify({"error": "Missing email or password"}), 400
        user = login_user(data)
        if user:
            return jsonify(access_token=create_access_token(user['email'])), 200
        return jsonify({"error": "Invalid email or password"}), 401
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@user_bp.route('/profile', methods=['GET'])
@jwt_required_middleware()
def get_profile():
    try:
        current_user = get_current_user()
        if not current_user:
            return jsonify({"error": "User not found"}), 404
        return jsonify({"message": "Access granted to profile.", "user" : current_user}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

