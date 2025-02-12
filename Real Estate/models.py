from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(100), unique = True, nullable = False)
    password = db.Column(db.String(100),nullable = False)
    access_code = db.Column(db.String(10),unique = True, nullable = False)


class Property(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(200), nullable = False)
    price = db.Column(db.Float, nullable = False)
    description = db.Column(db.Text, nullable=False)