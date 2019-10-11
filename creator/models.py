import datetime
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, DateTime, Text, ForeignKey
from creator import db

#creating classes to hold user data in the databases:
class User(db.Model):
    tablename = 'user'
    id = Column(Integer, primary_key=True)
    username =Column(String(20), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    image_file = Column(String(20), nullable=False, default='default.jpg')
    password = Column(String(60), nullable=False)
   # posts = relationship("Post", backref = 'author', lazy=True)
    



    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

#creating Post class to hold data of Posts:
class Post(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    content = Column( Text, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    
    
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
