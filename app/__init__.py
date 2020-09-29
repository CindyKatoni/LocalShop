#Application's entry point
#3rd Party Imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


#local imports
from config import app_config

#Db initialization
db = SQLAlchemy()

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

    # Register Home Blueprint
    from app import models
    
    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

        
    return app

    

