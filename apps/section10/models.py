from apps.app import db


class Puppy(db.Model):

    # MANUAL TABLE NAME CHOICE!
    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    age = db.Column(db.Integer)
    breed = db.Column(db.String(120))

    # ONE TO MANY
    # Puppy to Many Toys...
    toys = db.relationship('Toy', backref='puppy', lazy='dynamic')

    # ONE TO ONE
    # Puppy to One Owner
    owner = db.relationship('Owner', backref='puppy', uselist=False)

    def __init__(self, name, age=0, breed=''):
        self.name = name
        self.age = age
        self.breed = breed

    def __repr__(self):
        if self.owner:
            return f"Puppy name is {self.name} and owner is {self.owner.name}"
        else:
            return f"Puppy name is {self.name} and has no owner yet!"

    def report_toys(self):
        print("Here are my toys:")
        for toy in self.toys:
            print(toy.item_name)


class Toy(db.Model):

    __tablename__ = 'toys'

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(120))
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, item_name, puppy_id):
        self.item_name = item_name
        self.puppy_id = puppy_id


class Owner(db.Model):

    __tablename__ = 'owners'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id
