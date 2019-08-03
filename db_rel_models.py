import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


class Animal(db.Model):

    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Text)
    name = db.Column(db.Text)
    foods = db.relationship('Food', backref='animal', lazy='dynamic')  # 1:many
    sponser = db.relationship('Sponser', backref='animal', uselist=False)  # 1:1

    def __init__(self, type, name):
        self.type = type
        self.name = name

    def __repr__(self):
        if self.sponser:
            return f'{self.name.title()} the {self.type.lower()} is sponsored by {self.sponser.name.title()}.'
        else:
            return f'{self.name.title()} the {self.type.lower()} does not yet have a sponser.'

    def report_foods(self):
        print(f'{self.name.title()} eats:')
        for food in self.foods:
            print(food.item_name)


class Food(db.Model):

    __tablename__ = 'foods'

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.Text)
    animal_id = db.Column(db.Integer, db.ForeignKey('animals.id'))

    def __init__(self, item_name, animal_id):
        self.item_name = item_name
        self.animal_id = animal_id


class Sponser(db.Model):

    __tablename__ = 'sponsers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    animal_id = db.Column(db.Integer, db.ForeignKey('animals.id'))

    def __init__(self, name, animal_id):
        self.name = name
        self.animal_id = animal_id
