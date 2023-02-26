import os

from flask import Flask
from flask_dance.contrib.google import make_google_blueprint
from flask_debugtoolbar import DebugToolbarExtension
from flask_jwt import JWT
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_seeder import FlaskSeeder
from flask_sqlalchemy import SQLAlchemy

from apps.config import config
from apps.section14.secure_check import authenticate, identity

db = SQLAlchemy()

login_manager = LoginManager()

# os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
# os.environ["OAUTHLIB_RELAX_TOKEN_SCOPE"] = "1"


def create_app(config_key):
    app = Flask(__name__)
    app.config.from_object(config[config_key])
    # print(app.config["GOOGLE_CLIENT_ID"])
    # print(app.config["GOOGLE_CLIENT_SECRET"])
    # print(app.config["SECRET_KEY"])

    db.init_app(app)
    Migrate(app, db)

    seeder = FlaskSeeder()
    seeder.init_app(app, db)

    login_manager.init_app(app)
    # login_manager.login_view = "section12.login"

    JWT(app, authenticate, identity)

    from apps.section07.views import section07

    app.register_blueprint(section07, url_prefix="/section07")

    from apps.section08.views import section08

    app.register_blueprint(section08, url_prefix="/section08")

    from apps.section09.views import section09

    app.register_blueprint(section09, url_prefix="/section09")

    from apps.section10.views import section10

    app.register_blueprint(section10, url_prefix="/section10")

    from apps.section12.views import section12

    app.register_blueprint(section12, url_prefix="/section12")

    oauth_google = make_google_blueprint(
        client_id=app.config["GOOGLE_CLIENT_ID"],
        client_secret=app.config["GOOGLE_CLIENT_SECRET"],
        offline=True,
        scope=["profile", "email"],
        redirect_url="/oauth/welcome",
    )
    app.register_blueprint(oauth_google, url_prefix="/oauth/login")

    from apps.oauth.views import oauth

    app.register_blueprint(oauth, url_prefix="/oauth")

    from apps.blog.views import blog

    app.register_blueprint(blog, url_prefix="/blog")

    from apps.section14.simple import simple

    app.register_blueprint(simple, url_prefix="/api")

    from apps.section14.crud import crud

    app.register_blueprint(crud, url_prefix="/api")

    from apps.section16.views import section16

    app.register_blueprint(section16, url_prefix="/section16")

    # app.register_error_handler(404, page_not_found)
    # app.register_error_handler(500, internal_server_error)

    app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
    DebugToolbarExtension(app)

    return app


# def page_not_found(e):
#     """ 404 Not Found  """
#     return render_template("404.html"), 404
#
#
# def internal_server_error(e):
#     """ 500 Internal Server Error """
#     return render_template("500.html"), 500
