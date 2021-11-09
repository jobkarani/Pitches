from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from . import login_manager


class Category(db.Model):  # category table
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    post = db.relationship('Post', backref='category', lazy='dynamic')


    def save_cat(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Category {self.name}'



class User(UserMixin, db.Model):  
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    hashed_pass = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_image_path = db.Column(db.String())
    posts = db.relationship('Post', backref='author', lazy='dynamic')


    def save_user(self):
        db.session.add(self)
        db.session.commit()

    
    def __repr__(self):
        return f'User {self.username}'




