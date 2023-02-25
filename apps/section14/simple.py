# https://rajansahu713.medium.com/hands-on-guide-to-restful-api-using-flask-python-16270f866ffe
from flask import Blueprint
from flask_restful import Api, Resource

simple = Blueprint("simple", __name__)
api = Api(simple)


class HelloWorld(Resource):
    def get(self):
        return {"hello": "world"}


api.add_resource(HelloWorld, "/")
