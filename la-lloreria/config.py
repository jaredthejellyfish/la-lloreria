import os 

class Config():
    if os.path.exists(os.getcwd() + '/flask_pwa/config.ini'):
        import configparser
        config = configparser.ConfigParser()
        config.read(os.getcwd() + '/flask_pwa/config.ini')
        SECRET_KEY = config['SERVER']['SECRET_KEY']
        SQLALCHEMY_DATABASE_URI = config['SERVER']['DATABASE_URI']
        SQLALCHEMY_TRACK_MODIFICATIONS = False

        SSL_DISABLE = True
    else:
        SECRET_KEY = os.environ.get("SECRET_KEY")
        SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL").replace("postgres", "postgresql")
        SQLALCHEMY_TRACK_MODIFICATIONS = False