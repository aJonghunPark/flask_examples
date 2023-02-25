from apps.app import db, login_manager
from apps.section12.forms import LoginForm, RegistrationForm
from apps.section12.models import User
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_bcrypt import Bcrypt
from flask_login import login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

login_manager.login_view = "section12.login"

section12 = Blueprint(
    "section12",
    __name__,
    template_folder="templates",
    static_folder="static",
)


@section12.route("/")
def home():
    return render_template("section12/home.html")


@section12.route("/welcome")
@login_required
def welcome_user():
    return render_template("section12/welcome_user.html")


@section12.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You logged out!")

    return redirect(url_for("section12.home"))


@section12.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash("Logged in Successfully!")

            next = request.args.get("next")

            if next is None or not next[0] == "/":
                next = url_for("section12.welcome_user")

            return redirect(next)

    return render_template("section12/login.html", form=form)


@section12.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(
            email=form.email.data,
            username=form.username.data,
            password=form.password.data,
        )
        db.session.add(user)
        db.session.commit()
        flash("Thanks for registeration!")
        return redirect(url_for("section12.login"))

    return render_template("section12/register.html", form=form)


@section12.route("/bcrypt")
def using_bcrypt():
    bcrypt = Bcrypt()

    hashed_pass = bcrypt.generate_password_hash("mypassword")
    print(f"hashed_pass={hashed_pass}")
    wrong_check = bcrypt.check_password_hash(hashed_pass, "wrongpass")
    print(f"wrong_check={wrong_check}")
    right_check = bcrypt.check_password_hash(hashed_pass, "mypassword")
    print(f"right_check={right_check}")

    return "Using Bcrypt: Please confirm console"


@section12.route("/werkzeug")
def using_werkzeug():
    hashed_pass = generate_password_hash("mypassword")
    print(hashed_pass)
    wrong_check = check_password_hash(hashed_pass, "wrongpassword")
    print(wrong_check)
    right_check = check_password_hash(hashed_pass, "mypassword")
    print(right_check)

    return "Using werkzeug: Please confirm console"
