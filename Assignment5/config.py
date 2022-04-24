from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)

app.config['SECRET_KEY']='thisisfirstflaskapp'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database/crypto.db'
db=SQLAlchemy(app)