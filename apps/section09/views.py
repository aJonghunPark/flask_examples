from flask import Blueprint, flash, redirect, render_template, session, url_for
from flask_wtf import FlaskForm
from wtforms import (BooleanField, RadioField, SelectField, StringField,
                     SubmitField, TextAreaField)
from wtforms.validators import DataRequired

section09 = Blueprint(
    "section09",
    __name__,
    template_folder="templates",
    static_folder="static",
)


class SimpleForm(FlaskForm):

    breed = StringField("What breed are you?", validators=[DataRequired()])
    submit = SubmitField("Submit")


@section09.route("/simple", methods=["GET", "POST"])
def simple():

    form = SimpleForm()

    if form.validate_on_submit():
        flash("You just changed your breed to:")
        session['breed'] = form.breed.data

        return redirect(url_for("section09.simple"))

    return render_template("section09/simple.html", form=form)


class InfoForm(FlaskForm):
    '''
    This general class gets a lot of form about puppies.
    Mainly a way to go through many of the WTForms Fields.
    '''
    breed = StringField('What breed are you?', validators=[DataRequired()])
    neutered = BooleanField("Have you been neutered?")
    mood = RadioField("Please choose your mood:",
                      choices=[('mood_one', 'Happy'), ('mood_two', 'Excited')])
    food_choice = SelectField(u"Pick your favorite food:",
                              choices=[('chi', 'Chicken'), ('bf', 'Beef'),
                                       ('fish', 'Fish')])
    feedback = TextAreaField()
    submit = SubmitField('Submit')


@section09.route("/", methods=['GET', 'POST'])
def index():
    form = InfoForm()
    if form.validate_on_submit():
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food'] = form.food_choice.data
        session['feedback'] = form.feedback.data

        return redirect(url_for('section09.thankyou'))

    return render_template('section09/index.html', form=form)


@section09.route("/thankyou")
def thankyou():
    return render_template("section09/thankyou.html")
