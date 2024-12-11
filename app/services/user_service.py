from app.models.user import User
from app.extensions import db

def get_all_users():
    return User.query.all()

def create_user(data):
    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return user

def login_user(data):
    if data.get('username') == "admin" and data.get('password') == "password":
        return True
    return False