from flask import Blueprint, redirect, render_template, url_for
from flask_dance.contrib.google import google

oauth = Blueprint("oauth", __name__, template_folder="templates")


@oauth.route("/")
def index():
    return render_template("oauth/home.html")


@oauth.route("/welcome")
def welcome():
    # RETURN ERROR INTERNAL SERVER ERROR IF NOT LOGGED IN!
    res = google.get("/oauth2/v2/userinfo")
    assert res.ok, res.text
    email = res.json()["email"]

    return render_template("oauth/welcome.html", email=email)


@oauth.route("/login/google")
def login():
    if not google.authorized:
        return redirect(url_for("google.login"))
    res = google.get("/oauth2/v2/userinfo")
    # res = google.get("/plus/v1/people/me")
    assert res.ok, res.text
    email = res.json()["email"]

    return render_template("oauth/welcome.html")
