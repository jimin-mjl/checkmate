from flask import current_app
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from config import DB_CONNECT

# current_app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://elice:miniproject2@localhost:3306/elice"
current_app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql://{DB_CONNECT['username']}:{DB_CONNECT['password']}@{DB_CONNECT['server']}:3306/{DB_CONNECT['dbname']}"
current_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(current_app)

class User(UserMixin, db.Model):
      id = db.Column(db.Integer, primary_key=True)
      username = db.Column(db.String(15), unique=True, nullable=False)
      email = db.Column(db.String(50), unique=True, nullable=False)
      password = db.Column(db.String(80), nullable=False)
      institute = db.Column(db.String(45), nullable=True)

# class Group(db.Model):
#       id = db.Column(db.Integer, primary_key=True)
#       username = db.Column(db.String(15), unique=True, nullable=False)
#       institute = db.Column(db.String(45), nullable=True)

# class TodoList(db.Model):
#       id = db.Column(db.Integer, primary_key=True)
#       title = db.Column(db.String(45), nullable=False)
#       content = 
#       due = 
#       status = db.Column(db.String(45), nullable=True)

# class Comment(db.Model):
#       id = db.Column(db.Integer, primary_key=True)

# class Member(db.Model):
#       role = db.Column(db.String(45), nullable=False)

def init_db():
    db.create_all()
    db.session.commit()