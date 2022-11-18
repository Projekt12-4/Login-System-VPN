from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
import os

db_secret_key = os.environ.get("DB_SECRET_KEY");
db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = f'{db_secret_key}'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


# The new versions of flask require an app context without the "app=<app>"-create_all function parameter
def create_database(app):
    if not path.exists('/website/instance/' + DB_NAME): # originally website/DB_NAME

        print("---------------------------------\n[INFO-SERVER-STATUS]\nServer has been started\n---------------------------------")
        with app.app_context():
            db.create_all()
    