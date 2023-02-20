from apps.app import db
from apps.section10.forms import AddForm, AddOwnerForm, DelForm
from apps.section10.models import Owner, Puppy, Toy
from flask import Blueprint, redirect, render_template, url_for

section10 = Blueprint(
    "section10",
    __name__,
    template_folder="templates/section10",
    static_folder="static",
)


@section10.route("/")
def index():
    return render_template('home.html')


@section10.route("/add", methods=['GET', 'POST'])
def add_pup():

    form = AddForm()

    if form.validate_on_submit():

        name = form.name.data
        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for("section10.list_pup"))

    return render_template("add.html", form=form)


@section10.route("/list")
def list_pup():

    puppies = Puppy.query.all()
    return render_template("list.html", puppies=puppies)


@section10.route("/delete", methods=["GET", "POST"])
def del_pup():

    form = DelForm()

    if form.validate_on_submit():

        id = form.id.data
        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for("section10.list_pup"))
    return render_template("delete.html", form=form)


@section10.route("/add_owner", methods=["GET", "POST"])
def add_owner():

    form = AddOwnerForm()

    if form.validate_on_submit():

        name = form.name.data
        pup_id = form.pup_id.data
        new_owner = Owner(name, pup_id)
        db.session.add(new_owner)
        db.session.commit()

        return redirect(url_for("section10.list_pup"))

    return render_template("add_owner.html", form=form)


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


@section10.route("/relation")
def relation():
    rufus = Puppy('Rufus', 3, 'Lab')
    fido = Puppy('Fido', 1, 'Lab')

    # ADD PUPPIES TO DB
    db.session.add_all([rufus, fido])
    db.session.commit()

    # Check!
    print(Puppy.query.all())
    print("\n")

    # rufus = Puppy.query.filter_by(name='Rufus').all()[0]
    rufus = Puppy.query.filter_by(name='Rufus').first()

    # Create Owner Object
    jose = Owner('Jose', rufus.id)

    # Give Rufus some toys
    toy1 = Toy('Chew Toy', rufus.id)
    toy2 = Toy('Ball', rufus.id)

    db.session.add_all([jose, toy1, toy2])
    db.session.commit()

    # Grab Rufus after those additions!
    rufus = Puppy.query.filter_by(name='Rufus').first()
    print(rufus)
    print(rufus.report_toys())
    print("\n")

    return "Practice SQLAlchemy: Please confirm console"
