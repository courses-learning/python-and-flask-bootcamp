from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

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

    def get(self):
        return {'people': people}


api.add_resource(Name, '/person/<string:name>')
api.add_resource(AllNames, '/people')

if __name__ == '__main__':
    app.run(debug=True)
