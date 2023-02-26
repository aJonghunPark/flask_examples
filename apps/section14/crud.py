from apps.app import db
from apps.section10.models import Puppy
from flask import Blueprint
from flask_jwt import jwt_required
from flask_restful import Api, Resource

crud = Blueprint("crud", __name__)
api = Api(crud)


class PuppyNames(Resource):
    def get(self, name):
        pup = Puppy.query.filter_by(name=name).first()

        if pup:
            return pup.json()
        else:
            return {"name": None}, 404

        return {"name": None}, 404

    def post(self, name):
        pup = Puppy(name=name)
        db.session.add(pup)
        db.session.commit()

        return pup.json()

    def delete(self, name):
        pup = Puppy.query.filter_by(name=name).first()
        db.session.delete(pup)
        db.session.commit()

        return {"note": "delete successful"}


class AllNames(Resource):
    @jwt_required()
    def get(self):
        # return all the puppies :)
        puppies = Puppy.query.all()

        return [pup.json() for pup in puppies]


api.add_resource(PuppyNames, "/puppy/<string:name>")
api.add_resource(AllNames, "/puppies")
