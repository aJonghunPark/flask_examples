from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate
from flask_seeder import FlaskSeeder
from flask_sqlalchemy import SQLAlchemy

from apps.config import config

db = SQLAlchemy()


def create_app(config_key):

    app = Flask(__name__)
    app.config.from_object(config[config_key])

    db.init_app(app)
    Migrate(app, db)

    seeder = FlaskSeeder()
    seeder.init_app(app, db)

    from apps.section07.views import section07
    app.register_blueprint(section07, url_prefix="/section07")

    from apps.section08.views import section08
    app.register_blueprint(section08, url_prefix="/section08")

    from apps.section09.views import section09
    app.register_blueprint(section09, url_prefix="/section09")

    from apps.section10.views import section10
    app.register_blueprint(section10, url_prefix="/section10")

    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, internal_server_error)

    app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
    DebugToolbarExtension(app)

    return app


def page_not_found(e):
    """ 404 Not Found  """
    return render_template("404.html"), 404


def internal_server_error(e):
    """ 500 Internal Server Error """
    return render_template("500.html"), 500
