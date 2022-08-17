from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))



db = SQLAlchemy()

def create_app(test_config=None):
    app = Flask(__name__)

    # app.config.from_mapping(
    #     SECRET_KEY='dev',
    #     DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    #     SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3'),
    #     SQLALCHEMY_TRACK_MODIFICATIONS=False
    # )

    app.config['SECRET_KEY'] = 'a3410e5f349e760123db6e01649311f9dc6866a3cb320081bc08bb0ed48f22cc2cc076f98da263b21bc87206b6408d5ed5a0'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    login_manager = LoginManager()

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .auth import auth as auth_bluprint
    app.register_blueprint(auth_bluprint)

    from .main import main as main_bluprint
    app.register_blueprint(main_bluprint)

    return app

