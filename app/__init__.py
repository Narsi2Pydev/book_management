from flask import Flask
from .config import Config
from .database import init_db
from routes.books import books_bp
from routes.users import users_bp
from routes.reviews import reviews_bp
from routes.auth import auth_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    init_db(app)

    app.register_blueprint(books_bp, url_prefix='/books')
    app.register_blueprint(users_bp, url_prefix='/users')
    app.register_blueprint(reviews_bp, url_prefix='/reviews')
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app
