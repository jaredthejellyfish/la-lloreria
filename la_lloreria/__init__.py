from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
#from flask_login import LoginManager

from flask_minify import Minify

from la_lloreria.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
#login_manager = LoginManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    bcrypt.init_app(app)
    #login_manager.init_app(app)

    from la_lloreria.main.routes import main
    from la_lloreria.valorant.routes import valorant
    
    app.register_blueprint(main)
    app.register_blueprint(valorant)
    
    Minify(app=app, html=True, js=True, cssless=True)

    return app

