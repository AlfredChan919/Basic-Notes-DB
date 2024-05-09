from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

from flask_login import LoginManager

db=SQLAlchemy()

DB_NAME="database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'evwvav wefwef'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # my sqlalchemy DB is stored/located at this location.
    # stores it in the website folder, just telling flask where this is located

    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    # if i did prefix as /auth, then everyfile will go frmo /auth/smt

    from .models import User,Note

    with app.app_context():
        db.create_all()
    # create_database(app)

    login_manager=LoginManager()
    login_manager.login_view = 'auth.login'
    # tells which app login manager is using
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        # telling flaks how to look for a user similar to user query get filter
        return User.query.get(int(id))

    return app

# def create_database(app):
#     if not path.exists('website/' + DB_NAME):
#         db.create_all(app=app)
#         db.create_all()
#         print('Created Database!')