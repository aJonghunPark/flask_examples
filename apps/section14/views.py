from flask import Blueprint
from flask_restful import Api, Resource

section14 = Blueprint("section14", __name__)
api = Api(section14)


class HelloWorld(Resource):
    def get(self):
        return {"hello": "world"}


api.add_resource(HelloWorld, "/")
