from flask import Blueprint
from flask_jwt import jwt_required
from flask_restful import Api, Resource

crud = Blueprint("crud", __name__)
api = Api(crud)

puppies = []


class PuppyNames(Resource):
    def get(self, name):
        print(puppies)

        # Cycle through list for puppies
        for pup in puppies:
            if pup["name"] == name:
                return pup

        # If you request a puppy not yet in the puppies list
        return {"name": None}, 404

    def post(self, name):
        # Add the dictionary to list
        pup = {"name": name}
        puppies.append(pup)
        # Then return it back
        print(puppies)
        return pup

    def delete(self, name):
        # Cycle through list for puppies
        for index, pup in enumerate(puppies):
            if pup["name"] == name:
                # don't really need to save this
                deleted_pup = puppies.pop(index)
                return {"note": "delete successful"}


class AllNames(Resource):
    @jwt_required()
    def get(self):
        # return all the puppies :)
        return {"puppies": puppies}


api.add_resource(PuppyNames, "/puppy/<string:name>")
api.add_resource(AllNames, "/puppies")
