import os

class DevelopmentConfig(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://ubuntu:thinkful@localhost:5432/TheAppDB"
    DEBUG = True
    SECRET_KEY = os.environ.get("THEAPP_SECRET_KEY", os.urandom(12))

class TestingConfig(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://username:password@localhost:5432/TheAppDB"
    DEBUG = True
    SECRET_KEY = os.environ.get("THEAPP_SECRET_KEY", os.urandom(12))

class TravisConfig(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://username:password@localhost:5432/TheAppDB"
    DEBUG = True
    SECRET_KEY = os.environ.get("THEAPP_SECRET_KEY", os.urandom(12))
