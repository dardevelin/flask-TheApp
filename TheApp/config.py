import os

class DevelopmentConfig(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://username:password@localhost:port/TheAppDB"
    DEBUG = True
    SECRET_KEY = os.environ.get("TheApp_SECRET_KEY", os.urandom(12))


class TestingConfig(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://username:password@localhost:port/TheAppDB"
    DEBUG = True
    SECRET_KEY = os.environ.get("TheApp_SECRET_KEY", os.urandom(12))
