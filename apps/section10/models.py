from apps.app import db


class Puppy(db.Model):

    # MANUAL TABLE NAME CHOICE!
    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    age = db.Column(db.Integer)
    breed = db.Column(db.String(120))

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __repr__(self):
        return f"Puppy {self.name} is {self.age} years old"
