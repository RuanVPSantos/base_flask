import os
from flask import Flask
from app.extensions import db, migrate, ma, jwt
from app.routers.v1 import user_routes as v1_user_routes, product_routes as v1_product_routes
# from app.routers.v2 import user_routes as v2_user_routes, product_routes as v2_product_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    # Inicializar extensões
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    jwt.init_app(app)

    # Registrar blueprints (v1 e v2)
    app.register_blueprint(v1_user_routes.user_bp, url_prefix='/api/v1/users')
    app.register_blueprint(v1_product_routes.product_bp, url_prefix='/api/v1/products')
    # app.register_blueprint(v2_user_routes.user_bp, url_prefix='/api/v2/users')
    # app.register_blueprint(v2_product_routes.product_bp, url_prefix='/api/v2/products')
    
    with app.app_context():
        if os.getenv("AUTO_CREATE_TABLES", "false").lower() == "true":
            db.create_all()

    return app
