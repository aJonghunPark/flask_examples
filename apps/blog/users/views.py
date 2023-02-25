from apps.app import db
from apps.blog.models import Post
from apps.blog.users.forms import LoginForm, RegistrationForm, UpdateUserForm
from apps.blog.users.picture_handler import add_profile_pic
from apps.section12.models import User
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user

users = Blueprint("users", __name__)


# register
@users.route("/register", methods=["GET", "POST"])
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
        flash("Thanks for registration!")
        return redirect(url_for("blog.users.login"))

    return render_template("register.html", form=form)


# login
@users.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash("Log in Success!")

            next = request.args.get("next")

            if next is None or not next[0] == "/":
                next = url_for("blog.core.index")

            return redirect(next)

    return render_template("login.html", form=form)


# logout
@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("blog.core.index"))


# account (update UserForm)
@users.route("/account", methods=["GET", "POST"])
@login_required
def account():
    form = UpdateUserForm()
    if form.validate_on_submit():
        if form.picture.data:
            username = current_user.username
            pic = add_profile_pic(form.picture.data, username)
            current_user.profile_image = pic

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash("User Account Update!")
        return redirect(url_for("blog.users.account"))
    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email

    profile_image = url_for(
        "static", filename="profile_pics/" + current_user.profile_image
    )
    return render_template("account.html", profile_image=profile_image, form=form)


# user's list of Blog posts
@users.route("/<username>")
def user_posts(username):
    page = request.args.get("page", 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = (
        Post.query.filter_by(author=user)
        .order_by(Post.date.desc())
        .paginate(page=page, per_page=5)
    )
    return render_template("posts.html", posts=posts, user=user)
