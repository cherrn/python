class Config:
    SECRET_KEY = "K^#%6%1KP&n?6!2N6i4TwSiS*"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///blog.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_BINDS = {'users': 'sqlite:///user.db'}
    PASSWORD_TO_ADD_NEWS = 1111
