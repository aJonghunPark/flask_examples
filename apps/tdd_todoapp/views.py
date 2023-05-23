from flask import Blueprint, render_template

tdd_todoapp = Blueprint("tdd_todoapp", __name__, template_folder="templates")


@tdd_todoapp.route("/")
def index():
    return "<h1>hello world</h1>"
