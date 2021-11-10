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

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.hashed_pass = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.hashed_pass, password)

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    def __repr__(self):
        return f'User {self.username}'


class Post(db.Model):  # post table
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.Text)
    cat_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_post(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Post {self.title}'


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Comment {self.content}'

