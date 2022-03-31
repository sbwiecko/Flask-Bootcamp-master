from flask import Flask, request
from flask_restful import Resource, Api
from secure_check import authenticate, identity
# pip install flask-jwt
from flask_jwt import JWT, jwt_required


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
api = Api(app)

jwt = JWT(app, authenticate, identity)
# will create an address at http://127.0.0.1:5000/auth
# then it will be possible to POST the name:pass in the headers as follows:
# Content-Type | application/json
# and in the body, as `raw` add the json as follows:
# {"username": "Jose", "password": "mypassword"}
# and finally grab the access token provided, to GET the request
# by adding it in the headers as `Authorization` using the format
# JWT eyfrjigiUHUASjfeiofjoefoekofe.f8889898
# with a space between the token and JWT, and no quotes

# see documentation at https://pythonhosted.org/Flask-JWT/

# Later on this will be a model call to our database!
# Right now its just a list of dictionaries
# puppies = [{'name':'Rufus'},{name:'Frankie'},......]
# Keep in mind, its in memory, it clears with every restart!


puppies = []

class PuppyNames(Resource):
    def get(self, name):
        print(puppies)
        for pup in puppies:
            if pup['name'] == name:
                return pup
        # If you request a puppy not yet in the puppies list
        return {'name': None}, 404

    def post(self, name):
        pup = {'name': name}
        puppies.append(pup)
        # Then return it back
        print(puppies)
        return pup

    def delete(self, name):
        for ind, pup in enumerate(puppies):
            if pup['name'] == name:
                # don't really need to save this
                delted_pup = puppies.pop(ind)
                return {'note': 'delete successful'}


class AllNames(Resource):
    @jwt_required() # adding authentication to any function we want!
    def get(self):
        # return all the puppies :)
        return {'puppies': puppies}


api.add_resource(PuppyNames, '/puppy/<string:name>')
api.add_resource(AllNames,'/puppies')

if __name__ == '__main__':
    app.run(debug=True)