# from os import environ, path
# from pathlib import Path

import stripe
# from dotenv import load_dotenv
from flask import (Blueprint, current_app, redirect, render_template, request,
                   url_for)

section16 = Blueprint(
    "section16", __name__, template_folder="templates", static_folder="static"
)

# basedir = Path(__file__).parent.parent.parent
# load_dotenv(path.join(basedir, ".env"))
#
# public_key = environ.get("STRIPE_PUBLISHABLE_KEY")
# stripe.api_key = environ.get("STRIPE_SECRET_KEY")


@section16.route("/")
def index():
    # https://msiz07-flask-docs-ja.readthedocs.io/ja/latest/patterns/appfactories.html
    public_key = current_app.config["PUBLIC_KEY"]
    stripe.api_key = current_app.config["SECRET_KEY"]
    return render_template("section16/index.html", public_key=public_key)


@section16.route("/thankyou")
def thankyou():
    return render_template("section16/thankyou.html")


@section16.route("/payment", methods=["POST"])
def payment():
    # CUSTOMER INFO
    customer = stripe.Customer.create(
        email=request.form["stripeEmail"], source=request.form["stripeToken"]
    )

    # PAYMENT INFO
    charge = stripe.Charge.create(
        customer=customer.id, amount=1999, currency="usd", description="Donation"
    )

    return redirect(url_for("section16.thankyou"))
