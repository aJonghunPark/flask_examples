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

    from apps.section07 import views as section07_views
    app.register_blueprint(section07_views.section07, url_prefix="/section07")

    from apps.section08 import views as section08_views
    app.register_blueprint(section08_views.section08, url_prefix="/section08")

    from apps.section09 import views as section09_views
    app.register_blueprint(section09_views.section09, url_prefix="/section09")

    from apps.section10 import views as section10_views
    app.register_blueprint(section10_views.section10, url_prefix="/section10")

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
