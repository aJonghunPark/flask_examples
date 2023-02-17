from flask import Blueprint, render_template

section07 = Blueprint(
    "section07",
    __name__,
    template_folder="templates",
    static_folder="static",
)


@section07.route("/")
def index():
    return render_template("home.html")


@section07.route("/information")
def information():
    return "<h1>Puppies are cute!</h1>"


@section07.route("/puppy/<name>")
def puppy(name):
    return render_template("puppy.html", name=name)


@section07.route("/puppy_latin/<name>")
def puppy_latin(name):
    latin_name = ""
    if name[-1] == 'y':
        latin_name = name[:-1] + 'iful'
    else:
        latin_name = name + 'y'

    return "<h1>Hi! Your puppy latin name is {}.</h1>".format(latin_name)
