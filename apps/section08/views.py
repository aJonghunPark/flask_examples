from flask import Blueprint, render_template, request

section08 = Blueprint(
    "section08",
    __name__,
    template_folder="templates",
    static_folder="static",
)


@section08.route("/")
def index():
    return render_template("section08/index.html")


@section08.route("/signup_form")
def signup_form():
    return render_template("section08/signup.html")


@section08.route("/thankyou")
def thank_you():
    first = request.args.get("first")
    last = request.args.get("last")
    return render_template("section08/thankyou.html", first=first, last=last)


@section08.route("/check")
def check():
    return render_template("section08/check.html")


@section08.route("/report")
def report():
    username = request.args.get("username")
    lower = False
    upper = False
    num_end = False

    lower = any(c.islower() for c in username)
    upper = any(c.isupper() for c in username)
    num_end = username[-1].isdigit()

    report = lower and upper and num_end

    return render_template("section08/report.html",
                           report=report,
                           lower=lower,
                           upper=upper,
                           num_end=num_end)


@section08.errorhandler(404)
def page_not_found(e):
    return render_template("section08/404.html"), 404
