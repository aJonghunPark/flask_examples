from apps.app import db
from apps.section10.models import Puppy
from flask import Blueprint, render_template

section10 = Blueprint(
    "section10",
    __name__,
    template_folder="templates",
    static_folder="static",
)


@section10.route("/sql")
def sql():
    # CREATE
    my_puppy = Puppy('Rufus', 5)
    db.session.add(my_puppy)
    db.session.commit()

    # READ
    all_puppies = Puppy.query.all()
    print(all_puppies)
    print("\n")

    # Grab by id
    puppy_one = Puppy.query.get(1)
    print(puppy_one)
    print(puppy_one.age)
    print("\n")

    # Filters
    puppy_olia = Puppy.query.filter_by(name="Olia")
    print(puppy_olia)
    print("\n")

    # UPDATE
    first_puppy = Puppy.query.get(1)
    first_puppy.age = 10
    db.session.add(first_puppy)
    db.session.commit()
    print(first_puppy)
    print("\n")

    # DELETE
    Puppy.query.filter_by(name="Rufus").delete()
    db.session.commit()

    # Check for changes:
    all_puppies = Puppy.query.all()
    print(all_puppies)
    print("\n")

    return "Practice SQLAlchemy: Please confirm console"
