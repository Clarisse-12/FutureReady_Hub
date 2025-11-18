from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime
from .extentions import db
from werkzeug.security import generate_password_hash, check_password_hash
import uuid

class User(db.Model):
    __tablename__ = 'users'
    
    userid = db.Column(db.Integer, primary_key=True,autoincrement=True)
    usertype=db.Column(db.String(50))
    email=db.Column(db.String(50))
    password=db.Column(db.String(255))
    secretkey=db.Column(db.String(255))

    def set_hashpassword(self, password):
        self.password = generate_password_hash(password)
    def check_password(self, entered_password):
        return check_password_hash(self.password, entered_password)
    


class Internship(db.Model):
    __tablename__ = 'internship'

    internship_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(150))
    provider = db.Column(db.String(100))
    location = db.Column(db.String(100))
    salary = db.Column(db.String(200))
    posted_at = db.Column(db.DateTime, default=datetime.now())
    link = db.Column(db.String(300))
  


class Training(db.Model):
    __tablename__ = 'training'

    training_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(150))
    provider = db.Column(db.String(100))
    location = db.Column(db.String(100))
    level = db.Column(db.String(100))
    paid_free = db.Column(db.String(50))
    posted_at = db.Column(db.DateTime, default=datetime.utcnow)
    link = db.Column(db.String(300))
   


class SearchHistory(db.Model):
    __tablename__ = 'search_history'

    history_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.Integer, db.ForeignKey('users.userid'))
    search_type = db.Column(db.String(50))
    keyword = db.Column(db.String(50))
    timestamb = db.Column(db.DateTime, default=datetime.utcnow)



    
