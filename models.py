from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

import datetime

def connect_db(app):
    db.app = app
    db.init_app(app)



class User(db.Model):
    
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    image_url = db.Column(db.String(50))

    posts = db.relationship('Post')

class Post(db.Model):

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(40), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User')
    post_tag = db.relationship('PostTag')

    tags = db.relationship('Tag', secondary='posttags')

class PostTag(db.Model):

    __tablename__ = 'posttags'

    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), primary_key=True, nullable=False)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True, nullable=False)

    posts = db.relationship('Post')
    tags = db.relationship('Tag')

class Tag(db.Model):

    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False, unique=True)

    post_tag = db.relationship('PostTag')
    
    posts = db.relationship('Post', secondary='posttags')
    





