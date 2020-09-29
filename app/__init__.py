from flask import Flask 
from config import Config
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
<<<<<<< HEAD
from flask_login import LoginManager


=======
from flask_mail import Mail
>>>>>>> intialised log manager

db = SQLAlchemy()
bootstap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
mail = Mail()

<<<<<<< HEAD
login_manager = LoginManager()

def create_app(config_name):
    '''
    This function loads the correct configurations from config.py and instance/config.py
    also it creates a db object
    '''
    app = Flask(__name__, instance_relative_config=True)
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    # app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)


    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    # login_manager.login_view = "auth.login"

    
    # Register Home Blueprint
    from app import models
    
    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')  ##dashboard

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)




        
    return app
=======

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    from .auth import auth as authentication_blueprint
>>>>>>> intialised log manager

    app.register_blueprint(authentication_blueprint)

    login_manager.init_app(app)
    db.init_app(app)
    bootstap.init_app(app)
    mail.init_app(app)
    
    return app

    