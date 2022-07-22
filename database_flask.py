#database SQL flask app

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


basedir = os.path.abspath(os.path.dirname(__file__)) #__file__ -> databse_flask.py

app = Flask(__name__)

#sets up database location
app.config['SQLALCHEMY_DATA_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

############################################
class Puppy(db.Model):

   #manually make table name 
    __tablename__ = 'puppies'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)

    def __int__(self,name,age):
        self.name = name
        self.age = age

    #give string rep    
    def __repr__(self):
        return f'Puppy {self.name} is {self.age} years old'
