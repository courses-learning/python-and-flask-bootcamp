from flask import Flask
from flask_restful import Resource, Api
from secure_check import authenticate, identity
from flask_jwt import JWT, jwt_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

api = Api(app)
jwt = JWT(app, authenticate, identity)

people = []


class Name(Resource):

    def get(self, name):
        for person in people:
            if person['name'] == name:
                return person

        return {'name': None}, 404

    def post(self, name):
        person = {'name': name}
        people.append(person)
        return person

    def delete(self, name):
        for ind, person in enumerate(people):
            if person['name'] == name:
                deleted_person = people.pop(ind)
                return {'note': 'delete success'}


class AllNames(Resource):

    # Added decorator menans fuction requires authentication to use
    @jwt_required()
    def get(self):
        return {'people': people}


api.add_resource(Name, '/person/<string:name>')
api.add_resource(AllNames, '/people')

if __name__ == '__main__':
    app.run(debug=True)
