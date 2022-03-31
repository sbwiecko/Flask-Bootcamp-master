from flask import Flask
# pip install flask-restful
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app) # wrapper around the app allow Resource to connect

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'} # JSON


# connect the resource to an actual URL extension
api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
