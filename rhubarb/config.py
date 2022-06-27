class Config(object):
    SECRET_KEY = '9b755692e0a99a14183d46f6ce7ef16666aab1362f7a89e16802c453128323ea'


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    debug = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///data/rhubarb.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    