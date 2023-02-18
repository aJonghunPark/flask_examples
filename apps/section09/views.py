from flask import Blueprint, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

section09 = Blueprint(
    "section09",
    __name__,
    template_folder="templates",
    static_folder="static",
)


class InfoForm(FlaskForm):
    '''
    This general class gets a lot of form about puppies.
    Mainly a way to go through many of the WTForms Fields.
    '''
    breed = StringField('What breed are you?')
    submit = SubmitField('Submit')


@section09.route("/", methods=['GET', 'POST'])
def index():
    # Set the breed to a boolean False.
    # So we can use it an if statement in the html.
    breed = False
    # Create instance of the form.
    form = InfoForm()
    # If the form is valid on submission (we'll talk about validation next)
    if form.validate_on_submit():
        # Grab the data from the breed on the form.
        breed = form.breed.data
        # Reset the form's breed data to be False.
        form.breed.data = ''

    return render_template('section09/home.html', form=form, breed=breed)
