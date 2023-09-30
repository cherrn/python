import os


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///blog.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_BINDS = {'users': 'sqlite:///user.db'}
    PASSWORD_TO_ADD_NEWS = os.getenv('PASSWORD_TO_ADD_NEWS')
