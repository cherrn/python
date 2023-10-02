from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()  # Инициализация объекта db


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(200))
    date = db.Column(db.DateTime, default=datetime.utcnow)
    language = db.Column(db.String(2), nullable=False)

    def __repr__(self):
        return '<Article %r>' % self.id


class User(db.Model):
    __tablename__ = 'users'
    __bind_key__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(400), unique=True, nullable=False)
    password = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.username}>'
