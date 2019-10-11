from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, DateTime, Text, ForeignKey
from datetime import datetime


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]= 'sqlite:///site.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

from creator import routes