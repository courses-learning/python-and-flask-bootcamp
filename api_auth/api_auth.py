from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from secure_check import authenticate, identity
from flask_jwt import JWT, jwt_required
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app, db)

api = Api(app)
jwt = JWT(app, authenticate, identity)


class Person(db.Model):
    name = db.Column(db.String(80), primary_key=True)

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name}


class Name(Resource):

    def get(self, name):
        person = Person.query.filter_by(name=name).first()
        if person:
            return person.json()
        else:
            return {'name': None}, 404

    def post(self, name):
        person = Person(name=name)
        db.session.add(person)
        db.session.commit()
        return person.json()

    def delete(self, name):
        person = Person.query.filter_by(name=name).first()
        db.session.delete(person)
        db.session.commit()
        return {'note': 'delete success'}


class AllNames(Resource):

    # Added decorator menans fuction requires authentication to use
    @jwt_required()
    def get(self):
        people = Person.query.all()

        return [person.json() for person in people]


api.add_resource(Name, '/person/<string:name>')
api.add_resource(AllNames, '/people')

if __name__ == '__main__':
    app.run(debug=True)
